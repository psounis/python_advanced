from random import choice, choices

my_list = list(range(5))

print(f"Random choice: {choice(my_list)}")
print(f"3 Random choices: {choices(my_list, k=3)}")
print(f"5 Weighted choices: {choices(my_list, [1,100,10,1,1], k=10)}")
print(f"5 Cum.W. choices: {choices(my_list, cum_weights=[1,101,111,112,113], k=10)}")