import random
import os

clear = lambda: os.system('clear')
clear()

# sitting up the game

deck_name_list = [
    'ace', 'tow', 'three', 'four', 'five', 'six', 'seven', 'eghit', 'nine',
    'ten', 'jack', 'queen', 'king'
]
deck_num_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# first dealing for dealer and user
dealer = []
dealer_total = 0
user = []
user_total = 0
for i in range(2):
    dealer_cards = random.choice(deck_name_list)
    dealer.append(dealer_cards)
    dealer_total += deck_num_list[deck_name_list.index(dealer_cards)]
    user_cards = random.choice(deck_name_list)
    user.append(user_cards)
    user_total += deck_num_list[deck_name_list.index(user_cards)]
print(f'\nYour cards are {user} with a total of {user_total}')
print(
    f'\nDealer first card is {dealer[0]} with value of {deck_num_list[deck_name_list.index(dealer[0])]}\n '
)

# hit or stand
end_game = False
while end_game == False:
    if user_total > 21:
        print(
            f'Your total is {user_total} more than 21, you got Bust, you lost')
        end_game = True
    elif user_total == 21:
        print('you won')
        end_game = True
    else:
        hit_or_stand = input('for Hit type Y for stand type N: ').upper()
        if hit_or_stand == 'Y':
            clear()
            user_cards = random.choice(deck_name_list)
            user.append(user_cards)
            user_total += deck_num_list[deck_name_list.index(user_cards)]
            print(f'\nYour cards are {user} with a total of {user_total}')
            print(
                f'\nDealer first card is {dealer[0]} with value of {deck_num_list[deck_name_list.index(dealer[0])]}\n '
            )
        elif hit_or_stand == 'N':
            clear()
            print(f'\nYour cards are {user} with a total of {user_total}')
            print(
                f'\nDealer  cards are {dealer} with value of {dealer_total}\n '
            )
            if dealer_total < 17:
                dealer_cards = random.choice(deck_name_list)
                dealer.append(dealer_cards)
                dealer_total += deck_num_list[deck_name_list.index(
                    dealer_cards)]
                print(
                    f'Dealer hand less than 17, dealer take one card: {dealer_cards}'
                )
                print(f'\nYour cards are {user} with a total of {user_total}')
                print(
                    f'\nDealer first card is {dealer} with value of {dealer_total}\n '
                )
                if dealer_total > 21:
                    print('You Win!!!')
                    end_game = True
                elif dealer_total == 21:
                    print('You lose!!!')
                    end_game = True
                else:
                    if user_total > dealer_total:
                        print('You Win!!!')
                        end_game = True
                    elif user_total == dealer_total:
                        print('Draw!!!')
                        end_game = True
                    else:
                        print('You lose!!!')
                        end_game = True
            else:
                if user_total > dealer_total:
                    print('You Win!!!')
                    end_game = True
                elif user_total == dealer_total:
                    print('Draw!!!')
                    end_game = True
                else:
                    print('You lose!!!')
                    end_game = True
        else:
            print('Wrong Entry...! ')
