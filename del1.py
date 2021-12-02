def smallest(a):
    if a[1] < a[0]:                 # c1: O(6)
        a[0], a[1] = a[1], a[0]     
    if a[2] < a[1]:                 
        a[1], a[2] = a[2], a[1]     
        if a[1] < a[0]:             
            a[0], a[1] = a[1], a[0] 
            
    f, s, t = a[0], a[1], a[2]      # c2: O(3)
    for e in a[3:len(a)]:           # always executes n-3 times
        if e < f:                   # c3: O(4)
            t = s                   
            s = f                    
            f = e                   
        elif e < s:                 # c4: O(3)
            t = s                   
            s = e                     
        elif e < t:                 # c5: O(2)
            t = e                   
    return (f, s, t)                # c6: O(1)

# time complexity: f(n) = c1 + c2 + c6 + (n-3)(c3 + c4 + c5)
# O(f(n)) = O(n-3) = O(n) - O(3) = O(n) 

# number of comparisons (best-case): 3 + n
# number of comparisons (worst-case): 3 + 3n



def merge(l, r):
    ret = []                            # O(1)
    while len(l) > 0 and len(r) > 0:    # 
        if l[0] > r[0] or l[0] == r[0]: # 
            ret.append(r[0])
            del r[0]
        elif r[0] > l[0]:
            ret.append(l[0])
            del l[0]     
    for el in l:
        ret.append(el)
    for er in r:
        ret.append(er)
    return ret

def correct(a):
    if len(a) >= 3: return list(smallest(a))    # c2 = O(4)
    if len(a) == 1: return [a[0]]               
    if len(a) == 2:
        if a[0] > a[1]: return [a[0], a[1]]
        else: return [a[1], a[0]]        

def smallestDAC(arr):
    n = len(arr)                    # c1: O(4)
    arr1 = arr[0      : n//3]
    arr2 = arr[n//3   : 2*n//3]
    arr3 = arr[2*n//3 : 3*n//3]

    v1 = correct(arr1)              # c2: se def.
    v2 = correct(arr2)
    v3 = correct(arr3)

    l1 = merge(v1, v2)              # c3: se def.
    l2 = merge(l1, v3)

    return (l2[0], l2[1], l2[2])    # O(1)

# O(f(n))  =  c1 + 3(c2) + 2(c3) + c4  =  

print(smallestDAC([1,2,3]))
arr = [27, 5, 13, 28, 25, 48, 54, 56, 64, 64, 62, 2, 1, 3]
print(smallestDAC(arr))