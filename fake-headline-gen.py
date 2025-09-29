# 1- import random module
import random

# 2- create subject
subjects =[
    "Shahrukh khan",
    "Virat kohli",
    "Nirmala Sitharam",
    "A mumbai cat",
    "Group of monkey",
    "Prime minister",
    "Auto Riksha driver from dehli"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
]

place_or_things =[
    "at red fort",
    "mumbai local train",
    "a plate of samosa",
    "inside parliment",
    "at ghanga ghat",
    "suring IPL match",
    "india gate",
]


# 3- start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)

    headline = f"Breaking News: {subject} {action} {place_or_thing} "
    print("\n" + headline)

    user_input = input("\nDo you want to regenerate healine?(yes/no)").strip().lower()
    if user_input != "yes":
        print('Program terminate ...')
        break

print("\nThanks for using Fake Headline Generator. Have a fun day")
