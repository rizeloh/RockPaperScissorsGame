import random

def get_computer_choice():
    """
    Возвращает случайный выбор компьютера: 'камень', 'ножницы' или 'бумага'.
    """
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)

def get_player_choice():
    """
    Запрашивает у игрока выбор: 'камень', 'ножницы' или 'бумага'.
    """
    choice = ""
    while choice not in ['камень', 'ножницы', 'бумага']:
        print("Выберите: камень, ножницы или бумага")
        choice = input("> ").lower()
    return choice

def determine_winner(player, computer):
    """
    Определяет победителя на основе выборов игрока и компьютера.
    """
    if player == computer:
        return "Ничья!"
    elif (player == 'камень' and computer == 'ножницы') or \
         (player == 'ножницы' and computer == 'бумага') or \
         (player == 'бумага' and computer == 'камень'):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

def play_game():
    """
    Основная функция игры.
    """
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print(f"Ваш выбор: {player_choice}")
    print(f"Выбор компьютера: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
