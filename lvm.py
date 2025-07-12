def push(num, ls):
    ls.insert(0, num)

def store(ls, reg):
    reg[0] = ls.pop(0)

def load(ls, reg):
    ls.insert(0, reg[0])

def plus(ls):
    ls[0] = ls[0] + ls[1]
    ls.pop(1)

def times(ls):
    ls[0] = ls[0] * ls[1]
    ls.pop(1)

def done(ls):
    print(ls[0])


ls = []
register = [0]  
n = int(input())
instructions = [input().split() for _ in range(n)]

i = 0 

while i < n:
    s = instructions[i]

    if len(s) == 2:
        cmd, val = s[0], s[1]
        if cmd == 'PUSH':
            push(int(val), ls)
            i += 1
        elif cmd == 'IFZERO':
            top = ls.pop(0)
            if top == 0:
                i = int(val)
            else:
                i += 1

    elif len(s) == 1:
        cmd = s[0]
        if cmd == 'STORE':
            store(ls, register)
        elif cmd == 'LOAD':
            load(ls, register)
        elif cmd == 'PLUS':
            plus(ls)
        elif cmd == 'TIMES':
            times(ls)
        elif cmd == 'DONE':
            done(ls)
            break
        i += 1
