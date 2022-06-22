# AUTOMATED FIBONACCI PRINTER

When run, this small program makes use of APScheduler module to print out one digit of the fibonacci sequence (https://en.wikipedia.org/wiki/Fibonacci_number) every 10 seconds.

To use it, just clone this repo and run the following command on the respective directory:

<br>

```
python main.py
```

<br>
The output will be something like:

<br>

```
1
1
2
3
5
8
13
...
```

<br>

It will keep printing numbers following the sequence forever, as long as it's not stopped by pressing Ctrl + C.

<br>

##### Note: If you uncomment lines 1 and 16, APScheduler will also print the time at which the jobs have been called.