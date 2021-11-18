def func4(list):
    try:
        avg=0
        for i in range(len(list)):
            avg += list[i]
        avg =avg/len(list)
        for i in range(len(list)):
            list[i]=list[i]*avg
        return list
    except:
        print('Wrong list')
