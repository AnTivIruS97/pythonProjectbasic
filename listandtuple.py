#list number
list_num = [1,2,3,4,5,6,7,8,9,10]
print(list_num)
print(list_num[0:5])
print(list_num[0::3])

#mixed list
list_mixed = [1,2,3,4,'hello']
print(list_mixed)

#indexing and slicing
print(list_mixed[4])
print(list_num + list_mixed)      #concatenation on list
list1 = ['A','b','c','D']            #mutable list
list1 [0] = 'a'
print(list1)
print(list1)
print(list1.pop())           #popping out element
list1.append('e')            #appending element to list
print(list1)
list2 = [3,6,1,3,8,9,5]
list2.sort()
print(list2)                 #sorting the list2 elements

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict1 = {'name' :'Antima','age':23, 'designation' : 'software tester'}
print(my_dict1)

tuple1 = (1,2,3,4)
print(tuple1)               #tuples printing
print(tuple1[0:])               #indexing and slicing
print(tuple1[0:2])
tuple2 = (1,1,3,5,3,3,3,7)
print(tuple2.count(3))             #using count to see the number of rpeating the elements
print(type(tuple2))
list5 = [1,2,3,4]
list5 [0] = 5
print(list5)

set1 = {'hello','how','how','how'}
set1.add(1)
print(set1)
print(set(list5))
set1.add(5)
print(set1)

a = 1
b = 2
print(a>b)          #boolean check
c = 'hello'
d = 'world'
print(c!=d)
print(c==d)

if(a>b):
    print("the condition is true")
else:
    print("it is false")

name = 'ram'
if name =='ram':
    print("login as ram")
elif name == 'sam':
    print("login as sam")
else:
    print("check user")