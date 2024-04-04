{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "dbe95d73-02e6-409c-950b-7f683f32be1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "할인율은?  20\n",
      "A 상품의 할인된 가격은?  8000\n",
      "B 상품의 할인된 가격은?  10200\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A 상품의 정가는 12500 원\n",
      "B 상품의 정가는 15938 원\n"
     ]
    }
   ],
   "source": [
    "def get_fixed_price(discount_rate, discounted_price):\n",
    "    # 할인 전 가격을 계산\n",
    "    fixed_price = discounted_price / (1 - discount_rate / 100)\n",
    "    return fixed_price\n",
    "\n",
    "# 할인율과 상품의 할인 가격 입력 받기\n",
    "discount_rate = int(input(\"할인율은? \"))\n",
    "discounted_price_a= int(input(\"A 상품의 할인된 가격은? \"))\n",
    "discounted_price_b = int(input(\"B 상품의 할인된 가격은? \"))\n",
    "\n",
    "# 할인 전 가격 계산\n",
    "fixed_price_A = get_fixed_price(discount_rate, discounted_price_a)\n",
    "fixed_price_B = get_fixed_price(discount_rate, discounted_price_b)\n",
    "\n",
    "# 정가 출력\n",
    "print(\"A 상품의 정가는\", round(fixed_price_A / (1 - discount_rate / 100)), \"원\")\n",
    "print(\"B 상품의 정가는\", round(fixed_price_B / (1 - discount_rate / 100)), \"원\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3dc62d6-a67b-47c3-9271-c0edb17d81e3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
