x = 15
if x < 10:
    print("Smaller")
if x > 10:
    print("Greater")
print("Finish")
#comparison operators 
x = 20
if x == 20:
    print("Equals 5")
if x > 18:
    print("Greater than 18")
if x < 21:
    print("Less than 21")
if x <= 20:
    print("Less than and Equals to 20")
if x >+ 20:
    print("Greater than and Equals to 20")
if x != 21:
    print("Not Equals 21")
print("Finish")
#one-way decisions
x = 5
print("Before 5")
if x == 5:
    print("Is 5")
    print("Is still 5")
    print("Third 5")
print("Afterwards 5")
print("Before 6")
if x == 6:
    print("Is 6")
    print("Is still 6")
    print("Third 6")
print("Afterwards 6")
print("Before 7")
if x == 7:
    print("Is 7")
    print("Is still 7")
    print("Third 7")
print("Finish")
#nested 
x = 25
print(x)
if x != 25:
    print("Error!")
    if x == 25:
        print("Correct!")
print("All done!")
#multi-way
x = 12
if x < 3:
    print("Small")
elif x < 6:
    print("Medium")
elif x == 6:
    print("Mid")
elif x > 6:
    print("Big")
elif x > 9:
    print("Large")
else:
    print("None")
print("Send it!")
