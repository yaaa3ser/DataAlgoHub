# if we want to measure the time of a function, we can use the time module like this:
import time
start = time.time()
for i in range(5):
    time.sleep(1)
end = time.time()

print(end - start) 

# but time module is not accurate and depends on the clock of the system, so it may cause problems if the system clock is changed
# so we use perf_counter() instead ===> it provides a relative time and has no reference to the system clock

start = time.perf_counter()
for i in range(5):
    time.sleep(1)
end = time.perf_counter()

print(end - start) 
