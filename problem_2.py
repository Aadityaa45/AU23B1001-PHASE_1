""" 

Problem: Knock Knock are you there?

Input Format:

1. Take M int input from the User 
2. Get M , seperated values from a user 
3. Enter a number 'N' you are looking for

Output Format:

1. Print index on console once Found or Print 'Better Luck Next Time' to the console


"""
#Declared a variable M to take input of number for the size of list
M = int(input())
#declared the variable get_M and take the input sepearted with , 
get_M = input()
#created an empty list
list1 = []
#created an empty string
empty_str =""
#applied for loop to iterate the input numbers
for i in get_M:
    if i==',' or i==';':
        list1.append(empty_str) #appended the value of empty string into list 1
        empty_str = " " #here we make the empty_str empty becuase it should not return the previous stored value
    else:
        empty_str = empty_str+i
if empty_str!=',':
    list1.append(empty_str)
for k in range(0,len(list1)):
    list1[k] = int(list1[k])
n = int(input()) #Here the input is taken for what the user is looking for
count = 0
for j in list1:
    if(n==j):
        count = count+1 #count is declared to find the index of duplicate elements
if(count==1):
    print(list1.index(n)) #printed the index on console
elif(count==2):
    print(list1.index(n,list1.index(n)+1,len(list1)+1))
else:
    print("Better Luck Next Time")
    