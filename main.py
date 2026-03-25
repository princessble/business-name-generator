print("Welcome to the Business Name Generator!\n")

print("Enter the city you grew up in:")
city = input().strip().title()

print("Enter the name of your pet:")
pet = input().strip().title()

name1 = city + " " + pet
name2 = pet + " " + city
name3 = city + pet

print("\nYour business name ideas are:")
print("1.", name1)
print("2.", name2)
print("3.", name3)