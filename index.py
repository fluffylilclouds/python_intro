name="tina" # this is a string variable
print(name)

x = 5
y = 99
print(x+y)

isloggedin=False
if isloggedin:
    welcome_message="welcome"
    print(welcome_message+" "+name+"!")

else:
    print("please log in")

if name=="tina":
    print("welcome tina")
elif name=="tommy":
    print("welcome tommy")
else:
    print("welcome aliens")


if x<=5:
    print("abc")
elif 5<x:
    print("xyz")


if y>99 and name=="tina": # and (2 conditions are true)
    print("i will not print")


if y>99 or  name=="tina": # or (1 condition is true)
    print("i will print")


if y<100: # first condition must be true to come into the next block 'name check'
    if name=="tina":
        print("I will also print")
    else:
        print("...")
else:
    print("I will not print")


