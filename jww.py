def exchange(amount):
    ch500 = amount // 500
    ch100 = (amount - (500 * ch500)) // 100
    ch50 = (amount - (500 * ch500 + 100 * ch100)) // 50
    ch10 = (amount - (500 * ch500 + 100 * ch100 + 50 * ch50)) // 10
    print("500원 동전의 개수: %d" %ch500)
    print("100원 동전의 개수: %d" %ch100)
    print("50원 동전의 개수: %d" %ch50)
    print("10원 동전의 개수: %d" %ch10)

def get_integer(prompt):
    value = int(input(prompt))
    return value

amount = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(amount)

