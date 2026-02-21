def check_letter(letter):
    if  letter.isalpha():
        return letter
    else:
        print("Input must be letters from A-Z")
        return False
def easygame():
        Easy = {1: 'A region in space with gravity so strong that even light can\'t escape',
                2: 'The planet closest to ours',
                3: 'Earth\'s natural satellite',
                4: 'That force that pulls you down',
                5: 'I exist when the moon blocks the sun',
                6: 'The star at the centre of the earth',
                7: 'I wear a beautiful ring decorated with ice and rocks',
                8: 'A huge ball of gas that produces light and heat(my shape is totally different from afar)',
                9: 'I am the gaseous part of earth',
                10: 'I first landed on moon'

                }
        print("Welcome to the Easy Game\n\n Press * to exit")
        ls = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        tried = []
        while True:
            choice= input("Please enter a number between 1 and 10: ").strip()
            if choice in ls:
                if choice == '1':
                    print('HINT\n', Easy[1])
                    word = "BLACK HOLE"
                    display = []
                    lives = 5
                    guessed_letters = []
                    for letter in word:
                        if letter == " ":
                            display.append(" ")  # keep the space
                        else:
                            display.append("_")  # hide letters

                    while "_" in display and lives > 0:
                        print("\n" + " ".join(display))
                        guess = input("Guess a letter: ").strip().capitalize()

                        if guess in guessed_letters:
                            print("You already guessed that letter!")
                            continue

                        guessed_letters.append(guess)

                        if guess in word:

                            for i in range(len(word)):
                                if word[i] == guess:
                                    display[i] = guess
                        else:
                            lives -= 1
                            print("Wrong guess! Lives left: ", lives)

                    if "_" not in display:
                        print("Congratulations! You guessed the word!\n\n The word was ", word, '.')
                        tried.append(choice)
                    else:
                        print("You ran out of lives! The word was ", word, ".")


                elif choice == '2':
                    print('HINT\n\n', Easy[2])
                    word = "MARS"
                    display = ["_"] * len(word)
                    lives = 5
                    guessed_letters = []
                    while "_" in display and lives > 0:
                        print("\n" + " ".join(display))
                        guess = input("Guess a letter: ").strip().capitalize()
                        check_letter(guess)

                        if guess in guessed_letters:
                            print("You already guessed that letter!")
                            continue

                        guessed_letters.append(guess)

                        if guess in word:

                            for i in range(len(word)):
                                if word[i] == guess:
                                    display[i] = guess
                        else:
                            lives -= 1
                            print("Wrong guess! Lives left: ", lives)

                    if "_" not in display:
                        print("Congratulations! You guessed the word!\nThe word was ",  word,".")
                        tried.append(choice)
                    else:
                        print("You ran out of lives! The word was ", word,'.')
                elif choice == '3':
                    print('HINT\n\n', Easy[3])
                    word = "MOON"
                    display = ["_"] * len(word)
                    lives = 5
                    guessed_letters = []

                    while "_" in display and lives > 0:
                        print("\n" + " ".join(display))
                        guess = input("Guess a letter: ").lower().capitalize()
                        check_letter(guess)

                        if guess in guessed_letters:
                            print("You already guessed that letter!")
                            continue

                        guessed_letters.append(guess)

                        if guess in word:

                            for i in range(len(word)):
                                if word[i] == guess:
                                    display[i] = guess
                        else:
                            lives -= 1
                            print("Wrong guess! Lives left: ", lives)

                    if "_" not in display:
                        print("Congratulations! You guessed the word!\n\nThe word is ", word,'.')
                        tried.append(choice)
                    else:
                        print("You ran out of lives! The word was ", word,'.')
                elif choice == '4':
                    print('HINT\n\n', Easy[4])
                    word = "GRAVITY"
                    display = ["_"] * len(word)
                    lives = 5
                    guessed_letters = []

                    while "_" in display and lives > 0:
                        print("\n" + " ".join(display))
                        guess = input("Guess a letter: ").capitalize().strip()
                        check_letter(guess)

                        if guess in guessed_letters:
                            print("You already guessed that letter!")
                            continue

                        guessed_letters.append(guess)

                        if guess in word:

                            for i in range(len(word)):
                                if word[i] == guess:
                                    display[i] = guess
                        else:
                            lives -= 1
                            print("Wrong guess! Lives left: ", lives)

                    if "_" not in display:
                        print("Congratulations! You guessed the word!\n\nThe word is ", word,'.')
                        tried.append(choice)
                    else:
                        print("You ran out of lives! The word was ", word,'.')
                elif choice == '5':
                    print('HINT\n\n', Easy[5])
                    word = "SOLAR ECLIPSE"
                    display =[]
                    lives = 5
                    guessed_letters = []

                    for letter in word:
                        if letter == " ":
                            display.append(" ")  # keep the space
                        else:
                            display.append("_")  # hide letters

                    while "_" in display and lives > 0:
                        print("\n" + " ".join(display))
                        guess = input("Guess a letter: ").capitalize().strip()
                        check_letter(guess)

                        if guess in guessed_letters:
                            print("You already guessed that letter!")
                            continue

                        guessed_letters.append(guess)

                        if guess in word:

                            for i in range(len(word)):

                                if word[i] == guess:
                                    display[i] = guess
                        else:
                            lives -= 1
                            print("Wrong guess! Lives left: ", lives)

                    if "_" not in display:
                        print("Congratulations! You guessed the word!\n\nThe word is ", word,'.')
                        tried.append(choice)
                    else:
                        print("You ran out of lives! The word was ", word,'.')
                elif choice == '6':
                    print('HINT\n\n', Easy[6])
                    word = "SUN"
                    display = ["_"] * len(word)
                    lives = 5
                    guessed_letters = []

                    while "_" in display and lives > 0:
                        print("\n" + " ".join(display))
                        guess = input("Guess a letter: ").capitalize().strip()
                        check_letter(guess)

                        if guess in guessed_letters:
                            print("You already guessed that letter!")
                            continue

                        guessed_letters.append(guess)

                        if guess in word:

                            for i in range(len(word)):
                                if word[i] == guess:
                                    display[i] = guess
                        else:
                            lives -= 1
                            print("Wrong guess! Lives left: ", lives)

                    if "_" not in display:
                        print("Congratulations! You guessed the word!\n\nThe word is ", word,'.')
                        tried.append(choice)
                    else:
                        print("You ran out of lives! The word was ", word,'.')
                elif choice == '7':
                    print('HINT\n\n', Easy[7])
                    word = "SATURN"
                    display = ["_"] * len(word)
                    lives = 5
                    guessed_letters = []

                    while "_" in display and lives > 0:
                        print("\n" + " ".join(display))
                        guess = input("Guess a letter: ").capitalize().strip()
                        check_letter(guess)

                        if guess in guessed_letters:
                            print("You already guessed that letter!")
                            continue

                        guessed_letters.append(guess)

                        if guess in word:

                            for i in range(len(word)):
                                if word[i] == guess:
                                    display[i] = guess
                        else:
                            lives -= 1
                            print("Wrong guess! Lives left: ", lives)

                    if "_" not in display:
                        print("Congratulations! You guessed the word!\n\nThe word is ", word,'.')
                        tried.append(choice)
                    else:
                        print("You ran out of lives! The word was ", word,'.')
                elif choice == '8':
                    print('HINT\n\n', Easy[8])
                    word = "STAR"
                    display = ["_"] * len(word)
                    lives = 5
                    guessed_letters = []

                    while "_" in display and lives > 0:
                        print("\n" + " ".join(display))
                        guess = input("Guess a letter: ").capitalize().strip()
                        check_letter(guess)

                        if guess in guessed_letters:
                            print("You already guessed that letter!")
                            continue

                        guessed_letters.append(guess)

                        if guess in word:

                            for i in range(len(word)):
                                if word[i] == guess:
                                    display[i] = guess
                        else:
                            lives -= 1
                            print("Wrong guess! Lives left: ", lives)

                    if "_" not in display:
                        print("Congratulations! You guessed the word!\n\nThe word is ", word,'.')
                        tried.append(choice)
                    else:
                        print("You ran out of lives! The word was ", word,'.')
                elif choice == '9':
                    print('HINT\n\n', Easy[9])
                    word = "ATMOSPHERE"
                    display = ["_"] * len(word)
                    lives = 5
                    guessed_letters = []

                    while "_" in display and lives > 0:
                        print("\n" + " ".join(display))
                        guess = input("Guess a letter: ").capitalize().strip()
                        check_letter(guess)

                        if guess in guessed_letters:
                            print("You already guessed that letter!")
                            continue

                        guessed_letters.append(guess)

                        if guess in word:

                            for i in range(len(word)):
                                if word[i] == guess:
                                    display[i] = guess
                        else:
                            lives -= 1
                            print("Wrong guess! Lives left: ", lives)

                    if "_" not in display:
                        print("Congratulations! You guessed the word!\n\nThe word is ", word,'.')
                        tried.append(choice)
                    else:
                        print("You ran out of lives! The word was ", word,'.')
                elif choice == '10':
                    print('HINT\n\n', Easy[10])
                    word = "NEIL ARMSTRONG"
                    display = []
                    lives = 5
                    guessed_letters = []
                    for letter in word:
                        if letter == " ":
                            display.append(" ")  # keep the space
                        else:
                            display.append("_")

                    while "_" in display and lives > 0:
                        print("\n" + " ".join(display))
                        guess = input("Guess a letter: ").capitalize().strip()
                        check_letter(guess)

                        if guess in guessed_letters:
                            print("You already guessed that letter!")
                            continue

                        guessed_letters.append(guess)

                        if guess in word:

                            for i in range(len(word)):
                                if word[i] == guess:
                                    display[i] = guess
                        else:
                            lives -= 1
                            print("Wrong guess! Lives left: ", lives)

                    if "_" not in display:
                        print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                        tried.append(choice)
                    else:
                        print("You ran out of lives! The word was ", word,'.')
                elif choice == '*':
                    print('Exit')
                    break
                else:
                    print("Incorrect input! Try again.\n Numbers between 1 and 10.")
            else:
                print('invalid input\nTry again')
                return None
            if tried == ls:
                print('Easy level completed!\n\nMoving on to the next level.')

                break


def medium_game():
    Medium = {1: 'The galaxy that contains our solar system',
              2: 'I am composed of ice and dust',
              3: 'I exist when the sun blocks the moon',
              4: 'The first artificial satellite sent into space',
              5: 'That piece of metal and rock that burns up the earth\'s atmosphere',
              6: 'A space rock that orbits the sun',
              7: 'The common name for creatures outside our planet',
              8: 'Famous for my astronomical history, every aspiring astronaut wants to work with me',
              9: 'In my solar system, I am known as the hottest planet',
              10: 'I am a planet outside your plant'

              }

    print("Welcome to the Medium level Game\nPress * to exit or continue playing")
    ls = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    tried = []
    while True:
        choice = input("Please enter a number between 1 and 10: ").strip()
        if choice in ls:
            if choice == '1':
                print('HINT:', Medium[1])
                word = "MILKY WAY"
                display = []
                lives = 5
                guessed_letters = []
                for letter in word:
                    if letter == " ":
                        display.append(" ")
                    else:
                        display.append("_")
                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue
                    guessed_letters.append(guess)
                    if guess in word:
                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word, '.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word, '.')

            elif choice == '2':
                print('HINT: ', Medium[2])
                word = "COMET"
                display = ["_"] * len(word)
                lives = 5
                guessed_letters = []

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')
            elif choice == '3':
                print('HINT: ', Medium[3])
                word = "LUNAR ECLIPSE"
                display = []
                lives = 5
                guessed_letters = []
                for letter in word:
                    if letter == " ":
                        display.append(" ")
                    else:
                        display.append("_")

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')
            elif choice == 4:
                print('HINT: ', Medium[4])
                word = "SPUTNIK 1"
                display = []
                lives = 5
                guessed_letters = []
                for letter in word:
                    if letter == " ":
                        display.append(" ")
                    else:
                        display.append("_")

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").strip().capitalize()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')
            elif choice == 5:
                print('HINT: ', Medium[5])
                word = "METEOR"
                display = ["_"] * len(word)
                lives = 5
                guessed_letters = []

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')
            elif choice == 6:
                print('HINT: ', Medium[6])
                word = "ASTEROID"
                display = ["_"] * len(word)
                lives = 5
                guessed_letters = []

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')
            elif choice == 7:
                print('HINT: ', Medium[7])
                word = "ALIEN"
                display = ["_"] * len(word)
                lives = 5
                guessed_letters = []

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')
            elif choice == 8:
                print('HINT: ', Medium[8])
                word = "NASA"
                display = ["_"] * len(word)
                lives = 5
                guessed_letters = []

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").strip().capitalize()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')
            elif choice == 9:
                print('HINT: ', Medium[9])
                word = "VENUS"
                display = ["_"] * len(word)
                lives = 5
                guessed_letters = []

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')
            elif choice == 10:
                print('HINT: ', Medium[10])
                word = "EXOPLANET"
                display = ["_"] * len(word)
                lives = 5
                guessed_letters = []

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')
            else:
                print('Invalid input! Try again. Pick numbers between 1 and 10.')
        elif choice == '*':
            print('Exit')
            break
        else:
            print('invalid input\nTry again')
            return None

        if tried == ls:
            print('Bravo! Medium level completed.\nMoving to the next round')
            break


def hard_game():
    Hard = {1: 'I am the largest moon in your solar system',
            2: 'The invisible substance thought to make up most of the universe\'s mass',
            3: 'I am the study of the universe\'s origin and structure',
            4: 'My death is always the birth or either something beautiful or something terrible',
            5: 'That boundary in black hole beyond which nothing can escape',
            6: 'The widely believed theory that the universe began',
            7: 'I am believed to be the cause of the universe\'s expansion',
            8: 'I house the largest volcano\'s mountain',
            9: 'Sadly but interestingly the leftover core of a massive star made almost entirely of neuron ',
            10: 'I make over 70% of the Earth\'s surface'

            }
    print("Welcome to the Hard level Game\nPress * to exit or continue playing")

    ls = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    tried = []
    while True:
        choice = input("Please enter a number between 1 and 10: ").strip()
        if choice in ls:
            if choice == '1':
                print('HINT: ', Hard[1])
                word = "GANYMEDE"
                display = ["_"] * len(word)
                lives = 5
                guessed_letters = []

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')

            elif choice == '2':
                print('HINT: ', Hard[2])
                word = "DARK MATTER"
                display = []
                lives = 5
                guessed_letters = []
                for letter in word:
                    if letter == " ":
                        display.append(" ")
                    else:
                        display.append("_")

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')


            elif choice == '3':
                print('HINT: ', Hard[3])
                word = "COSMOLOGY"
                display = ["_"] * len(word)
                lives = 5
                guessed_letters = []
                for letter in word:
                    if letter == " ":
                        display.append(" ")
                    else:
                        display.append("_")

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')

            elif choice == '4':
                print('HINT: ', Hard[4])
                word = "SUPERNOVA"
                display = ["_"] * len(word)
                lives = 5
                guessed_letters = []

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')

            elif choice == '5':
                print('HINT: ', Hard[5])
                word = "EVENT HORIZON"
                display = []
                lives = 5
                guessed_letters = []
                for letter in word:
                    if letter == " ":
                        display.append(" ")
                    else:
                        display.append("_")

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')

            elif choice == '6':
                print('HINT: ', Hard[6])
                word = "BIG BANG"
                display = []
                lives = 5
                guessed_letters = []
                for letter in word:
                    if letter == " ":
                        display.append(" ")
                    else:
                        display.append("_")

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:
                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')

            elif choice == '7':
                print('HINT: ', Hard[7])
                word = "DARK MATTER"
                display = []
                lives = 5
                guessed_letters = []
                for letter in word:
                    if letter == " ":
                        display.append(" ")
                    else:
                        display.append("_")

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')

            elif choice == '8':
                print('HINT: ', Hard[8])
                word = "MARS"
                display = ["_"] * len(word)
                lives = 5
                guessed_letters = []

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')

            elif choice == '9':
                print('HINT: ', Hard[9])
                word = "NEUTRON STAR"
                display = []
                lives = 5
                guessed_letters = []
                for letter in word:
                    if letter == " ":
                        display.append(" ")
                    else:
                        display.append("_")

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')

            elif choice == '10':
                print('HINT: ', Hard[10])
                word = "WATER"
                display = ["_"] * len(word)
                lives = 5
                guessed_letters = []

                while "_" in display and lives > 0:
                    print("\n" + " ".join(display))
                    guess = input("Guess a letter: ").capitalize().strip()
                    check_letter(guess)

                    if guess in guessed_letters:
                        print("You already guessed that letter!")
                        continue

                    guessed_letters.append(guess)

                    if guess in word:

                        for i in range(len(word)):
                            if word[i] == guess:
                                display[i] = guess
                    else:
                        lives -= 1
                        print("Wrong guess! Lives left: ", lives)

                if "_" not in display:
                    print("Congratulations! You guessed the word!\n\nThe word was ", word,'.')
                    tried.append(choice)
                else:
                    print("You ran out of lives! The word was ", word,'.')

            else:
                print('Invalid input! Please enter a number between 1 and 10.')
        elif choice == '*':
            print('Exit')
            break

        else:
            print('invalid input\nTry again')
            return None

        if tried == ls:
            print('All levels completed! Move to the next level')
            break
def future_game():
    print("New level coming soon")









def rule():
    print('How to play?')
    print('In each level, you have 10 rounds.'
    '\n For each round, you have 5 trials.'
    '\n If you guess all 10 words right, You\'ll be asked to go to the net level'
    '\n If you guess a word wrong, you lose one life\n\nIf you lose all 5 lives, you will need to restart'
    '\n Repeating an already guessed letter does not reduce your chances of trial'
    '\nFinally, when playing, be careful with your spellings. You might know the correct word, but if you misspell, you get the word wrong')
    choice=input("1. Continue reading\n\n 2.Exit How to play\n ")
    if choice=="1":
        rule()
    elif choice=="2":
        return
    else:
        print("Invalid input! Please enter 1 or 2.")

def main():
    name = input("WELCOME TO THE ASTRONOMY WORD GUESS GAME!\n\n\nPlease enter your preferred name: ").title().strip()
    print("Hello ", name, "Happy to see you today. Sit tight and enjoy the game")
    while True:
        option=input("Please select an option to proceed\n\n\n 1.Select easy level\n\n2.Select medium level\n\n3. select hard level\n\n4. How to play\n\n5.New level\n\n6.Exit\n").strip()
        if option=="1":
            easygame()
        elif option=="2":
            medium_game()
        elif option=="3":
            hard_game()
        elif option=="4":
            rule()
        elif option=="5":
            future_game()
        elif option=="6":
            while True:
                choice = input('Thanks for playing!\n\n Are you sure you want to exit? \n Yes or No?').lower().strip()
                if choice == "yes":
                    exit()
                elif choice == "no":
                    break
                else:
                    print("Invalid input! Please enter yes or no.")



        else:
            print("Invalid input! Please select a valid option.")
main()



