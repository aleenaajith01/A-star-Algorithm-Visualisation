array = (1,4,5,6,3,2)

i=0
temp =0
for i in range len(array):
    if (array[i]<=array[i+1]):
        continue
    temp = array[i]
    array[i] = array[i+1]
    array[i+1] = temp
print(array)