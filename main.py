

def get_age():
    while True:
        try:
            age = int(input("Введите ваш возраст: "))
            return age
        except ValueError:
            print("Ошибка: введите возраст числом.")


def get_user_data():
    age = get_age()
    citizen = input("Вы гражданин страны? (да/нет): ").lower()
    restriction = input("Есть ли у вас запрет на голосование? (да/нет): ").lower()
    return age, citizen, restriction


def can_vote(age, citizen, restriction):
    return age >= 18 and citizen == "да" and restriction == "нет"


def show_result(result):
    if result:
        print("Вы можете голосовать.")
    else:
        print("Вы не можете голосовать.")


age, citizen, restriction = get_user_data()
result = can_vote(age, citizen, restriction)
show_result(result)