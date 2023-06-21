requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies")
print('--------------------------------------')

age = 18
print(age == 18)
print('--------------------------------------')

answer = 17
if answer != 42:
	print("wrong")
print('--------------------------------------')

requested_topping = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_topping)
# in is a judgement key word
print('--------------------------------------')

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a reponse if you wish")
print('--------------------------------------')

car = 'subaru'
print("is car == 'subaru'? i predict True.")
print(car == 'subaru')

print("\nis car == 'audi'? i predict False.")
print(car == 'audi')
print('--------------------------------------')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	print(f"adding {requested_topping}.")

print("\nfinished making your pizza!")
print('--------------------------------------')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("sorry, we are out of green peppers right now.")
	else:
		print(f"adding {requested_topping}.")

print("\n finished making your pizza!")
print('--------------------------------------')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'peperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"adding {requested_topping}.")
	else:
		print(f"sorry, we don't have {requested_topping}.")

print("\nfinished making your pizza!")
