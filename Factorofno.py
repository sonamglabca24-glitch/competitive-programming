#print all factors /divisors of a given positive number.
n=int(input("Enter a positive number: "))
while n<1:
    i=1
for i in range(1, n+1):
   if n % i == 0:
       print(i)

