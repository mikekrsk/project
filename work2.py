# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input("Введите количество секунд: "))

hour = seconds // 3600
minute = (seconds - hour * 3600) // 60
sec = seconds - (hour * 3600 + minute * 60)

print(f"{hour}:{minute}:{sec}.")
