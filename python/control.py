#if statement
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

#for loop
Words = ['cat', 'window', 'defenestrate']
for w in Words:
    print(w, len(w))
#range function
for i in range(5):
    print(i)
print(list(range(5, 10)))
#break and continue
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
        else:
            print(f"{n} is a prime number")

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")
#pass statement
for i in range(10):
    pass
#match statement
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
http_error(404)

