import math
from math import cos, sin

readfilename = '1.txt'
writefilename = '1-1.txt'
speed = 2  # 走刀速度

P = 0  # 序号
alpha = 0


def G1WriteMoveInstrucion(speedi, x, y, z, q1, q2, q3, q4):
    if speedi == 1:
        w.write(
            "P1:=[[" + str(x) + ',' + str(y) + ',' + str(
                z) + "],[" + q1 + ',' + q2 + ',' + q3 + ',' + q4 + ']' + ",[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write("MoveL P1,v5,fine,MyTool;\n")

    elif speedi == 2:
        w.write(
            "P1:=[[" + str(x) + ',' + str(y) + ',' + str(
                z) + "],[" + q1 + ',' + q2 + ',' + q3 + ',' + q4 + ']' + ",[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write("MoveL P1,v10,fine,MyTool;\n")
    elif speedi == 3:
        w.write(
            "P1:=[[" + str(x) + ',' + str(y) + ',' + str(
                z) + "],[" + q1 + ',' + q2 + ',' + q3 + ',' + q4 + ']' + ",[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write("MoveL P1,v7,fine,MyTool;\n")
    else:
        pass


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
        q1 = round(
            cos(math.pi / 180 * 0.5 * gamma) * cos(math.pi / 180 * 0.5 * beta) * cos(math.pi / 180 * 0.5 * alpha) + sin(
                math.pi / 180 * 0.5 * gamma) * sin(math.pi / 180 * 0.5 * beta) * sin(math.pi / 180 *
                                                                                     0.5 * alpha), 3)
        q2 = round(
            sin(math.pi / 180 * 0.5 * gamma) * cos(math.pi / 180 * 0.5 * beta) * cos(math.pi / 180 * 0.5 * alpha) - cos(
                math.pi / 180 * 0.5 * gamma) * sin(math.pi / 180 * 0.5 * beta) * sin(math.pi / 180 *
                                                                                     0.5 * alpha), 3)
        q3 = round(
            cos(math.pi / 180 * 0.5 * gamma) * sin(math.pi / 180 * 0.5 * beta) * cos(math.pi / 180 * 0.5 * alpha) + sin(
                math.pi / 180 * 0.5 * gamma) * cos(math.pi / 180 * 0.5 * beta) * sin(math.pi / 180 *
                                                                                     0.5 * alpha), 3)
        q4 = round(
            cos(math.pi / 180 * 0.5 * gamma) * cos(math.pi / 180 * 0.5 * beta) * sin(math.pi / 180 * 0.5 * alpha) - sin(
                math.pi / 180 * 0.5 * gamma) * sin(math.pi / 180 * 0.5 * beta) * cos(math.pi / 180 *
                                                                                     0.5 * alpha), 3)
        w.write("P0:=[[" + str(x) + ',' + str(y) + ',' + str(z) + ']')
        w.write(',[' + str(q1) + ',' + str(q2) + ',' + str(q3) + ',' + str(
            q4) + ']' + ',[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n')
        w.write('MoveJ P0,v40,fine,MyTool;\n')
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
        q1 = round(
            cos(math.pi / 180 * 0.5 * gamma) * cos(math.pi / 180 * 0.5 * beta) * cos(math.pi / 180 * 0.5 * alpha) + sin(
                math.pi / 180 * 0.5 * gamma) * sin(math.pi / 180 * 0.5 * beta) * sin(math.pi / 180 *
                                                                                     0.5 * alpha), 3)
        q2 = round(
            sin(math.pi / 180 * 0.5 * gamma) * cos(math.pi / 180 * 0.5 * beta) * cos(math.pi / 180 * 0.5 * alpha) - cos(
                math.pi / 180 * 0.5 * gamma) * sin(math.pi / 180 * 0.5 * beta) * sin(math.pi / 180 *
                                                                                     0.5 * alpha), 3)
        q3 = round(
            cos(math.pi / 180 * 0.5 * gamma) * sin(math.pi / 180 * 0.5 * beta) * cos(math.pi / 180 * 0.5 * alpha) + sin(
                math.pi / 180 * 0.5 * gamma) * cos(math.pi / 180 * 0.5 * beta) * sin(math.pi / 180 *
                                                                                     0.5 * alpha), 3)
        q4 = round(
            cos(math.pi / 180 * 0.5 * gamma) * cos(math.pi / 180 * 0.5 * beta) * sin(math.pi / 180 * 0.5 * alpha) - sin(
                math.pi / 180 * 0.5 * gamma) * sin(math.pi / 180 * 0.5 * beta) * cos(math.pi / 180 *
                                                                                     0.5 * alpha), 3)
        G1WriteMoveInstrucion(speed, str(x), str(y), str(z), str(q1), str(q2), str(q3), str(q4))
        P += 1
        aa += 1


with open(writefilename, 'w') as w:
    w.write("MODULE Cut\n")
    w.write("var robtarget P0;\n")
    w.write("var robtarget P1;\n")
    w.write("PROC MoveSub()\n")
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
    w.write("END PROC\n")
    w.write("ENDMODULE")
