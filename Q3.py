# Conversion of two list into Dictionary Using Python

def list_to_dict():
    l1 = [1,2,3,4]
    l2 = ['one', 'two', 'three']

    result = dict(zip(l1,l2))
    print(result)

list_to_dict()

def dict_to_tuple():
    x = {1: 'one', 2: 'two', 3: 'three'}
    for i in x.items():
        print(i)

dict_to_tuple()