import random

secret_code = random.randint(1, 100)

while True:
    guess = int(input("Введите код: "))

    if guess < secret_code:
        print("Больше")
    elif guess > secret_code:
        print("Меньше")
    else:
        print("Код подобран!")
        break