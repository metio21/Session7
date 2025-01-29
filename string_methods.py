s = "hello"
useful_methods = [m for m in dir(s) if "__" not in m]
print(useful_methods)

print(help(s.capitalize))
print(s.capitalize()) # this turns the first letter of s (hello) into a capital letter

print("HELLO".casefold()) # same as .lower() method

print("hello".center(50))
print("hello".center(50, "x"))

print("I see a little dove".count("e")) # how many time do i see 'e'
print("banananananana".count("ana"))
x = "I do not cook nor compare"
print(f"There are {x.count("o")}os inside |'{x}'|") # f lets us use curly brackets that replace the value it takes and prints it
print("helooooo000000ooollolo".find("l", 10)) # finds number of occurence after the first 10 characters (in this case)

s = "bob goes home to meet bob so they can take their bob and go bobing"
pos = 0
while True:
    start = s.find("bob", pos)
    if start == -1:
        break
    print("found bob on position", start)
    pos = start + 1

items = ["cat", "rat", "mouse", "house"]
print("+another".join(items))
print("I LIKE to go HIKING!!".lower().upper()) # capitalizes all elements
print("i like to go skiing".title()) # replace, replaces item with item inside the string
print("i like to go skiing".replace( "i", "1").replace("e", "3")) # replaces all i's with 1 and all e's with 3
print("I like to go skiing".split()) # make a list of the string split by the delimiter





