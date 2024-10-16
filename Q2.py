# Count the frequency of words appearing in a string

def frequency_of_words():
    str = 'sheena loves eating apple and mango. her sister also loves eating apple and mango.'

    li = str.split()
    d = {}

    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)

frequency_of_words()