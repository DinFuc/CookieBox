from math import ceil
def cookieBox(s):
    if (s**0.5).is_integer():return int(s**0.5),int(s**0.5)
    item=[]
    for i in range(int(s**0.5),1,-1):
        item.append([i,ceil(s/i)])
    item.sort(key = lambda x:(sum(x),x[0]*x[1]-s,x[0]))
    return item[0]
