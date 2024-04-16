"""
Given a list of length M, you need to print and find sum of the elements of list 

Input Format :
Line 1 : An int M 
Line 2 : M int elements of list seperated by ';'
Output Format:
Addition 
Constraints :
1 <= M <= 10^6"""
#declared variable M to take input for the number to get sum upto
M = int(input())
#Declare the variable M_elements to get input of numbers to do sum of
M_elements = input()
#declared the sum variable to compute sum and declared it with 0
sum = 0
#created an empty string to remove ; from the given string
empty_string=" "
#created a new list to store input numbers
new_list = []
#apply for loop in order to iterate given elements
for i in M_elements:
    if(i==';'):
        new_list.append(empty_string)
        empty_string = " "
    else:
        empty_string = empty_string+i
if(empty_string!=';'):
    new_list.append(empty_string)
#another for loop ro convert each element into integer to compute sum 
for j in range(M):
    new_list[j] = int(new_list[j])
#This for loop is executed to compute sum of each elements in the list
for k in new_list:
    sum = sum+k
print(sum)