fio_input = input("Введите фамилию, имя и отчество: ").split()

last_name = fio_input[0] 
first_name = fio_input[1] 
middle_name = fio_input[2]
result = f"{last_name.capitalize()} {first_name[0].upper()}.{middle_name[0].upper()}."
print(f"Вывод: {result}")

