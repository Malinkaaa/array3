def func1(n):
    try:
        print('Input number:')
        x=[float(j) for j in input().split()]
        print('List:')
        print(x)
        if(n!= len(x)):
            print("List's length is not " + str(n))
        else:
            print("List's length is " + str(n))
    except:
        print('You must type correct number!')

