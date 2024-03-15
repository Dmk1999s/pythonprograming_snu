{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPy/0/N+jxo/zlGYVwyFTUq",
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
        "<a href=\"https://colab.research.google.com/github/Dmk1999s/pythonprograming_snu/blob/main/hw1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5yAsQa8dxRth",
        "outputId": "1573963e-8888-4ea9-84d9-5c540c70e809"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n"
          ]
        }
      ],
      "source": [
        "print(2+3)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def show_message(msg='안녕하세요',name='여러분'):\n",
        "  print(msg,name,'님')\n",
        "\n",
        "print('시작')\n",
        "show_message('안녕','이찬수')\n",
        "show_message('안녕')\n",
        "show_message()\n",
        "show_message(name='이찬수')\n",
        "show_message(msg='안녕')\n",
        "print('마침')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ptPgEzgoxUEW",
        "outputId": "7cef5174-58bb-42c3-f10a-a2146590b0d4"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "시작\n",
            "안녕 이찬수 님\n",
            "안녕 여러분 님\n",
            "안녕하세요 여러분 님\n",
            "안녕하세요 이찬수 님\n",
            "안녕 여러분 님\n",
            "마침\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import cv2\n",
        "cv2.__version__"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "8R4NfmSq16-5",
        "outputId": "6b3e4069-7e4e-4a37-92b6-e874e261ad62"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'4.8.0'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def show_message() :\n",
        "  print('hello')\n",
        "  return 'good bye'\n",
        "\n",
        "print('시작')\n",
        "result = show_message()\n",
        "print(result)\n",
        "print('마침')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ytaOfw8CBKUo",
        "outputId": "19591a14-ed71-455d-a4ff-4bb31cf854ce"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "시작\n",
            "hello\n",
            "good bye\n",
            "마침\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def make_message(name):\n",
        "  return print(\"당신의 이름은 \" + name)\n",
        "\n",
        "input_name = input(\"당신의 이름은?\")\n",
        "make_message(input_name)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ypwhDoYYCd1k",
        "outputId": "8487279b-2f64-4589-8596-81091f9ebca3"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "당신의 이름은?dmksdmkasl\n",
            "당신의 이름은 dmksdmkasl\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def make_message():\n",
        "  name = input(\"당신의 이름은? \")\n",
        "  msg = '반가워요 ' + name\n",
        "  return msg\n",
        "\n",
        "result = make_message()\n",
        "print('만나게 되어', result)\n",
        "print(result, '좋은 인연 만들어가요')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "22s_UmOaLT7A",
        "outputId": "b28e1010-6a71-4b6f-d6bb-e7acdebae3ea"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "당신의 이름은? 김씨\n",
            "만나게 되어 반가워요 김씨\n",
            "반가워요 김씨 좋은 인연 만들어가요\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def get_radius():\n",
        "  r = int(input(\"넓이를 구하고자 하는 원의 반지름은? \"))\n",
        "  return r\n",
        "\n",
        "R = get_radius()\n",
        "def get_circle_area():\n",
        "  area = R * R * 3.14\n",
        "  return print(\"반지름이 %d인 원의 넓이 = 3.14 x %d x %d = %.02f\" %(R, R, R, area))\n",
        "get_circle_area()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BVDQJIK2NUUo",
        "outputId": "0342c2b2-e4b3-40db-c052-34170863d61a"
      },
      "execution_count": 25,
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
        "id": "V5aO-TYSPnHL"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}