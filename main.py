from random_word import RandomWords
import random


def password_generator(k):
    # generates a password from random k words with simple algorithm
    output = ""
    i = 0
    r = RandomWords()

    while True:
        random_word = r.get_random_word()
        temp_word = str(random_word).capitalize()

        m = random.randint(0, 2)

        if m == 1:
            temp_word += str(random.randint(0, 9))

        output += temp_word
        i += 1

        if i == k:
            break

        output += "-"

    return output


def main():
    # main function
    k = int(input(
        "How many words should the password contain? Enter an int value greater than zero: "))
    print(f"Here is your password: {password_generator(k)}")

    return


main()