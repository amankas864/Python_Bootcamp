# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
c=0
l=0
for i in student_heights:
    c+=i
    l+=1
print("Average height of the students is ",round(c/l))

