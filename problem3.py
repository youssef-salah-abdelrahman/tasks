import random
words = [ "python","programmer","devoloper","challange"]
word = random.choice(words)
unword = "".join(random.sample(word,len(word)))
attempts = 5
print ("welcome in the game")
print (f"try guss the original word: {unword}")
print (f"you have {attempts} attempts")

while attempts > 0:
    guess = input("enter your guess :").strip().lower()

    if guess == word:
        print ("congratulation")
        break
    else:
        attempts-=1
        if attempts > 0:
            print (f"try again you have {attempts} attempts left")
        else:
            print (f"game over the original word {word}" )