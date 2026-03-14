import timeit

def fibRecursive(N):

    if N == 1 or N == 2:
        return 1
    else:
        return fibRecursive(N-1) + fibRecursive(N-2)

def fibIterative(N):

    f1 = 1
    f2 = 1
    for i in range(1,N-1):
        nextValue = f1 + f2
        f1 = f2
        f2 = nextValue

    return f2

def main():
    num = int(input("Calculate the Fibonacci Number for N = "))

    print("\nRecursive:")
    start = timeit.default_timer()
    fNumber = fibRecursive(num)
    end = timeit.default_timer()
    elapsedNS = round((end - start)*10**9)
    print("Fibonacci(",num,") = ", fNumber)
    print("Solution took",elapsedNS,"nanoseconds\n")

    print("Iterative:")
    start = timeit.default_timer()
    fNumber = fibIterative(num)
    end = timeit.default_timer()
    elapsedNS = round((end - start) * 10 ** 9)
    print("Fibonacci(", num, ") = ", fNumber)
    print("Solution took",elapsedNS,"nanoseconds")

main()