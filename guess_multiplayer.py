# TODO: make this a two player and AI version

#  count scores and add ..first to max num based on range ..or default
#  for the AI version ..high and low to streamline computer guess

# this works fine ... PWinput.. rename and post on gitHub ..remove all unnecessary comments
import random
import pwinput as pn  # this module is just to mask the secret number from the guesser 
print('you are welcome to the guess game')
print(__name__)  # this line is not needed .. just used it to show what if __name__ = __main__ implies 

# note the AI mode doesn't work here .. i just used it to test the demo round 

# make this call another function that would handle the game sections and all
# this would be removed here and use for the combination where we would have both single and multiplayer
def play_mode():
    game_mode = input('select (M) for multiplayer or (C) to play against computer: ')

    if game_mode.strip().upper() == 'M':
        multiplayer()


    elif game_mode.strip().upper() == 'C':
        play_AI()
        #  see to add switch turn here also
    else:
        print('pls enter a valid input, C or M')
        play_mode()


# to optimize this code ..this function can be renamed  human_player_input().. the checkwin seprated from it
# i.e it would handle all possible errors from human input .. be it secrete num or guess
# see the updated version in the multiplyer and ai version in my repo
def multiplayer():
    while True:
        try:
            magic_number = int(pn.pwinput('enter a number btw 1 and 10:', '*'))
            if not 1 <= magic_number <= 10:
                print('pls enter a correct value btw 1 and 10')
                continue
            break
        except ValueError:
            print('pls enter a number ')
            continue

    
    if check_win(magic_number):
        print('won ..nice game')
        return True


def play_AI():
    magic_number = random.randrange(10)
    check_win(magic_number)


def check_win(num):
    guess = 'a'            # this line is to just ensure a neutral value for guess before starting
    count = 0
    while guess != num and count < 3:
        guess = input('guess a number btw 0 and 9: ')
        try:
            guess = int(guess)
            if not 0 <= guess <= 9:
                print('pls enter a correct value btw 0 and 9')
                count -= 1
                # count is just decremented here to account for mistaken input.. the +1 below will neutralise it
            
            else:
                if guess > num:
                    print('too high, try again')
                if guess < num:
                    print('too low, try again')
            count += 1

        except ValueError:
            print("pls enter a valid number")
        if guess == num:
            print(' you got it right nice one ')
            return True

    if guess != num:
        print('end of turn ..switching')
        # return False
    #  this false statement here not really necessary 
    # ..since a function would return None by default if it has retun value or return True 



def main():
    p1 = input('player1 enter your name: ')
    p2 = input('player2 eneter your name: ')

    print(' the first round you would play is just a demo, doesnt affect the scores')
    play_mode()
    print('the round  above was just a demo, the game ..starts now. ')
    scores_p1, scores_p2 = 0, 0  # scores can be 2 for guessing right or +1 to the opponent
    switcher = 0

    while scores_p1 < 4 and scores_p2 < 4:
        if switcher % 2 == 0:
            c, b = p1, p2
        else:
            c, b = p2, p1
        print(c, 'will  input hidden number', b, 'turn to guess')
        if multiplayer():
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
        print(f'scoreboard is p1={scores_p1} vs p2={scores_p2}')

    print('the winner is', c)  
    # use a condition that prints based on socres .sees c is based on position
    # ..copy condition from pycharm update  


# Editors choice:
#  see how to implement AI , remove unnecessary comments ...set maximum score for competing within a range
# the scores shoud be set based on players choice
#  remove the call of multiplayer function from the play mode...input human/human and AI mode


# add an if statement to continue playing  or while loop with an input to quit 
# major advantage .. i.e only magic input is masked 
if __name__ == '__main__':
    main()
