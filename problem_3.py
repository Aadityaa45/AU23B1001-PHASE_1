"""
Problem 3: Reflection or Pratibimb 

Design and Develop a User Defined function named (reflection) pass the input literal 'Welcome to EN2004' and return Output Format Mentioned Below

Input Format:

1. Take M str input from the User 
2. Get M , seperated str literals from a user (Test string to pass: 'Welcome to EN2004')

Output Format:

EN2004
to
Welcome



"""
#defined the function named reflection
def reflection(user_string):
    empty_str = " " #declared the empty string 
    new_list = [] #created an empty list
    for i in user_string: #applied for loop to iterate user string input
        if(i==','):  #checking the if condition for ,
            new_list.append(empty_str.strip())  #appended the value of empty-str to new_list
            empty_str = " " #here again the empty_str become empty so it doesnot return any previous holded value
        else:
            empty_str = empty_str+i
    if(empty_str!=''):
        new_list.append(empty_str.strip()) #strip function is used to deal with leading and trailing character
    x = new_list[::-1]  #the reversed list is stored in x variable
    for k in x:
        print(k)
M = input()
a = input()
reflection(a)