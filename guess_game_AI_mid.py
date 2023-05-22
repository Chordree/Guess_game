import random

#  the prameter a added in the check_win would account for switching
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
            guess = AI_input(num)
            count = 3  # i made count = 3 at once cause AI input takes care of all the iterations/ ai turn counts
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


def AI_input(MAGIC_NUM):
    guess = 'a'    # see if this is necessary
    count = 0
    used_nums = []
    b = 1
    l = 11
    while guess != MAGIC_NUM and count < 3:
        guess = random.randrange(b, l)
        
        print('ai guessed the number: ', guess)
        while guess in used_nums:
            guess = random.randrange(b, l)
            print('guess again is', guess)
        if not 1 <= guess <= 10:
            print('pls enter a correct value btw 1 and 10')
            # this if would never execute. since AI input would never go out of range 
            # the code would still work fine .. if this if block above is commented well .. see while/else block
            # the else works when the while executes to false .. so if the if is removed, when the while executes to false the else is excuted
            # i.e the else excutes so far the loop is not broken, i.e breaking a while loop is not same as setting trigger condition to false
        else:
            if guess > MAGIC_NUM:
                print('too high, try again')
                hint = 'h'
                l = guess + 1  # this was done intentionally to avoid any clashes .. i.e range(5, 5) e.t.c
            if guess < MAGIC_NUM:
                print('too low, try again')
                hint = 'l'
                b = guess + 1

        if guess == MAGIC_NUM:
            print('yeah nice one i read your mind right')
            break
        count += 1
        used_nums.append(guess)
        

    if guess != MAGIC_NUM:
        print('end of turn try harder next time')

    return guess

def human_input():
    while True:       # isdigit fuction call also be used here 
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


# if AI is selected turns should alternate btw AI Human
# if human is selected ... all turn calls should just be human inputs
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
# create a version without hint for the user .
# try a 4567 Ai version ..
# create a fuction to handle all leves of aI.
# a comination that can switch btw multiplayer and AI.