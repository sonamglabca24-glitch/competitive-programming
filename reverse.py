#Read N ,Print reverse of N.
n = int(input("Enter a number: "))
r= 0
while n > 0:    
    digit=n % 10 
    n = n // 10
    r = r * 10 + digit
print("Reverse of number:", r)