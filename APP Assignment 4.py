memo={} #creates a dictionary to store previously calculated fibonacci series, key is n and value is its summed series
def fib(n):
    if n<=1:
        return n #stops recursion when n is less than one
    if n in memo:
        return memo[n] #if series already present in dictionary, prints that (memoization)
    memo[n]=fib(n-1)+fib(n-2) #uses fibonacci series of smaller numbers to calculate series of larger number (recursion)
    return memo[n]

while True: #keeps running loop forever
    num=int(input("Enter Number: "))
    print("Fibonacci Series of",num,":",fib(num))
