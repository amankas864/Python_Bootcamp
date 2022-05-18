# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name=name1+name2
countt,countl=0,0
for i in name:
    for j in "true":
        if i.lower()==j:
            countt+=1 
    for j in "love":
        if i.lower()==j:
            countl+=1
count=int('{}{}'.format(countt,countl))
if count<10 or count>90:
    print("Your score is {}, you go together like coke and mentos.".format(count))
elif count>=40 and count<=50:
    print("Your score is {}, you are alright together.".format(count))
else:
    print("Your score is {}.".format(count))