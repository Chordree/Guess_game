import random, time

def ai_easy( MAGIC_NUM):
    print( MAGIC_NUM)
    guess = 'a' # this is just to initialize the while loop 
    count = 0
    used_nums = []
    while guess != MAGIC_NUM and count < 3:
        guess = random.randrange(1, 11)
        
        while guess in used_nums:
            guess = random.randrange(10)
        print('ai guessed the number: ', guess)    
        if not 0 <= guess <= 9:
            print('pls enter a correct value btw 0 and 9')  # this is just a test case to show the flow 
        else:
            if guess > MAGIC_NUM:
                print('too high, try again')
                hint = 'h'
            if guess < MAGIC_NUM:
                print('too low, try again')
                hint = 'l'

        if guess == MAGIC_NUM:
            print('yeah yeah yeah ..you see i read your mind so well')
            break
        count += 1
        used_nums.append(guess)
        time.sleep(0.5)
    # note the sleep time here was just to make user experience more real..i.e AI can guess the turns in a second 


    if guess != MAGIC_NUM:
        print('end of turn try harder next time')
    
    return guess


def ai_medium(MAGIC_NUM):
    guess = 'a'    # see what happens in you change the value assinged to the initial guess variable 
    count = 0
    used_nums = []
    b = 1
    l = 11
    while guess != MAGIC_NUM and count < 3:
        guess = random.randrange(b, l)
        
        
        while guess in used_nums:
            guess = random.randrange(b, l)
            print('guess again is', guess) # just showing you what happens if AI repeats a previous guess 
        print('ai guessed the number: ', guess)    
        if not 1 <= guess <= 10:
            print('pls enter a correct value btw 1 and 10')
            # this if block would never execute. since AI input would never go out of range 
            # the code would still work fine .. if this if block above is commented well .. see while/else block
            # a while else block was used in the ai_hard fuction below 
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
        time.sleep(0.5)
        

    if guess != MAGIC_NUM:
        print('end of turn try harder next time')
    return guess


# use binary search algorithm code to make the ai_hard cleaner
def ai_hard(MAGIC_NUM):
    guess = 'a'
    count = 0
    used_nums = []
    b = 1
    l = 11
    while guess != MAGIC_NUM and count < 3:
        if count == 0:
            guess = random.choice((4, 5, 6, 7))
            print('ai guessed the number: ', guess)
            if guess == MAGIC_NUM:
                print('yeah!! AI got it right on first attempt')

        elif count == 1:
            # use a random. choice here btw l and l-1 .. # the risk with l is that it can be left with 3 options at last
            e = random.choice((l, l - 1))
            guess = list(range(b, e))[(l - b) // 2]  # better ways to write this
            # len of list can be used here instead of l - b ..this just works .. cause the numbers are consecutive
            # check which is stronger ..using to range l or (l-1) .. run an experiment.. to have higher winning chance
            # still review if just leaving at l - 1 .. l -1 always left with two options at the end
        else:
            guess = random.randrange(b, l)

        print('ai guessed the number: ', guess)
        while guess in used_nums:
            guess = random.randrange(b, l)
            print('guess again is', guess)

         # this is just an example showing how the while/else block works  
        else:
            if guess > MAGIC_NUM:
                print('too high, try again')
                hint = 'h'
                l = guess + 1
            if guess < MAGIC_NUM:
                print('too low, try again')
                hint = 'l'
                b = guess + 1

        if guess == MAGIC_NUM:
            print('nice Job i  got you there')
            break
        count += 1
        used_nums.append(guess)
        time.sleep(0.5)

    if guess != MAGIC_NUM:
        print('end of turn try harder next time')
    return guess

''' note the codes in the fuction above could be written in a cleaner and shorter manner .. 
    but some lines and loops were intentionally added to show some control flow 
'''
