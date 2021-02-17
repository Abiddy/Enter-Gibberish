strr = input(
    "Find the passcode, enter gibberish: ")

matched = 0
p = "fitbit"

for x in strr:
    for y in p:
        if (x == y):
            matched += 1


if matched > 0:
    print("Your gibberish contains " +
          str(matched) + " letters from the passcode")
else:
    print("Your gibberish does not contain anything from the passcode")


answer = input("Try to guess the passcode now!")

if (answer == p):
    print("You got the passcode: ")
elif(answer != p):
    print("try again")
