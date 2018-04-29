import math

def collect_file(f):
    arr = []
    with open(f,"r")as file_read:
        for line in file_read:
            arr.append(float(line))
    return arr

def mean(arr):
    return sum(arr)/len(arr)

def stdev(arr):
    m = mean(arr)
    return math.sqrt(sum([(n-m)**2 for n in arr])/len(arr))

f = lambda x: x > 50.0 and x < 400.0
times = collect_file("boss times.txt")
times = filter(f, times)
            
        
