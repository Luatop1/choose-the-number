import random
attempts = 0
while True:
    try:
        user_number = int(input("Угадайте число! от 1 до 25: "))
        attempts += 1
        break
    except ValueError:
        print("Введите число!")
number = random.randint(1, 25)

while True:
    if user_number != number:
        attempts += 1
        if user_number > number:
            print("Меньше")
        elif user_number < number:
            print("Больше")
        while True:
            try:
                user_number = int(input("Попробуйте еще раз: "))
                break
            except ValueError:
                print("Введите число!")
    else:
        read_file = open("data/record.txt", "r")
        saved_attempt = int(read_file.read(2))
        if attempts < saved_attempt:
            print(f"Вы побили рекорд, угадав число за {attempts} попыток! Ваш новый рекорд {attempts}")
            read_file.close()
            write_file = open("data/record.txt", "w")
            write_file.write(str(attempts))
            write_file.close()
        else:
            print(f"Вы угадали число за {attempts} попыток! Ваш рекорд: {saved_attempt}")
            read_file.close()
        break