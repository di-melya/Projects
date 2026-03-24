import random
print('Guess the number')
num=random.randint(0,1000)
count=0
while True:
    guess =input()
    if not guess.isdigit():
        print('Please enter a number')
        continue
    guess=int(guess)
    if guess<0 or guess>1000:
        print('Invalid input')
        continue
    count+=1
    if guess>num:
        print('less')
    elif guess<num:
        print('more')
    else:
        print('Great!')
        break