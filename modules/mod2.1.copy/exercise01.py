from copy import copy, deepcopy

ml = [[1,2,3],[4,5,6],[7,8,9]]

ml2 = ml
ml2[0][0]=10
print(ml)

ml = [[1,2,3],[4,5,6],[7,8,9]]
ml2 = copy(ml)
ml2[0]=[0]
print(ml, ml2)

ml = [[1,2,3],[4,5,6],[7,8,9]]
ml2 = copy(ml)
ml2[0][0]=0
print(ml, ml2)

ml = [[1,2,3],[4,5,6],[7,8,9]]
ml2 = deepcopy(ml)
ml2[0][0]=0
print(ml, ml2)