def jiechen(a):
    b = 1
    for each in range(1,a+1):
        b = each * b
    return b

if __name__ == '__main__':
    print(jiechen(10))