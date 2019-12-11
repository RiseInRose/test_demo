def deidai_feibonaqi(a):
    if a < 1:
        print("a need > 0 !")
        return -1
    if a == 1 or a == 2:
        return 1
    else :
        return deidai_feibonaqi(a-1)+deidai_feibonaqi(a-2)

def digui_feibonaqi(a):
    n1 = 1
    n2 = 1
    n3 = 1
    if a < 1:
        print("a need > 0 !")
        return -1
    while (a-2) > 0:
        n3 = n2+n1
        n2 = n3
        n1 = n2

        a -= 1
    return n3

if __name__ == '__main__':
    a = input("please input a:")
    c = digui_feibonaqi(int(a))
    b = deidai_feibonaqi(int(a))
    print("%d digui %d" % (int(a) ,c))
    print("%d diedai %d" % (int(a) ,b))