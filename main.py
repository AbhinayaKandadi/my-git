import random

def getDigits(secretcode):
    return [int(i) for i in str(secretcode)]

def noDuplicates(secretcode):
    secretcode_li = getDigits(secretcode)
    if len(secretcode_li) == len(set(secretcode_li)):
        return True
    else:
        return False

def generateNum():
    while True:
        secretcode = random.randint(1000, 9999)
        if noDuplicates(secretcode):
            return secretcode

def numOfBullsCows(secretcode, guess):
    bull_cow = [0, 0]
    secretcode_li = getDigits(secretcode)
    guess_li = getDigits(guess)

    for i, j in zip(secretcode_li, guess_li):

        if j in secretcode_li:

            if j == i:
                bull_cow[0] += 1

            else:
                bull_cow[1] += 1

    return bull_cow

secretcode = generateNum()
tries = int(input('Enter number of tries: '))

while tries > 0:
    guess = int(input("Enter your guess: "))

    if not noDuplicates(guess):
        print("Number should not have repeated digits. Try again.")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only. Try again.")
        continue

    bull_cow = numOfBullsCows(secretcode, guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -= 1

    if bull_cow[0] == 4:
        print("You guessed right!")
        break
else:
    print(f"You ran out of tries!!! Number was {secretcode}")