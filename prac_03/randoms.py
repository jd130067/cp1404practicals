import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

#line one:
    #min 5, max 20
    #saw 13,18,17

#line two:
    #min 3, max 9
    #saw 5, 5 ,7

#line three:
    #min 2.5, max 5.5 (depending on rounding)
    #saw 2.7306718917889103, 4.615404322552742, 4.065412834334289

#Code for random number between 0 and 100
print(f"Random Integer: {random.randint(0,100)}")
print(f"Random Float: {random.uniform(0,100): .2f}")