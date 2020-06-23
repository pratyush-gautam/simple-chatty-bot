def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    print('What a great name you have, ' + input() + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.\n(write each in new line respectively)')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    
    print("Your age is " + str(age) + "; that's a good time to start programming!")

def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("\nWhy do we use methods?")
    print('\n1. To repeat a statement multiple times.\n2. To decompose a program into several small subroutines.\n3. To determine the execution time of a program.\n4. To interrupt the execution of a program.\n')
    
    while input() != '2':
    	print('Please, try again.')
    else:
    	print('Completed, have a nice day!')
def end():
	print('Congratulations, have a nice day!')

greet('Aid', '2020')
remind_name()
guess_age()
count()
test()
end()
