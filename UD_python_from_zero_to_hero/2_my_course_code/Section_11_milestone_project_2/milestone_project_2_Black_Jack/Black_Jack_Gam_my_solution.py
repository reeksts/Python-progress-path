import random


class CreatePlayer:
    def __init__(self):
        self.player_credit = 0
        self.player_bet = 0

    def add_credit(self, amount):
        self.player_credit = amount        

    def add_bet(self, amount):
        self.player_bet = amount
        self.player_credit = self.player_credit - self.player_bet

    def add_funds(self, amount):
        self.player_credit = self.player_credit + amount

    def show_credit(self):
        return self.player_credit
    

class CreateDeck:
    def __init__(self):
        self.player_card_tag_count = []
        self.player_card_value_count = []
        self.player_card_suit_count = []

        self.pc_card_tag_count = []
        self.pc_card_value_count = []
        self.pc_card_suit_count = []
        
        self.hearts = '\u2665'
        self.diamonds = '\u2666'
        self.spades = '\u2660'
        self.clubs = '\u2663'

        self.sum_1 = 0
        self.sum_2 = 0
        self.sum_3 = 0
        self.sum_4 = 0
        self.player_final = 0

        self.player_bank = 0
        self.player_bet = 0
        
        a1 = {'h_two': [2, 2], 'suit' : self.hearts}
        a2 = {'d_two' : [2, 2], 'suit' : self.diamonds}
        a3 = {'s_two' : [2, 2], 'suit' : self.spades}
        a4 = {'c_two' : [2, 2], 'suit' : self.clubs}
        a5 = {'h_three' : [3, 3], 'suit' : self.hearts}
        a6 = {'d_three' : [3, 3], 'suit' : self.diamonds}
        a7 = {'s_three' : [3, 3], 'suit' : self.spades}
        a8 = {'c_three' : [3, 3], 'suit' : self.clubs}
        a9 = {'h_four' : [4, 4], 'suit' : self.hearts}
        a10 = {'d_four' : [4, 4], 'suit' : self.diamonds}
        a11 = {'s_four' : [4, 4], 'suit' : self.spades}
        a12 = {'c_four' : [4, 4], 'suit' : self.clubs}
        a13 = {'h_five' : [5, 5], 'suit' : self.hearts}
        a14 = {'d_five' : [5, 5], 'suit' : self.diamonds}
        a15 = {'s_five' : [5, 5], 'suit' : self.spades}
        a16 = {'c_five' : [5, 5], 'suit' : self.clubs}
        a17 = {'h_six' : [6, 6], 'suit' : self.hearts}
        a18 = {'d_six' : [6, 6], 'suit' : self.diamonds}
        a19 = {'s_six' : [6, 6], 'suit' : self.spades}
        a20 = {'c_six' : [6, 6], 'suit' : self.clubs}
        a21 = {'h_seven' : [7, 7], 'suit' : self.hearts}
        a22 = {'d_seven' : [7, 7], 'suit' : self.diamonds}
        a23 = {'s_seven' : [7, 7], 'suit' : self.spades}
        a24 = {'c_seven' : [7, 7], 'suit' : self.clubs}
        a25 = {'h_eight' : [8, 8], 'suit' : self.hearts}
        a26 = {'d_eight' : [8, 8], 'suit' : self.diamonds}
        a27 = {'s_eight' : [8, 8], 'suit' : self.spades}
        a28 = {'c_eight' : [8, 8], 'suit' : self.clubs}
        a29 = {'h_nine' : [9, 9], 'suit' : self.hearts}
        a30 = {'d_nine' : [9, 9], 'suit' : self.diamonds}
        a31 = {'s_nine' : [9, 9], 'suit' : self.spades}
        a32 = {'c_fine' : [9, 9], 'suit' : self.clubs}
        a33 = {'h_ten' : [10, 10], 'suit' : self.hearts}
        a34 = {'d_ten' : [10, 10], 'suit' : self.diamonds}
        a35 = {'s_ten' : [10, 10], 'suit' : self.spades}
        a36 = {'c_ten' : [10, 10], 'suit' : self.clubs}
        a37 = {'h_jack' : ['J', 10], 'suit' : self.hearts}
        a38 = {'d_jack' : ['J', 10], 'suit' : self.diamonds}
        a39 = {'s_jack' : ['J', 10], 'suit' : self.spades}
        a40 = {'c_jack' : ['J', 10], 'suit' : self.clubs}
        a41 = {'h_queen' : ['Q', 10], 'suit' : self.hearts}
        a42 = {'d_queen' : ['Q', 10], 'suit' : self.diamonds}
        a43 = {'s_queen' : ['Q', 10], 'suit' : self.spades}
        a44 = {'c_queen' : ['Q', 10], 'suit' : self.clubs}
        a45 = {'h_king' : ['K', 10], 'suit' : self.hearts}
        a46 = {'d_king' : ['K', 10], 'suit' : self.diamonds}
        a47 = {'s_king' : ['K', 10], 'suit' : self.spades}
        a48 = {'c_king' : ['K', 10], 'suit' : self.clubs}
        a49 = {'h_ace' : ['A', [1,11]], 'suit' : self.hearts}
        a50 = {'d_ace' : ['A', [1,11]], 'suit' : self.diamonds}
        a51 = {'s_ace' : ['A', [1,11]], 'suit' : self.spades}
        a52 = {'c_ace' : ['A', [1,11]], 'suit' : self.clubs}
        

        self.deck = [a1, a2, a3, a4, a5, a6, a7, a8,
                     a9, a10, a11, a12, a13, a14, a15, a16,
                     a17, a18, a19, a20, a21, a22, a23, a24,
                     a25, a26, a27, a28, a29, a30, a31, a32,
                     a33, a34, a35, a36, a37, a38, a39, a40,
                     a41, a42, a43, a44, a45, a46, a47, a48,
                     a49, a50, a51, a52]
        
    def shuffle_deck(self):
        random.shuffle(self.deck)

    def player_takes_card(self):
        card = self.deck[-1]
        card_keys = list(card.keys())

        card_info = card.get(card_keys[0])
        card_tag = card_info[0]
        self.player_card_tag_count.append(card_tag)

        card_value = card_info[1]
        self.player_card_value_count.append(card_value)

        card_suit = card.get(card_keys[1])
        self.player_card_suit_count.append(card_suit)

        self.deck.pop(-1)

        sum_count_1 = 0
        sum_count_2 = 0
        for i in self.player_card_value_count:
            if isinstance(i, int):
                sum_count_1 += i
                sum_count_2 += i
            else:
                sum_count_1 += i[0]
                sum_count_2 += i[1]
        self.sum_1 = sum_count_1
        self.sum_2 = sum_count_2

    def pc_takes_card(self):
        card = self.deck[-1]
        card_keys = list(card.keys())

        card_info = card.get(card_keys[0])
        card_tag = card_info[0]
        self.pc_card_tag_count.append(card_tag)

        card_value = card_info[1]
        self.pc_card_value_count.append(card_value)

        card_suit = card.get(card_keys[1])
        self.pc_card_suit_count.append(card_suit)

        sum_count_3 = 0
        sum_count_4 = 0
        for i in self.pc_card_value_count:
            if isinstance(i, int):
                sum_count_3 += i
                sum_count_4 += i
            else:
                sum_count_3 += i[0]
                sum_count_4 += i[1]
        self.sum_3 = sum_count_3
        self.sum_4 = sum_count_4

    def show_sum(self):
        return (self.sum_1, self.sum_2)

    def show_sum_2(self):
        return (self.sum_3, self.sum_4)

    def player_fin(self):
        if self.sum_1 == self.sum_2:
            self.player_final = self.sum_1
        elif self.sum_2 > 21:
            self.player_final = self.sum_1
        else:
            self.player_final = self.sum_2
        return self.player_final

    def change_fin(self):
        self.player_final = 1

    def show_table_1(self):
        length_1 = len(self.player_card_tag_count)
       
        counter_1 = 0
        player_value_list_upper = []
        player_value_list_lower = []        
        player_suits_list = []
        for i in range(length_1):
            if isinstance(self.player_card_tag_count[counter_1], str):
                player_value_list_upper.append('|{}        |   '.format(self.player_card_tag_count[counter_1]))
                player_value_list_lower.append('|        {}|   '.format(self.player_card_tag_count[counter_1]))
            else:            
                if self.player_card_tag_count[counter_1] < 10:
                    player_value_list_upper.append('|{}        |   '.format(self.player_card_tag_count[counter_1]))
                    player_value_list_lower.append('|        {}|   '.format(self.player_card_tag_count[counter_1]))
                elif self.player_card_tag_count[counter_1] == 10:
                    player_value_list_upper.append('|{}       |   '.format(self.player_card_tag_count[counter_1]))
                    player_value_list_lower.append('|       {}|   '.format(self.player_card_tag_count[counter_1]))
            player_suits_list.append('|    {}    |   '.format(self.player_card_suit_count[counter_1]))
            counter_1 += 1

        length_2 = len(self.pc_card_tag_count)
        
        counter_2 = 0
        pc_value_list_upper = []
        pc_value_list_lower = []        
        pc_suits_list = []
        for i in range(length_2):
            if isinstance(self.pc_card_tag_count[counter_2], str):
                pc_value_list_upper.append('|{}        |   '.format(self.pc_card_tag_count[counter_2]))
                pc_value_list_lower.append('|        {}|   '.format(self.pc_card_tag_count[counter_2]))
            else:            
                if self.pc_card_tag_count[counter_2] < 10:
                    pc_value_list_upper.append('|{}        |   '.format(self.pc_card_tag_count[counter_2]))
                    pc_value_list_lower.append('|        {}|   '.format(self.pc_card_tag_count[counter_2]))
                elif self.pc_card_tag_count[counter_2] == 10:
                    pc_value_list_upper.append('|{}       |   '.format(self.pc_card_tag_count[counter_2]))
                    pc_value_list_lower.append('|       {}|   '.format(self.pc_card_tag_count[counter_2]))
            pc_suits_list.append('|    {}    |   '.format(self.pc_card_suit_count[counter_2]))
            counter_2 += 1

        if self.player_final == 0:
            
            print('\n'*40)

            print('           '+'-----------   '+'-----------')         
            print('           '+'{}'.format(pc_value_list_upper[1])+'| \     / |')
            print('           '+'|         |   '+'|  \   /  |')
            print('           '+'|         |   '+'|   \ /   |')
            print(' PC:       '+'{}'.format(pc_suits_list[1])+'|    x    |')
            print('           '+'|         |   '+'|   / \   |')
            print('           '+'|         |   '+'|  /   \  |')
            print('           '+'{}'.format(pc_value_list_lower[1])+'| /     \ |')
            print('           '+'-----------   '+'-----------')

        elif self.player_final !=0:
            print('\n'*40)
            
            print('           '+'-----------   '*length_2)         
            print('           '+''.join(pc_value_list_upper))
            print('           '+'|         |   '*length_2)
            print('           '+'|         |   '*length_2)
            print(' PC:       '+''.join(pc_suits_list))
            print('           '+'|         |   '*length_2)
            print('           '+'|         |   '*length_2)
            print('           '+''.join(pc_value_list_lower))
            print('           '+'-----------   '*length_2)

        print('\n'*2)

        print('           '+'-----------   '*length_1)         
        print('           '+''.join(player_value_list_upper))
        print('           '+'|         |   '*length_1)
        print('           '+'|         |   '*length_1)
        print(' PLAYER:   '+''.join(player_suits_list))
        print('           '+'|         |   '*length_1)
        print('           '+'|         |   '*length_1)
        print('           '+''.join(player_value_list_lower))
        print('           '+'-----------   '*length_1)

        if self.sum_1 == self.sum_2:
            print('\nYour sum is {}\n'.format(self.sum_1))
        else:
            print('\nYour sum is {} or {}\n'.format(self.sum_1, self.sum_2))





break_value_1 = 0

print('\n'*40)
print('Welcome to Black Jack game\n\n')
player_in1 = input('Start a new game? YES/NO')
if player_in1.lower() == 'yes':
    pass
elif player_in1.lower() == 'no':
    break_value_1 = 1

player = CreatePlayer()
print('\n'*40)
amount = int(input('Enter you credit'))
player.add_credit(amount)

while break_value_1 != 1:
    break_value_2 = 0

    while True:
        print('\n'*40)
        player_credit = player.show_credit()
        print('\nYour current credit is {}\n'.format(player_credit))
        bet = int(input('Enter you bet'))

        print('\n'*40)
        print('Your bet is {}'.format(bet))
        answer = input('Change bet? YES/NO')
        if answer.lower() == 'yes':
            pass
        if answer.lower() == 'no':
            player_bet = player.add_bet(bet)
            break


    print('\n'*40)
    maingame = CreateDeck()
    maingame.shuffle_deck()

    maingame.player_takes_card()
    maingame.pc_takes_card()
    maingame.player_takes_card()
    maingame.pc_takes_card()   
    maingame.show_table_1()
    a, b = maingame.show_sum()
    while True:
        player_in2 = input('What is your move? HIT or STAND')
        if player_in2.lower() == 'hit':
            maingame.player_takes_card()
            a, b = maingame.show_sum()
            if a > 21:
                maingame.change_fin()
                maingame.show_table_1()
                c, d = maingame.show_sum_2()
                if c == d:
                    print('PC sum is {}'.format(c))
                else:
                    print('PC sum is {} or {}'.format(c, d))
                print('\nYOU LOST\n')
                player_in3 = input('Start a new game? YES/NO')
                if player_in3.lower() == 'yes':
                    break_value_2 = 1
                    break
                elif player_in3.lower() == 'no':
                    break_value_1 = 1
                    break_value_2 = 1
                    break
            elif a <= 21:
                maingame.show_table_1()
        elif player_in2.lower() == 'stand':
            break
    while break_value_2 !=1:
        player_final = maingame.player_fin()
        c, d = maingame.show_sum_2()

        if c == d:
            pc_final = c
        elif c != d:
            if d > 21:
                pc_final = c
            elif d <= 21:
                pc_final = d

        if pc_final == player_final == 21:
            maingame.show_table_1()
            print('PC sum is {}'.format(c))
            print('\nYOU WON!!\n')
            player.add_funds(bet*2)
            player_in4 = input('Start a new game? YES/NO')
            if player_in4.lower() == 'yes':
                break
            elif player_in4.lower() == 'no':
                break_value_1 = 1
                break
        elif pc_final == player_final:
            maingame.pc_takes_card()
        elif pc_final < player_final:
            maingame.pc_takes_card()
        elif pc_final > 21:
            maingame.show_table_1()
            print('PC sum is {}'.format(c))
            print('\nYOU WON!!\n')
            player.add_funds(bet*2)
            player_in4 = input('Start a new game? YES/NO')
            if player_in4.lower() == 'yes':
                break
            elif player_in4.lower() == 'no':
                break_value_1 = 1
                break
        elif pc_final > player_final and pc_final < 21:
            maingame.show_table_1()
            print('PC sum is {}'.format(c))
            print('\nYOU LOST!!\n')
            player_in4 = input('Start a new game? YES/NO')
            if player_in4.lower() == 'yes':
                break
            elif player_in4.lower() == 'no':
                break_value_1 = 1
                break            
                
                
print('\n'*40)                
print('Thanks for the game!!')
            
    








