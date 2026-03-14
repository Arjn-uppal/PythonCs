import timeit
import sys

def triangleRecursive(N):

    if N == 1:
        return 1
    else:
        return N + triangleRecursive(N-1)

def triangleIterative(N):
    sum = 0
    for i in range(1,N+1):
        sum = sum + i
    return sum

def main():
    sys.setrecursionlimit(2000)
    num = int(input("Calculate Triangle Number for N = "))

    print("\nRecursive:")
    start = timeit.default_timer()
    tNumber = triangleRecursive(num)
    end = timeit.default_timer()
    elapsedNS = round((end - start)*10**9)
    print("Triangle(",num,") = ", tNumber)
    print("Solution took",elapsedNS,"nanoseconds\n")

    print("Iterative:")
    start = timeit.default_timer()
    tNumber = triangleIterative(num)
    end = timeit.default_timer()
    elapsedNS = round((end - start) * 10 ** 9)
    print("Triangle(", num, ") = ", tNumber)
    print("Solution took",elapsedNS,"nanoseconds")

main()