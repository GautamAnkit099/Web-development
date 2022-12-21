def linear_Search(List, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0,len(List)):  
        if (list1[i] == key):  
            return i  
    return 1  
  
List = [1 ,3, 5, 4, 7, 9]
key = 4
res = linear_Search(List, 5,key)  
if(res == 1):  
    print("Element not found")  
else:  
    print(key,"Element found at index: ", res)
    
