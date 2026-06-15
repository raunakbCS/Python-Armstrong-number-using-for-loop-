# Program to print all the armstrong number from 1-500.
'''
for r in range(1,501):
    num = r
    s = 0
    length = len(str(r))
    while(num != 0):
        dig = num % 10
        s = s + dig ** length
        num = num // 10
    if(r == s):
        print(r)
'''
#Program to print all the armstrong number by taking the user input.

s = int(input("Ente the starting of the range = "))
e = int(input("Ente the ending of the range = "))

for r in range(s,e+1):
    num = r
    s = 0
    length = len(str(r))
    while(num != 0):
        dig = num % 10
        s = s + dig ** length
        num = num // 10
    if(r == s):
        print(r)
