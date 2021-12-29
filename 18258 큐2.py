#18258 큐2

from collections import deque
import sys

dq = deque([])

N = int(sys.stdin.readline())

for i in range (N):
    command = sys.stdin.readline().split()
    
    if command[0] == "push":
        dq.append(int(command[1]))

    elif command[0] == "pop":
        if dq:
            print(dq.popleft())
        else:
            print(-1)

    elif command[0] == "size":
        print(len(dq))
    
    elif command[0] == "empty":
        if dq: print(0)
        else: print(1)

    elif command[0] == "front":
        if dq:
            print(dq[0])
        else: print(-1)

    elif command[0] == "back":
        if dq:
            print(dq[-1])
        else: print(-1)
