name="Tolu Amos,"
age= 21
height= float(5.5)
print(" My name is",name, "I am ", age, "years old," " and I am ", height, "feets tall" )

num1=50
num2=30
print("The subtraction of both num1 and 2 is:", num1-num2)
print("The addition of both num1 and 2 is:",num1+num2)
print("The multiplication of both num1 and 2 is:",num1*num2)
print("The division of both num1 and 2 is:",num1/num2)

val= 10
if val%2==0:
    print("The number is even")
else:
    print("The number is odd")
grade={70-100:'A', 60-69:"B", 50-59:"C", 45-49:"D",0-44:"E" }
print("The grade for scores 70-100 is: ", grade[70-100])
fav_food=["Rice", "Chicken", "Yam", "Noodles", "French fries"]
print("The favourite food is:", fav_food)
fav_food.append('Chicken')
print("The updated(added) favourite food is:", fav_food)
fav_food.remove('Yam')
print("The updated(remove) favourite food is:", fav_food)

summer=0
for i in range(51):
    summer += i
print(summer)

