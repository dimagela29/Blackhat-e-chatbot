{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyNDdnmHVGtZY/4HK7XnfnvF",
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
        "<a href=\"https://colab.research.google.com/github/dimagela29/Blackhat-e-chatbot/blob/master/Gradiente%20Boosting.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "djqjGpqcErll",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "b6cfa83a-bcff-4c7c-97dc-7f96562fc167"
      },
      "source": [
        "#import dos modulos\n",
        "from pandas import read_csv\n",
        "from sklearn.model_selection import KFold\n",
        "from sklearn.model_selection import cross_val_score\n",
        "from sklearn.ensemble import GradientBoostingClassifier\n",
        "\n",
        "#Carregando os dados\n",
        "arquivo = '/home/pima-indians-diabetes.csv'\n",
        "colunas = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']\n",
        "dados = read_csv(arquivo, names = colunas)\n",
        "array = dados.values\n",
        "\n",
        "#separando os arrays em componentes de input e output\n",
        "x = array [:,0:8]\n",
        "y = array [:,8]\n",
        "\n",
        "#definindo os valores para o numero de folds\n",
        "num_folds = 10\n",
        "seed = 7\n",
        "\n",
        "#definindo o numero de tress\n",
        "num_tress = 100\n",
        "\n",
        "#separando os dados em folds\n",
        "KFold = KFold(num_folds, True, random_state= seed)\n",
        "\n",
        "#criando o modelo\n",
        "modelo = GradientBoostingClassifier(n_estimators = num_tress, random_state = seed)\n",
        "\n",
        "#cross Validation\n",
        "resultado = cross_val_score(modelo, x, y, cv= KFold)\n",
        "\n",
        "#print do resultado\n",
        "print('Acurácia: %.3f' % (resultado.mean() * 100))"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Acurácia: 76.049\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}