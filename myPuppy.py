def myPuppy():
    guessesTaken = 0

    yourName = raw_input("What is your name?")

    favDog = "corgi"
    print "Hi " + yourName + "! I love puppies. You have 5 chances to guess what my favorite kind of puppy is!"

    while guessesTaken < 5:
        yourGuess = raw_input("Take a guess!")
        guessesTaken = guessesTaken + 1
        total = 5
        guessesLeft = str(total - guessesTaken)

        if yourGuess == favDog:
            guessesTaken = str(guessesTaken)
            print "You got it! Nice job " + yourName + "! Corgis are my favorite! And it only took you " + guessesTaken + " guesses!"
            break
        elif yourGuess != favDog:
            print "Nope...try again. You have " + guessesLeft + " guesses left."
        else:
            break #Ensures while loop won't keep running even if they guess correctly.

        while guessesTaken == 5:
            if yourGuess == favDog:
                print "Nice job " + yourName + "! You got it on your last guess."
            elif yourGuess != favDog:
                print "Sorry, you didn't get it. My favorite kind of dog is a corgi!"
                break

myPuppy()