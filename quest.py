player = {
    "name": "путник",
    "health": 100,
    "coins": 50,
    "turns": 0,
    "inventory": []
}

def show_status(player):
    print("\n--- Твои характеристики ---")
    for key, value in player.items():
        print(f"{key} - {value}")
    print("---------------------------\n")

def start():
    print("\nТы стоишь у опушки Тёмного леса. Слышен шёпот ветра и далёкий волчий вой.")
    print("Что ты сделаешь?")
    print("  1. Войти в лес")
    print("  2. Вернуться в деревню")
    choice = input("\nТвой выбор: ").lower().strip()
    return choice

def forest_path():
    print("\nТропа петляет между старых деревьев. Впереди виднеется развилка.")
    print("Куда пойдёшь?")
    print("  1. К ручью (нужна чистая вода)")
    print("  2. В чащу (говорят, там растёт лунный мох)")
    print("  3. К старому дубу (легенда о говорящем сове)")
    print("  4. Выйти из леса")
    choice = input("\nТвой выбор: ").lower().strip()
    return choice

def stream(player):
    print("\nУ ручья тихо журчит вода. Но чтобы набрать её, нужно доказать, что ты достоин.")
    solved = False
    while not solved:
        word = input("Назови слово-палиндром (или «выйти», чтобы уйти): ").lower().strip()
        if word == "выйти":
            break
        reversed_word = word[::-1]
        if word == reversed_word and len(word) > 1:
            print("Ручей засиял — ты набрал флягу чистой воды!")
            player["inventory"].append("Фляга чистой воды")
            solved = True
        else:
            print("Вода осталась мутной. Попробуй другое слово-палиндром.")
    return player

def thicket(player):
    print("\nВ чаще воздух густой и пахнет травами. Здесь растёт редкий лунный мох, но он прячется в тени.")
    if "Фляга чистой воды" in player["inventory"]:
        print("Ты полил место водой — и мох засветился! Ты собрал Лунный мох.")
        player["inventory"].append("Лунный мох")
        return player
    else:
        print("Без чистой воды мох не проявится. Сначала сходи к ручью.")
        return player

def old_oak(player):
    print("\nСтарый дуб скрипит, будто шепчет. На ветке сидит мудрая сова.")
    print("Сова говорит: «Чтобы получить корень мандрагоры, ответь на загадку: что растёт без корней, живёт без дыхания, и умирает без воды?»")
    answer = input("Твой ответ: ").lower().strip()
    if answer == "огонь":
        print("Сова кивнула: «Ты мудр». Она дала тебе корень мандрагоры.")
        player["inventory"].append("Корень мандрагоры")
    else:
        print("Сова покачала головой: «Неверно». Но она не прогоняет тебя — попробуй позже.")
    return player

print("\nДобро пожаловать в «Тени Тёмного леса»!")
print("Твоя цель — собрать 3 ингредиента, чтобы сварить зелье и снять проклятие с деревни.\n")

while player["health"] > 0 and player["coins"] >= 0:
    player["turns"] += 1
    show_status(player)
    
    choice = start()

    if choice == "1" or choice == "войти в лес":
        path_choice = forest_path()

        if path_choice == "1":
            player = stream(player)
        elif path_choice == "2":
            player = thicket(player)
        elif path_choice == "3":
            player = old_oak(player)
        elif path_choice == "4":
            print("\nТы выходишь из леса, но проклятие всё ещё висит над деревней...")
            break
        else:
            print("Неверный выбор. Тропа не ведёт туда.")

    elif choice == "2" or choice == "вернуться в деревню":
        if len(player["inventory"]) >= 3:
            print("\nЖители встречают тебя как героя! Ты сварил зелье, и проклятие снято.")
            print("Победа! Ты прошёл игру за", player["turns"], "ходов.")
            break
        else:
            print("\nДеревня всё ещё под проклятием. Тебе нужно больше ингредиентов.")
            print("В твоём инвентаре:", player["inventory"])
    else:
        print("Неверный выбор. Попробуй ещё раз.")
