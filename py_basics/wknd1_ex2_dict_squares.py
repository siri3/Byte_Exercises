#print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
def fn():
    sqdict = {}
    for k in range (1,4):
        sqdict[k] = k*k
    for k,v in sqdict.items():
        print (k," ",v)
fn()
                