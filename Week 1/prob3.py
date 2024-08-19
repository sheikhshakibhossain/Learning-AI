n=input("Enter the value of n:")
print(f"You entered the value {n}")
n=int(n)

def fibonacchi(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fibonacchi(n-1)+fibonacchi(n-2)

result=fibonacchi(n)
print(f'The {n}th term of the series is {result}')


print(f'The 11th term of the series is {fibonacchi(11)}')


