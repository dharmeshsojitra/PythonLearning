import copy

og_list = [1,2,3]

dup_list = copy.copy(og_list)

dup_list[1] = 5

print(og_list)
print(dup_list)

print('****** deep copy output*******')

another_list = copy.deepcopy(og_list)
another_list[1] = 6

print(og_list)
print(another_list)