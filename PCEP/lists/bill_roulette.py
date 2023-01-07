# Import the random module here
import random
#Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
# Angela, Ben, Jenny, Michael, Chloe
#Write your code below this line 👇
no_of_persons=(len(names)-1)
payee = random.randint(0,no_of_persons)
print(f"{names[payee]} is going to buy the meal today!" )


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[0][-1])
print(dirty_dozen[1][-1])