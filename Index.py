#Create an empty my_list
my_list = []
#Append 4 elements to my_list
for i in range(10):

    my_list.append(10*i)
#Print the my_list
    print(my_list)
#Print the length of my_list
    print(len(my_list))
#Print the first element of my_list
    print(my_list[i])
#Print the last element of my_list
    print(my_list[i-1])
#Print the first 4 elements of my_list
    print(my_list[10:30])
#Print the last 4 elements of my_list
    print (my_list[30:40])
#Extend my_list with 3 elements
    my_list.extend(10*i for i in range(10))
#Print extended my_list
    print(my_list)
#Insert 15 at index 2 of my_list
    my_list.insert (2, 15)
#Sort my_list in asceding order
    my_list.sort()
#Print the sorted my_list
    print(my_list)
#Print index of 30 in my list
    print(my_list.index(30))



    
