""" 

You have been given an ilist of size M that contains 1 and 2. Write a function to arrange them in order.
function name=arrange() 
#You are not allowed to use sort function in this program

Sample Input 1:
1
7
1 2 2 2 1 2 2

Sample Output 1:

1 1 2 2 2 2 2


Sample Input 2:
2
8
2 1 2 2 1 2 1 2
5
1 2 1 2 1

Sample Output 2:
1 1 1 2 2 2 2 2

1 1 1 2 2 

"""
""" 

You have been given an ilist of size M that contains 1 and 2. Write a function to arrange them in order.
function name=arrange() 
#You are not allowed to use sort function in this program

Sample Input 1:
1
7
1 2 2 2 1 2 2

Sample Output 1:

1 1 2 2 2 2 2


Sample Input 2:
2
8
2 1 2 2 1 2 1 2
5
1 2 1 2 1

Sample Output 2:
1 1 1 2 2 2 2 2

1 1 1 2 2 

"""
def str_to_int(elements):
    emptlist=[]
    emp_str =""
    for i in elements:
        if(i==' '):
            emptlist.append(emp_str)
            emp_str = ' '
        else:
            emp_str = emp_str + i
    if(emp_str!=' '):
        emptlist.append(emp_str)
    for j in range(0,len(emptlist)):
        emptlist[j] = int(emptlist[j])
    return emptlist
    
def arrange(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if(a[j]<=a[i]):
                a[j],a[i] = a[i],a[j]
    return a  

Number_of_list = int(input())
if(Number_of_list == 1):
    size_of_list = int(input())
    elements = input()
    a = str_to_int(elements)
    b = arrange(a)
    for k in range(len(b)-1):
        print(b[k],end=" ")
    print(b[len(b)-1])
if(Number_of_list == 2):
    size_of_list = int(input())
    elements = input()
    a = str_to_int(elements)
    b = arrange(a)
    for k in range(len(b)-1):
        print(b[k],end=" ")
    print(b[len(b)-1])
    size_of_2ndlist = int(input())
    elements2 = input()
    a = str_to_int(elements2)
    b = arrange(a)
    for k in range(len(b)-1):
        print(b[k],end=" ")
    print(b[len(b)-1])

    