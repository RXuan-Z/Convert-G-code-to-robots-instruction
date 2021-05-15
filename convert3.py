readfilename = '1.txt'
writefilename = '1-1.txt'
speed = 1  # 走刀速度

P = 0  # 序号


def G23WriteMoveInstrucion(speedi, x1, y1, x2, y2, z):
    if speedi == 1:
        w.write(
            "Pi1:=[[" + str(x1) + ',' + str(y1) + ',' + str(z) + "],[1,0,0,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write(
            "Pi2:=[[" + str(x2) + ',' + str(y2) + ',' + str(z) + "],[1,0,0,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write('MoveC P01,P02,V5,fine,MyTool;\n')
    elif speedi == 2:
        w.write(
            "Pi1:=[[" + str(x1) + ',' + str(y1) + ',' + str(z) + "],[1,0,0,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write(
            "Pi2:=[[" + str(x2) + ',' + str(y2) + ',' + str(z) + "],[1,0,0,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write('MoveC P01,P02,V10,fine,MyTool;\n')
    elif speedi == 3:
        w.write(
            "Pi1:=[[" + str(x1) + ',' + str(y1) + ',' + str(z) + "],[1,0,0,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write(
            "Pi2:=[[" + str(x2) + ',' + str(y2) + ',' + str(z) + "],[1,0,0,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write('MoveC P01,P02,V7,fine,MyTool;\n')
    else:
        pass


def G1WriteMoveInstrucion(speedi, x, y, z):
    if speedi == 1:
        w.write(
            "P1:=[[" + str(x) + ',' + str(y) + ',' + str(z) + "],[1,0,0,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write("MoveL P1,v5,fine,MyTool;\n")

    elif speedi == 2:
        w.write(
            "P1:=[[" + str(x) + ',' + str(y) + ',' + str(z) + "],[1,0,0,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write("MoveL P1,v10,fine,MyTool;\n")
    elif speedi == 3:
        w.write(
            "P1:=[[" + str(x) + ',' + str(y) + ',' + str(z) + "],[1,0,0,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write("MoveL P1,v7,fine,MyTool;\n")
    else:
        pass


def g0(a):  # 行序号引入
    aa = a  # 第aa行
    flag = 0  # 判断G
    global x
    global y
    global z
    global I
    global J
    global P
    while True:
        t = len(linelist[aa])  # 行列表长度
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
        x = round(x, 3)
        y = round(y, 3)
        z = round(z, 3)  # 保留三位小数
        w.write(
            "P0:=[[" + str(x) + ',' + str(y) + ',' + str(z) + "],[1,0,0,0],[1,1,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];\n")
        w.write('MoveJ P0,v40,fine,MyTool;\n')
        P += 1
        aa += 1


def g1(a):  # 行序号引入
    aa = a  # 第aa行
    flag = 0  # 判断G
    global x
    global y
    global z
    global I
    global J
    global P
    while True:
        t = len(linelist[aa])  # 行列表长度
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
        x = round(x, 3)
        y = round(y, 3)
        z = round(z, 3)  # 保留三位小数
        G1WriteMoveInstrucion(speed, str(x), str(y), str(z))

        P += 1
        aa += 1


def g2(a):  # 行序号引入
    aa = a  # 第aa行
    flag = 0  # 判断G
    global x
    global y
    global z
    global I
    global J
    global P
    while True:
        t = len(linelist[aa])  # 行列表长度
        x0 = x  # 上一次的结果
        y0 = y
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
        x2 = x0 + x
        y2 = y0 + y
        x1 = 0.5 * (x0 + x2)  # 运算输出结果
        if y0 >= 0:
            y1 = y0 + J + (I ** 2 + J ** 2 - (0.5 * x - I) ** 2) ** 0.5
        else:
            y1 = y0 + J - (I ** 2 + J ** 2 - (0.5 * x - I) ** 2) ** 0.5
        x1 = round(x1, 3)
        x2 = round(x2, 3)
        y1 = round(y1.real, 3)
        y2 = round(y2.real, 3)  # 保留三位小数
        G23WriteMoveInstrucion(speed, x1, y1, x2, y2, z)

        x = x2
        y = y2
        P += 2
        aa += 1


def g3(a):  # 行序号引入
    aa = a  # 第aa行
    flag = 0  # 判断G
    global x
    global y
    global z
    global I
    global J
    global P
    x0 = x  # 上一次的结果
    y0 = y
    while True:
        t = len(linelist[aa])  # 行列表长度
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
        x2 = x0 + x
        y2 = y0 + y
        x1 = 0.5 * (x0 + x2)  # 运算输出结果
        if y0 >= 0:
            y1 = y0 + J + (I ** 2 + J ** 2 - (0.5 * x - I) ** 2) ** 0.5
        else:
            y1 = y0 + J - (I ** 2 + J ** 2 - (0.5 * x - I) ** 2) ** 0.5
        x1 = round(x1, 3)
        x2 = round(x2, 3)
        y1 = round(y1.real, 3)
        y2 = round(y2.real, 3)  # 保留三位小数
        G23WriteMoveInstrucion(speed, x1, y1, x2, y2, z)
        x = x2
        y = y2
        P += 2
        aa += 1


with open(writefilename, 'w') as w:
    w.write("MODULE Cut\n")
    w.write("var robtarget Pi1;\n")
    w.write("var robtarget Pi2;\n")
    w.write("var robtarget P0;\n")
    w.write("var robtarget P1;\n")
    w.write("var robtarget P2;\n")
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
        elif linelist[i][0] == 'G02':
            g2(i)
        elif linelist[i][0] == 'G03':
            g3(i)
        else:
            continue
    w.write("END PROC\n")
    w.write("ENDMODULE")
