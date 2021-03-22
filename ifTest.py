import random



for i in range(0, 10):
    x = random.randint(0, 100)
    y = random.randint(0, 100)

    answer = int(input("{} + {} = ".format(x, y)))

    flag = (answer == (x + y))
    print(flag)

# a = 'a'
# print(f'a is {a}')

# x,y,z = 1,2,3

# print(f'a is {x},{y},{z}')
# print(f'a is {z},{y},{x}')

# name = 'Jun'
# family = 'Sakai'
# print(f' my name is {name} {family}')

# print("i love {} for {}".format('Geeks','Geeks'))
# print("{0} and {1}".format('Geeks','portal'))
# print("{1} and {0}".format('Geeks','Portal'))
