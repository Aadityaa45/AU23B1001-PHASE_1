"""   Turn Around Function 

Design a Function that should take list as an argument and perform turnaround() it in following fasion.

Input Format:

1. Take M, Inputs for Turnaround
2. Enter M numbers on new line 

10
10
20
30
40
50
60
70
80
90

Output Format:
50
60
70
80
90
100
30
40
10
20

"""
#defined a function turnaround 
def turnaround(emp):
    j=0 #declared the variables i and j for loops
    i=0
    while(i<len(emp)): #here while loop is applied to repeat the block of code untile the i is less than length of list i.e. emp
        if emp.index(emp[i]) >= 4: #as in the given pattern after the index no. 4 the number got printed first 
            print(emp[i],end="")
        i = i +1
        print()
    for j in range(0,len(emp)): #again loop is used to print the lower portion of the pattern
        if j == 0: #for the 0 index the swapping is done according to patterns
            emp[0], emp[2] = emp[2], emp[0]
        elif j == 1:  #for the index position 1 
            emp[1], emp[3] = emp[3], emp[1]
            #As we already printed the elements for 4 and greater than 4 so, if the loop reaches to to this condition and will break the loop
        elif emp.index(emp[j]) == 4:  
            break
        print(emp[j], end="")
        j = j+1
        print()
m = int(input()) #here the input of length is taken
emp =[]
for i in range(m):
    x = int(input())
    emp.append(x)
a = emp
turnaround(a)
