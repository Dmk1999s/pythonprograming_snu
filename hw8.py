# -*- coding: utf-8 -*-
"""hw8

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15zCyFiFe7wD3WRs0P-FQVDVrUEGZWBMY
"""

shopping_bag = {}

while True:
  print('[구입]')
  name = input('상품명? ')
  if name == '':
    print(f'장바구니 보기: {shopping_bag}')
    break
  num = int(input('수량은? '))
  shopping_bag[name] = num
  print(f'장바구니에 {name} {num}개가 담겼습니다.')

