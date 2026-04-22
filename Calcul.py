import random
def adder(x,y):
    '''adds two values returns a sum'''
    return x+y
def timesEm(x,y):
    '''Multiplies two values'''
    return x*y
def divEm(x,y):
    '''return the quotient'''
    return x/y

#num1 = int(input('Num1:'))
#num2 = int(input('Num2:'))
for i in range(5):
    op = random.choice(["+","*","/"])
    num1 =random.randint(1,13)
    num2 =random.randint(1,13)
    user_answer = int(input(f'{num1} {op} {num2} = '))
    if op == "+" and (user_answer ==adder(num1,num2)):
        print('Correct!')
    
    
