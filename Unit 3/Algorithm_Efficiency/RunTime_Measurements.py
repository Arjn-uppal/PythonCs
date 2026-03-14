import timeit

start = timeit.default_timer()

print("hi")
print("hi")

end = timeit.default_timer()

time = end - start

timeMilli = round(time * 10**3, 3)
timeMicro = round(time * 10**6, None)
timeNano = round(time * 10**9, None)

print(timeMilli)
print(timeMicro)
print(timeNano)

