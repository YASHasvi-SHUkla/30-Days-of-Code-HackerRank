# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
for j in range(n):
    
    s = input()
    even = ''
    odd = ''
    for i in range(len(s)):
        
        if i %2 ==0:
            even = even + s[i]
        else:
            odd = odd + s[i]
            
    print(even,odd)
        
