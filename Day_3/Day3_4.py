# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
add=0
if extra_cheese=='Y':
    add+=1
    if add_pepperoni=='Y'and size=='S':
        add+=17
    elif add_pepperoni=='Y':
        if size=='M':
            add+=23
        else:
            add+=28
    else:
        if size=='S':
            add+=15
        elif size=='M':
            add+=20
        else:
            add+=25
else:
    if add_pepperoni=='Y'and size=='S':
        add+=17
    elif add_pepperoni=='Y':
        if size=='M':
            add+=23
        else:
            add+=28
    else:
        if size=='S':
            add+=15
        elif size=='M':
            add+=20
        else:
            add+=25
print('Your final bill is: ${}.'.format(add))