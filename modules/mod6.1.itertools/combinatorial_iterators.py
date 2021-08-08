from itertools import product, permutations, combinations, \
    combinations_with_replacement

it_prod = product(["a","b","c"],[1,2,3])
print([x for x in it_prod])

print("="*30)
it_perm = permutations([1,2,3],3)
for perm in it_perm:
    print(perm)

print("="*30)
it_comb = combinations([1,2,3,4],2)
for comb in it_comb:
    print(comb)

print("="*30)
it_comb = combinations_with_replacement([1,2,3,4],2)
for comb in it_comb:
    print(comb)
