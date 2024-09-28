import time


def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1)+fib(n-2)


def dynamic_fib(n):
    A = [i for i in range(n+1)]
    A[0], A[1] = 1, 1
    if n < 2:
        return A[n]
    for i in range(2, n+1):
        A[i] = A[i-1]+A[i-2]
    return A[n]


# start = time.time()
# print("result:", fib(40))
# end = time.time()
# print(f"{end-start} sec")

start = time.time()
print("result:", dynamic_fib(40))
end = time.time()
print(f"{end-start} sec")
