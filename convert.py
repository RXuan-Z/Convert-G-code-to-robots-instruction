readfilename = '1.txt'
writefilename = '1-1.txt'


def g0(a):  # 行序号引入
    aa = a  # 第aa行
    flag = 0  # 判断G
    while True:
        t = len(linelist[aa])  # 行列表长度
        x = 0
        y = 0
        z = 0
        for j in range(t):  # 第j个字符串
            if linelist[aa][j].startswith('X'):
                x = eval(linelist[aa][j].strip('X'))
            elif linelist[aa][j].startswith('Y'):
                y = eval(linelist[aa][j].strip('Y'))
            elif linelist[aa][j].startswith('Z'):
                z = eval(linelist[aa][j].strip('Z'))
            elif linelist[aa][j].startswith('G') and a != aa:
                flag = 1
                break
            else:
                continue
        if flag or aa == tol - 1:
            break
        w.write('G00' + '(' + str(x) + ',' + str(y) + ',' + str(z) + ')\n')
        aa += 1


def g1(a):  # 行序号引入
    aa = a  # 第aa行
    flag = 0  # 判断G
    while True:
        t = len(linelist[aa])  # 行列表长度
        x = 0
        y = 0
        z = 0
        for j in range(t):  # 第j个字符串
            if linelist[aa][j].startswith('X'):
                x = eval(linelist[aa][j].strip('X'))
            elif linelist[aa][j].startswith('Y'):
                y = eval(linelist[aa][j].strip('Y'))
            elif linelist[aa][j].startswith('Z'):
                z = eval(linelist[aa][j].strip('Z'))
            elif linelist[aa][j].startswith('G') and a != aa:
                flag = 1
                break
            else:
                continue
        if flag or aa == tol - 1:
            break
        w.write('G01' + '(' + str(x) + ',' + str(y) + ',' + str(z) + ')\n')
        aa += 1


def g2(a):  # 行序号引入
    aa = a  # 第aa行
    flag = 0  # 判断G
    while True:
        t = len(linelist[aa])  # 行列表长度
        x = 0
        y = 0
        I = 0
        J = 0
        for j in range(t):  # 第j个字符串
            if linelist[aa][j].startswith('X'):
                x = eval(linelist[aa][j].strip('X'))
            elif linelist[aa][j].startswith('Y'):
                y = eval(linelist[aa][j].strip('Y'))
            elif linelist[aa][j].startswith('I'):
                I = eval(linelist[aa][j].strip('I'))
            elif linelist[aa][j].startswith('J'):
                J = eval(linelist[aa][j].strip('J'))
            elif linelist[aa][j].startswith('G') and a != aa:
                flag = 1
                break
            else:
                continue
        if flag or aa == tol - 1:
            break
        w.write('G02' + '(' + str(x) + ',' + str(y) + ',' + str(I) + ',' + str(J) + ')\n')
        aa += 1


def g3(a):  # 行序号引入
    aa = a  # 第aa行
    flag = 0  # 判断G
    while True:
        t = len(linelist[aa])  # 行列表长度
        x = 0
        y = 0
        I = 0
        J = 0
        for j in range(t):  # 第j个字符串
            if linelist[aa][j].startswith('X'):
                x = eval(linelist[aa][j].strip('X'))
            elif linelist[aa][j].startswith('Y'):
                y = eval(linelist[aa][j].strip('Y'))
            elif linelist[aa][j].startswith('I'):
                I = eval(linelist[aa][j].strip('I'))
            elif linelist[aa][j].startswith('J'):
                J = eval(linelist[aa][j].strip('J'))
            elif linelist[aa][j].startswith('G') and a != aa:
                flag = 1
                break
            else:
                continue
        if flag or aa == tol - 1:
            break
        w.write('G03' + '(' + str(x) + ',' + str(y) + ',' + str(I) + ',' + str(J) + ')\n')
        aa += 1


with open(writefilename, 'w') as w:
    with open(readfilename) as f:
        lines = f.readlines()
    tol = len(lines)
    linelist = []
    for i in range(tol):
        ls = (lines[i].rstrip()).split(' ')[1:]
        linelist.append(ls)
    for i in range(tol):
        if linelist[i][0] == 'G00':
            g0(i)
        elif linelist[i][0] == 'G01':
            g1(i)
        elif linelist[i][0] == 'G02':
            g2(i)
        elif linelist[i][0] == 'G03':
            g3(i)
        else:
            continue
