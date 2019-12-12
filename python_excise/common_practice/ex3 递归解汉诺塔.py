def digui_play_hannuota(n, x, y, z):
    global k
    if n == 1:
        print(x, ' --> ', z)
    else:
        digui_play_hannuota(n-1, x, z, y) # 将前n-1个盘子从x移动到y上
        k += 1
        print(x, ' --> ', z) # 将最底下的最后一个盘子从x移动到z上
        digui_play_hannuota(n-1, y, x, z) # 将y上的n-1个盘子移动到z上
        k +=1
    return k
if __name__ == '__main__':
    k = 1
    n = int(input('请输入汉诺塔的层数：'))
    print(digui_play_hannuota(n, 'X', 'Y', 'Z'))

