def isPrime(n):
    if n <= 1 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
t=int(input('Enter Number of test cases: '))
for x in range(t):
    while(1):
        m,n = map(int,input().split())
        if m<1 or n>1000000000 or m>n or n-m>100000:
            print('Incorrect value for m and/or n, Enter Again!')
            continue
        else:
            break
    a=list(range(m,n+1))
    for i in range(m,n+1):
        if isPrime(i):
            continue
        else:
            a.remove(i)
    print('The Output: ')
    print(m,n)
    print(a)
