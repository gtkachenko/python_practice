import time
def flutten(mylist):
    calctime = time.time()
    i = 0
    while i < len(mylist):
        while True:
            try:
                mylist[i:i+1] = mylist[i]
            except(IndexError,TypeError):
                break
        i += 1
    print('Time of executing is %f' % (time.time()-calctime))


lst = [1,[2,[3,[4]],5]]
flutten(lst)
print(lst)

def flatten(lst1):
    result = lst1
    calctime = time.time()
    while True:
        temp_result = []
        for item in result:
            if isinstance(item, list):
                temp_result.extend(item)
            else:
                temp_result.append(item)
        result = temp_result
        interrupt = True
        for i in result:
            if isinstance(i,list):
                interrupt = False
        if interrupt:
            break
    print('Time of exectuting function is %f' % (time.time()-calctime))
    return result

lst1 = [1,[2,[3,[4]],5]]
print(flatten(lst1))

