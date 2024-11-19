# Returns  alist of lists where each sublist is a group of three values
# INPUT: list of integers
# OUTPUT: list of lists of values, each nested list having a length of 3
def groups_of_3(arr : list[int]) -> list[list[int]]:
    grouped_list = []
    temp_list = []
    for i in range(len(arr)):
        if len(temp_list) == 3:
            grouped_list.append(temp_list)
            temp_list = []
        temp_list.append(arr[i])
    grouped_list.append(temp_list)
    return grouped_list

arr = [1,2,3,2,2,3,3,2,3,5,2]
x =groups_of_3(arr)
print(x)
