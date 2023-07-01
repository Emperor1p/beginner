#guess game
secret_number = 7
guess_count = 1
guess_limit = 4
while guess_count < guess_limit:
    guess = int(input('Guess number: '))
    guess_count += 1
    if guess == secret_number:
        print('you won!')
        break
else:
    print('Sorry you failed!')
