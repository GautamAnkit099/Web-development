list = [1,2,3,4,5]
print(list)
list.append(6)
print(list)
list.remove(6)
print(list)
l =list.copy()
print(list)
print(len(list))
print(list.count(1))
print(list.count(2))
list.append(6)

print(list)
list.append(6)
print(list)
print(list.count(6))

print(list.index(1))
list.insert(7,7)
print(list)
list.insert(-1,8)
print(list)
list2 = ["cat","dog","fox"]
list.extend(list2)
print(list)

list.pop()
print(list)
list.pop(2)
print(list)
'''
list3 = []
list3.remove(9)
print(list3)
'''
'''
list3 = []
list3.pop()
print(list3)
'''

list.reverse()
print(list)


list4 = [10,20,30,40,50]

list4.sort(reverse=True)
print(list4)

list5 = list4
list5[4] = 60
print(list4)


print(2**5)
print(2*6)
str = ":python"
print(str*2)

print(list*2)
print(5%2)
print(5/2)
print(5//2)


num = 10
print("number is %d"%num)

list.clear()
print(list)


list6 = [[4,5,6],[1,2,3]]
for i in list6:
    print(i)

for j in range(len(list6)):
        for k in range(len(list6[j])):
            print(list6[j][k],"\t",end='')
        print()
        
