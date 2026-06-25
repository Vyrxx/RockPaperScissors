from random import*
print("Игра Камень-Ножницы-Бумага")
print("Камень бьет ножницы")
print("Ножницы бьют бумагу")
print("Бумага бьет камень")
print("За победу 1 балл, за ничью 0")
print("Игра продолжится до тех пор пока у кого-то из участников будет 3 балла")
game = ["Камень", "Бумага", "Ножницы"]

def get_computer_choice():
    bot = choice(game)
    return bot

def determine_winner(p,b):
    print("Вы:",str(p),"Бот:",str(b))
    if p == 3:
        print("Поздравляю, вы выиграли!")
        return True
    elif b == 3:
        print("К сожалению, вы проиграли:(")
        return True
    return False


def main():
    pscore = 0
    bscore = 0
    while True:
        player = input("Выберите (Камень, Ножницы, Бумага): ").capitalize()
        bot = get_computer_choice()
        if player not in game:
            print("Неправильно выбрали")
        else:
            print("Бот выбрал: " + bot)
            if player == bot:
                print("")
            elif player == "Камень":
                if bot == "Ножницы":
                    pscore += 1
                else:
                    bscore += 1
            elif player == "Ножницы":
                if bot == "Бумага":
                    pscore += 1
                else:
                    bscore += 1
            else:
                if bot == "Камень":
                    pscore += 1
                else:
                    bscore += 1
        if determine_winner(pscore, bscore):
            answer = input("Хотите сыграть еще раз?").capitalize()
            if answer == "Да":
                main()
            else:
                break

main()