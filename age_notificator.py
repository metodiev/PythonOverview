#We'll provide different output based on age
# 1 - 18 -> Important
# all others -> Not Important

#Recive age and store in age
age = eval(input("Enter age: "))

#and if both are true it returns true
#or: if either condition is true then true
#not : convert a true condition into a false

if (age >= 1) and (age <=18):
    print("Important Birthday")


#if age is both greater than or equal to 1 and less then or equal to 18 Important
elif (age == 21) or (age ==50):
    print("Important Birthday")
#if age is either 21 or 51 Important

# we check if age is less than 65 then convert true to false and vice versa
elif  not (age < 65):
    print("Important Birthday 1")

#Else not important
else:
    print("Sorry Not Important")