#Use for loop through the list fomr 1 to 21

for i in range(1,21):

#Use modulus to check that result is NOT EQUAL to 0
    if((i%2) != 0):
#Print the odds
        print("i = ", i)

#float point numbers

your_flat = input("Enter a float number: ")

your_flat = float(your_flat)
print("Round 2 decimals : {:.2f}".format(your_flat))


#Have the user enter their investment ampunt and expected interest
#Each year their investment will increase by their investment + their investment * interest
#rate is

#print out the earnigs after a 10 year period

#Ask for the money invested + the interest rate
money = input("How much to invest : ")
interest_rate = input("Interest Rate :")


#convert the value to a float
money = float(money)


#Convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01

#Cycle through 10 years using a for loop and range from 0 to 9
for i in range(10):
    money = money + (money * interest_rate)


#Output the results
print("Investment after 10 years : {:.2f}".format(money))
print(float(100) * .01)