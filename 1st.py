#Asks user for their name & remove whitespace and capitalize
name = input("What's your name? ").strip().title()

#Split user's name
first, last = name.split(" ")
#Say hello to user
print(f"Hey, {name}")
    