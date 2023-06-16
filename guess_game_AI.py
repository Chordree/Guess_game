import random
import ai_players as ai

# NOTE rename this file properly 

# allow for user input name... remove all test comments 

#  the prameter a added in the check_win would account for switching
print('Welcome to this thrilling guessing game ')
def difficultymode():
    print('enter [E] for easy mode, [M] for medium mode or [H] for Hard mode ')
    diff_val = input('enter difficulty level("E" or "M" or "H"): ').strip().upper()
    while diff_val not in ['E', 'M', 'H']:
        print('you didn\'t eneter a valid choice , pls read the instructions below')
        diff_val = input('enter difficulty level("E" or "M" or "H"): ').strip().upper()

    return diff_val

mode = difficultymode()    

def check_win(a):
    guess = 'ab'  # this is just to ensure a neutral non numeric  value for guess before starting..to trigger while loop
    if a % 2 == 0:
        num = random.randrange(1, 11)
        print('AI has placed the secret number: *')
    else:
        num = human_input()
    count = 0
    
    
    while guess != num and count < 3:
        if a % 2 == 0:
            guess = human_input()       # input('guess a number btw 1 and 10: ')
        else:
            guess = comp_player(mode, num)
            count = 3  # i made count = 3 at once cause AI input takes care of all the iterations/ ai turn counts
            # you can also use a break here intead of settting count = 3 ..check the differnece
            print('aI is done guessing ')  # remove this later on 
            
            
        if guess > num:
            print('too high, try again')
        if guess < num:
            print('too low, try again')
        count += 1

        if guess == num:
            print(' yeah ..the guess was right.. nice one ')
            return True

    if guess != num:
        print('end of turn ..switching')
        # return False
        # since it doesn't return anything it returns NONE ..which is just like false, return False above is optional
    print(num)


def comp_player(diff_var, hidden_num):
    if diff_var == 'E':
        return ai.ai_easy(hidden_num)
    elif diff_var == 'M':
        return ai.ai_medium(hidden_num)
    elif diff_var == 'H':
        return ai.ai_hard(hidden_num)


def human_input():
    while True:       # isdigit fuction call can also be used also be used in place of try/except block below 
        try:
            val = int(input('enter a number btw 1 and 10: '))
            if not 1 <= val <= 10:
                print('pls enter a correct value btw 1 and 10')
                continue
            break
        except ValueError:
            print('pls enter a number ')
            continue
            
    return val



def main():
    p1 = 'AI'
    p2 = 'you' #Todo: ask  user to enter name here  .. if need be

    print('The game starts now. ')
    scores_p1, scores_p2 = 0, 0  # scores can be 2 for guessing right or +1 to the opponent
    switcher = 0

    while scores_p1 < 4 and scores_p2 < 4:
        if switcher % 2 == 0:
            c, b = p1, p2
        else:
            c, b = p2, p1
        print(c, 'will  input hidden number', b, 'turn to guess')
        if check_win(switcher):
            if c == p1:
                scores_p2 += 1
            if c == p2:
                scores_p1 += 1

        else:
            if c == p1:
                scores_p1 += .5
            if c == p2:
                scores_p2 += .5

        switcher += 1
        print(f'scoreboard is  >>> {p1} {scores_p1} vs {scores_p2} {p2} <<< ')

    if scores_p1 > scores_p2:
        print('the winner is', p1)
    else:
        print('the winner is', p2)  


main()

#TODO: list below 
# create a version without hint for the human_player .
# a comination that can switch btw multiplayer and AI.
