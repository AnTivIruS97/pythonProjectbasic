list_num = [1,2,3,4,5]
for item in list_num:
    print(item)

#printing given number of times
for _ in list_num:
    print('hello')

#even odd check
for item in list_num:
    if item % 2 == 0 :
        print(f'{item} is even')
    else:
        print(f'{item} is odd')

#tuple unpacking
tuple_num = (1,2,3,4)
for item in tuple_num:
    print(item)

list_tuple = [(1,2), (3,4), (5,6)]
for item in list_tuple:
    print(item)

#continue pass
list = [1,2,3,4,5,6,7]
for num in list:
    if num == 4:
        continue
    print(num)

#while loop
n = 0
while(n<5):
    print(n)
    n = n+1

string_msg = 'hello'
for a,b in enumerate(string_msg):
    print(a)
    print(b)
