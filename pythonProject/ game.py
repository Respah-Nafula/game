import random
number=random.randint(1,10)
player_name =input("Hello, what is your name?")
print('okay! '+ player_name+ ' you are guessing a number between 1 and 10:')
while number < 5:
    guess =int(input())
    number +=1
    if guess <number: 
        print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
            if guess == number:
                break
            if guess == number:
                 print('You guessed the number in ' + str(number + ' tries!'))
else:
    print('You did not guess the number, The number was ' + str(number))
