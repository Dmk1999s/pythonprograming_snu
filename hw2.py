{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO/Bhc4e2fbPn0igaRRJeB0",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/Dmk1999s/pythonprograming_snu/blob/main/hw2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def exchange(amount):\n",
        "    ch500 = amount // 500\n",
        "    ch100 = (amount - (500 * ch500)) // 100\n",
        "    ch50 = (amount - (500 * ch500 + 100 * ch100)) // 50\n",
        "    ch10 = (amount - (500 * ch500 + 100 * ch100 + 50 * ch50)) // 10\n",
        "    print(\"500원 동전의 개수: %d\" %ch500)\n",
        "    print(\"100원 동전의 개수: %d\" %ch100)\n",
        "    print(\"50원 동전의 개수: %d\" %ch50)\n",
        "    print(\"10원 동전의 개수: %d\" %ch10)\n",
        "\n",
        "def get_integer(prompt):\n",
        "    value = int(input(prompt))\n",
        "    return value\n",
        "\n",
        "amount = get_integer(\"동전으로 교환하고자 하는 금액은? \")\n",
        "exchange(amount)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i45s5Js-cVHJ",
        "outputId": "b9b187b7-d26d-46d0-86c1-4990af42a6a5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "동전으로 교환하고자 하는 금액은? 3526\n",
            "500원 동전의 개수: 7\n",
            "100원 동전의 개수: 0\n",
            "50원 동전의 개수: 0\n",
            "10원 동전의 개수: 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "4RV2qLR3cV3X"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}