from math import cos, sin

readfilename = '1.txt'
writefilename = '1.txt'
speed = 2  # 走刀速度

P = 0  # 序号
alpha = 0


def g0(a):  # 行序号引入
    aa = a  # 第aa行
    flag = 0  # 判断G
    global x
    global y
    global z
    global P
    gamma = 0
    beta = 0
    while True:
        t = len(linelist[aa])  # 行列表长度
        for j in range(t):  # 第j个字符串
            if linelist[aa][j].startswith('X'):
                x = eval(linelist[aa][j].strip('X'))
            elif linelist[aa][j].startswith('Y'):
                y = eval(linelist[aa][j].strip('Y'))
            elif linelist[aa][j].startswith('Z'):
                z = eval(linelist[aa][j].strip('Z'))
            elif linelist[aa][j].startswith('A'):
                gamma = eval(linelist[aa][j].strip('A'))
            elif linelist[aa][j].startswith('B'):
                beta = eval(linelist[aa][j].strip('B'))
            elif linelist[aa][j].startswith('G') and a != aa:
                flag = 1
                break
            else:
                continue
        if flag or aa == tol - 1:
            break
        x = round(x, 3)
        y = round(y, 3)
        z = round(z, 3)  # 保留三位小数
        q1 = round(cos(0.5 * gamma) * cos(0.5 * beta) * cos(0.5 * alpha) + sin(0.5 * gamma) * sin(0.5 * beta) * sin(
            0.5 * alpha), 3)
        q2 = round(sin(0.5 * gamma) * cos(0.5 * beta) * cos(0.5 * alpha) - cos(0.5 * gamma) * sin(0.5 * beta) * sin(
            0.5 * alpha), 3)
        q3 = round(cos(0.5 * gamma) * sin(0.5 * beta) * cos(0.5 * alpha) + sin(0.5 * gamma) * cos(0.5 * beta) * sin(
            0.5 * alpha), 3)
        q4 = round(cos(0.5 * gamma) * cos(0.5 * beta) * sin(0.5 * alpha) - sin(0.5 * gamma) * sin(0.5 * beta) * cos(
            0.5 * alpha), 3)
        w.write('CONST robtarget P' + str(P) + ':=[[' + str(x) + ',' + str(y) + ',' + str(z) + ']')
        w.write(',[' + str(q1) + ',' + str(q2) + ',' + str(q3) + ',' + str(
            q4) + ']' + ',[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n')
        w.write('MoveJ P' + str(P) + ',V40,fine,tool2;\n')
        P += 1
        aa += 1


def g1(a):  # 行序号引入
    aa = a  # 第aa行
    flag = 0  # 判断G
    global x
    global y
    global z
    global P
    gamma = 0
    beta = 0
    while True:
        t = len(linelist[aa])  # 行列表长度
        for j in range(t):  # 第j个字符串
            if linelist[aa][j].startswith('X'):
                x = eval(linelist[aa][j].strip('X'))
            elif linelist[aa][j].startswith('Y'):
                y = eval(linelist[aa][j].strip('Y'))
            elif linelist[aa][j].startswith('Z'):
                z = eval(linelist[aa][j].strip('Z'))
            elif linelist[aa][j].startswith('A'):
                gamma = eval(linelist[aa][j].strip('A'))
            elif linelist[aa][j].startswith('B'):
                beta = eval(linelist[aa][j].strip('B'))
            elif linelist[aa][j].startswith('G') and a != aa:
                flag = 1
                break
            else:
                continue
        if flag or aa == tol - 1:
            break
        x = round(x, 3)
        y = round(y, 3)
        z = round(z, 3)  # 保留三位小数
        q1 = round(cos(0.5 * gamma) * cos(0.5 * beta) * cos(0.5 * alpha) + sin(0.5 * gamma) * sin(0.5 * beta) * sin(
            0.5 * alpha), 3)
        q2 = round(sin(0.5 * gamma) * cos(0.5 * beta) * cos(0.5 * alpha) - cos(0.5 * gamma) * sin(0.5 * beta) * sin(
            0.5 * alpha), 3)
        q3 = round(cos(0.5 * gamma) * sin(0.5 * beta) * cos(0.5 * alpha) + sin(0.5 * gamma) * cos(0.5 * beta) * sin(
            0.5 * alpha), 3)
        q4 = round(cos(0.5 * gamma) * cos(0.5 * beta) * sin(0.5 * alpha) - sin(0.5 * gamma) * sin(0.5 * beta) * cos(
            0.5 * alpha), 3)
        if speed == 1:
            w.write('CONST robtarget P' + str(P) + ':=[[' + str(x) + ',' + str(y) + ',' + str(z) + ']')
            w.write(',[' + str(q1) + ',' + str(q2) + ',' + str(q3) + ',' + str(
                q4) + ']' + ',[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n')
            w.write('MoveL P' + str(P) + ',V4.75,fine,tool2;\n')
        elif speed == 2:
            w.write('CONST robtarget P' + str(P) + ':=[[' + str(x) + ',' + str(y) + ',' + str(z) + ']')
            w.write(',[' + str(q1) + ',' + str(q2) + ',' + str(q3) + ',' + str(
                q4) + ']' + ',[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n')
            w.write('MoveL P' + str(P) + ',V10,fine,tool2;\n')
        elif speed == 3:
            w.write('CONST robtarget P' + str(P) + ':=[[' + str(x) + ',' + str(y) + ',' + str(z) + ']')
            w.write(',[' + str(q1) + ',' + str(q2) + ',' + str(q3) + ',' + str(
                q4) + ']' + ',[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n')
            w.write('MoveL P' + str(P) + ',V7.33,fine,tool2;\n')
        else:
            pass
        P += 1
        aa += 1


with open(writefilename, 'w') as w:
    with open(readfilename) as f:
        lines = f.readlines()
    tol = len(lines)
    linelist = []
    for i in range(tol):
        ls = (lines[i].rstrip()).split(' ')[1:]
        linelist.append(ls)
    x = 0
    y = 0
    z = 0
    I = 0
    J = 0
    for i in range(tol):
        if linelist[i][0] == 'G00':
            g0(i)
        elif linelist[i][0] == 'G01':
            g1(i)
        else:
            continue
