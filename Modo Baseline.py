{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNjqZHsgtjSOEC1tg8nFng0",
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
        "<a href=\"https://colab.research.google.com/github/dimagela29/Blackhat-e-chatbot/blob/master/Modo%20Baseline.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "F3r80E4X8GHT",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "693760d6-101e-4e3a-ea9c-5ba3cb9b88a5"
      },
      "source": [
        "#importação dos modulos\n",
        "from pandas import read_csv\n",
        "from sklearn.model_selection import KFold\n",
        "from sklearn.model_selection import cross_val_score\n",
        "from sklearn.naive_bayes import GaussianNB\n",
        "\n",
        "#carregando os dados\n",
        "arquivo = '/home/pima-indians-diabetes.csv'\n",
        "colunas = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']\n",
        "dados = read_csv(arquivo, names = colunas)\n",
        "array = dados.values\n",
        "\n",
        "#separando o array em componentes de input e output\n",
        "X = array[:,0:8]\n",
        "Y = array[:,8]\n",
        "\n",
        "#definindo os valores para o numero de folds\n",
        "num_folds = 10\n",
        "seed = 7\n",
        "\n",
        "#separando oss dados em folds\n",
        "kfold = KFold(num_folds, True, random_state= seed)\n",
        "\n",
        "#criando o modelo\n",
        "modelo = GaussianNB()\n",
        "\n",
        "#cros Validation\n",
        "resultado = cross_val_score(modelo, x, Y, cv = kfold)\n",
        "\n",
        "#print do resultado\n",
        "print('Acurácia: %.3f' % (resultado.mean() * 100))\n"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Acurácia: 75.914\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "olVI3K6lEs7D",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gabRqi7uDwIh",
        "colab_type": "text"
      },
      "source": [
        ""
      ]
    }
  ]
}