secret_number=9
guess_count=1
trials=3

while guess_count<=trials:
    guess = int(input('Guess: '))
    guess_count+=1
    
    if guess==secret_number:
        print('You guessed it!!')
        break
else:
    print('Game Over')
    