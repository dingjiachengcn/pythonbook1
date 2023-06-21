cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

print('--------------------------------------')

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
#sort is permenant sort, the list will be changed
print('--------------------------------------')


cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)
#sorted is temporarly
print('--------------------------------------')

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

print('--------------------------------------')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))


print('--------------------------------------')
cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
