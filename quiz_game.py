print("Welcome to Iman's quiz!")

playing = input("Are you up for the challenge? ")

if playing.upper() !="YES":
    quit()

print("Okay! Let's see if you really know Iman ;p ")
score = 0

answer = input("1. What is Iman's CURRENT favorite book series? ")
if answer.upper() == "THRONE OF GLASS":
    print("Spot on! 10 points to Gryffindor!! ")
    score += 1
else:
    print("Uh oh :( Are you really Iman's friend? ")

answer = input("2. What is Iman's favorite actress? ")
if answer.upper() == "DILRABA DILMURAT":
    print("Bingo! You know the LOML ;p ")
    score += 1
else:
    print("Hmph! Its on her phone wallpaper to her laptop, did you not pay attention? ")

answer = input("3. What is Iman's favorite singer? ")
if answer.upper() == "TAEYEON":
    print("You Rock! Just the singer Iman's been in love with since 2013?! ")
    score += 1
else:
    print("Ugh, it's obvious you're new here ")

answer = input("4. What is Iman's favorite cuisine to cook? ")
if answer.upper() == "KOREAN":
    print("Yahoo! Betcha got a taste from these hands! ")
    score += 1
else:
    print("Hmm I guess you're not important enough for Iman to cook for you :( ")

answer = input("5. What is Iman's hobby? (hint there are two things!) ")
if answer.upper() == "READING AND WATCHING MOVIES":
    print("Well you just became a certified friend of Iman! ")
    score += 1
else:
    print("Fact check our relationship please ")

print("You got " + str(score) + " questions correct! ")
print("You got " + str((score / 5) * 100) + "% ")
