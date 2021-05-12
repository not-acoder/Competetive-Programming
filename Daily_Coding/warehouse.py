# cmd='start'
queue = []
A = []
B = []
C = []
sent = []
while True:
    cmd = input()
    if cmd == 'DONE':
        break
    if 'RECV' in cmd:
        queue.append(cmd[5:])
    elif 'LOAD' in cmd:
        if cmd[5] == 'C':
            C.append(queue[0])
        elif cmd[5] == 'B':
            B.append(queue[0])
        else:
            A.append(queue[0])

        queue.pop(0)

    elif 'XFER' in cmd:
        if cmd[5] == 'A' and cmd[7] == 'B':
            B.append(A[-1])
            A.pop()
        elif cmd[5] == 'B' and cmd[7] == 'A':
            A.append(B[-1])
            B.pop()
        elif cmd[5] == 'C' and cmd[7] == 'B':
            B.append(C[-1])
            C.pop()
        elif cmd[5] == 'B' and cmd[7] == 'C':
            C.append(B[-1])
            B.pop()
        elif cmd[5] == 'A' and cmd[7] == 'C':
            C.append(A[-1])
            A.pop()
        elif cmd[5] == 'C' and cmd[7] == 'A':
            A.append(C[-1])
            C.pop()

    elif 'SEND' in cmd:
        sent.append(cmd[5])

g = 1
for i in sent:
    if i == 'C' and len(C) != 0:
        print('VACTRAIN' + ' ' + str(g))
        for r in C[::-1]:
            print(r)
    elif i == 'B' and len(B) != 0:
        print('VACTRAIN' + ' ' + str(g))
        for r in B[::-1]:
            print(r)
    elif i == 'A' and len(A) != 0:
        print('VACTRAIN' + ' ' + str(g))
        for r in A[::-1]:
            print(r)
    g += 1

