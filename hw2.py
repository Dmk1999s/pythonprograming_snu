{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyP8WtRqFlLqpKGt0Jz18IKI",
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
        "def get_radius(prompt):\n",
        "  r = int(input(prompt))\n",
        "  return r\n",
        "\n",
        "R = get_radius(\"넓이를 구하고자 하는 원의 반지름은? \")\n",
        "def get_circle_area():\n",
        "  area = R * R * 3.14\n",
        "  return print(\"반지름이 %d인 원의 넓이 = 3.14 x %d x %d = %.02f\" %(R, R, R, area))\n",
        "get_circle_area()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9hfybSaSOer_",
        "outputId": "2416867f-98e8-4ec8-9a2e-4b06d5fbb1ef"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "넓이를 구하고자 하는 원의 반지름은? 4\n",
            "반지름이 4인 원의 넓이 = 3.14 x 4 x 4 = 50.24\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "kCyWIPQXRURC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "V5aO-TYSPnHL"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}