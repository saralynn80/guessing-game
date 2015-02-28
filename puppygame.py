def myPuppy():
    guessesTaken = 0

    yourName = raw_input("What is your name?")

    favDog = "corgi"
    print "Hi " + yourName + "! I love puppies. You have 5 chances to guess what my favorite kind of puppy is!"

    while guessesTaken < 5:
        yourGuess = raw_input("Take a guess!")
        guessesTaken = guessesTaken + 1

        if yourGuess == favDog:
            print "You got it!"
        elif yourGuess != favDog:
            print "Nope...try again."
        else
            break

        if yourGuess == favDog:
            guessesTaken = str(guessesTaken)
            print "Nice job " + yourName + "! Corgis are my favorite! And it only took you " + guessesTaken + " guesses!"
        elif yourGuess != favDog:
            print "Sorry, you didn't get it. My favorite kind of dog is a corgi!"


myPuppy()
