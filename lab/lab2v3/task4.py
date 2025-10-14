while True:
    try:
        pol_count = int(input("Сколько знакомых у Пола? "))
        if pol_count >= 0:
            break
        else:
            print("Количество не может быть отрицательным!")
    except ValueError:
        print("Ошибка! Введите целое число.")
pol_friends = set()
for i in range(pol_count):
    friend = input(f"Введите имя знакомого Пола {i+1}: ").strip()
    if friend:
        pol_friends.add(friend)
while True:
    try:
        mari_count = int(input("Сколько знакомых у Мари? "))
        if mari_count >= 0:
            break
        else:
            print("Количество не может быть отрицательным!")
    except ValueError:
        print("Ошибка! Введите целое число.")
mari_friends = set()
for i in range(mari_count):
    friend = input(f"Введите имя знакомого Мари {i+1}: ").strip()
    if friend:
        mari_friends.add(friend)
common_friends = pol_friends & mari_friends
only_pol_friends = pol_friends - mari_friends
only_mari_friends = mari_friends - pol_friends
all_friends = pol_friends | mari_friends
print(f"Общие знакомые: {list(common_friends)}")
print(f"Только знакомые Пола: {list(only_pol_friends)}")
print(f"Только знакомые Мари: {list(only_mari_friends)}")
print(f"Все знакомые: {list(all_friends)}")