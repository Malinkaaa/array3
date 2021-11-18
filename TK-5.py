import math
def func5(list):
    try:
        for i in range(len(list)):
            list[i]= math.sqrt(list[i])
        return list
    except:
        print('Wrong list')
