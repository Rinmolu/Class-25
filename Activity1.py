list1 = [5,9,12,6]
list2 = [4,8,11,5]
result = map(lambda x,y:x+y,list1,list2)
print(list(result))
numbers = [1,3,7,10]
def square(n):
    return n*n
square = list(map(square,numbers))
print(square)