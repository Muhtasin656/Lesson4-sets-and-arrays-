import array as arr
array_num=arr.array("i",[1,2,3,1,2,3,2,3,4,6,4,2])
print(str(array_num))

# count number of occurances
print(array_num.count(3)) 

# reverse the array
array_num.reverse()
print(str(array_num))