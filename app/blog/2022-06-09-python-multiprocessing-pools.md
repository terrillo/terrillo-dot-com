How many times in python have used a for loop and watched your terminal go through each item taking hours on end?

This article goes over the Multiprocessing module for Python. People get excited that Python uses threading. I know I was coming from PHP land. Threading is different than Multiprocessing by the way.

The threading module uses threads, the multiprocessing module uses processes. The difference is that threads run in the same memory space, while processes have separate memory. This makes it a bit harder to share objects between processes with multiprocessing. Since threads use the same memory, precautions have to be taken or two threads will write to the same memory at the same time.

The [multiprocessing](https://docs.python.org/dev/library/multiprocessing.html) module in Python’s Standard Library has a lot of powerful features. — [Official documentation](https://docs.python.org/dev/library/multiprocessing.html)

[[youtube_1]]

## Basic loop without Multiprocessing

```
def f(x):
    # Run Code
    print(x*x)
for item in [1, 2, 3, 4]:
    f(item)
```

### Run

```
time python3 main.py

>> 1
>> 4
>> 9
>> 16
>> python3 main.py  0.04s user 0.01s system 89% cpu 0.059 total
```


**0.059s** is nothing. Let’s say that the `f()` function executes some code that takes 2 seconds long (Updating a database, Resizing Images, scraping a website, etc).

## Basic loop with 2s delay

```
import time

def f(x):
    time.sleep(2) # Wait 2 seconds
    print(x*x)

for item in [1, 2, 3, 4]:
    f(item)
```

### Run

```
time python3 main.py

>> 1
>> 4
>> 9
>> 16
>> python3 main.py  0.04s user 0.01s system 89% cpu 8.067 total
```

**8.067s** adds up over 200 items. This when Multiprocessing can become your friend. Imagine running multiple items at once over that same two-second period. Parallel processing is getting more attention nowadays. As CPU manufacturers start adding more and more cores to their processors, creating parallel code is a great way to improve performance. Python introduced the multiprocessing module to let us write parallel code.

There are plenty of classes in Python multiprocessing module for building a parallel program. Among them, three basic classes are Process, Queue and Lock. These classes will help you to build a parallel program. This is an introduction to Pool.

A process pool object which controls a pool of worker processes to which jobs can be submitted. It supports asynchronous results with timeouts and callbacks and has a parallel map implementation


## Basic loop with 2s delay using Multiprocessing

```
import time 
from multiprocessing import Pool

def f(x):
    time.sleep(2) # Wait 2 seconds
    print(x*x)

p = Pool(8)
p.map(f, [1, 2, 3, 4])
p.close()
p.join()
```

### Run 

```
time python3 main.py

>> 1
>> 4
>> 9
>> 16
>> python3 main.py  0.08s user 0.06s system 6% cpu 2.180 total
```

**2.180s vs 8.067s** means each item in the same array took 2 seconds. Impressive right. It’s really nice when you do this on a Linux box. Your code can better use the resources available to you. So, that’s multiprocessing Pools in Python.

Thanks for reading.

