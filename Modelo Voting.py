{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled2.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPT5Z39CRJnrSOG9sak7lYT",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dimagela29/Blackhat-e-chatbot/blob/master/Modelo%20Voting.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sP_A1P1rLJUm",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "a7b1a904-e747-44a4-de55-57d6be63ebc5"
      },
      "source": [
        "from pandas import read_csv\n",
        "from sklearn.model_selection import KFold\n",
        "from sklearn.model_selection import cross_val_score\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.svm import SVC\n",
        "from sklearn.ensemble import VotingClassifier\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')\n",
        "\n",
        "#carregando os dados\n",
        "arquivo = '/home/pima-indians-diabetes.csv'\n",
        "colunas = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']\n",
        "dados = read_csv(arquivo, names = colunas)\n",
        "array = dados.values\n",
        "\n",
        "#separando o array em componentes de input e output\n",
        "x = array[:,0:8]\n",
        "y = array[:,8]\n",
        "\n",
        "#definindo os valores para numeros de folds\n",
        "num_folds = 10\n",
        "seed = 7\n",
        "\n",
        "#separando os dados em folds\n",
        "KFold = KFold(num_folds, True, random_state = seed)\n",
        "\n",
        "#criando os modelos\n",
        "estimators = []\n",
        "\n",
        "modelo1 = LogisticRegression()\n",
        "estimators.append(('logistic', modelo1))\n",
        "\n",
        "modelo2 = DecisionTreeClassifier()\n",
        "estimators.append(('cart', modelo2))\n",
        "\n",
        "modelo3 = SVC\n",
        "estimators.append(('svm', modelo3))\n",
        "\n",
        "#criando modelos ensemble\n",
        "ensemble = VotingClassifier(estimators)\n",
        "\n",
        "#cross validation\n",
        "resultado = cross_val_score(ensemble, x, y, cv = KFold)\n",
        "\n",
        "print(\"Acuracia: %.3f\" % (resultado.mean() * 100))"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Acuracia: nan\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}