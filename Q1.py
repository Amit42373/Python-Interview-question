# Find out common letters between two strings

def common_letter():
    s1 = input("enter the first string: ")
    s2 = input("enter the second string: ")
    str1 = set(s1)
    str2 = set(s2)

    comm_str = str1 & str2
    print(comm_str)


common_letter()






