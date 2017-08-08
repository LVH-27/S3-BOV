import random
random.seed()

print('{')
for i in range(100):
	print('"' + str(i) + '" :')
	print('\t{')
	print('\t"temperature":', random.randint(15, 40), ',')
	print('\t"pressure":', random.randint(15, 40))
	print('\t},')
	print()
print('}')
