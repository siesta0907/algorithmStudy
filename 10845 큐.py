#10845 큐
import sys

queue = []
N = int(input())

for i in range (N):
    command = sys.stdin.readline().split()
    
    if command[0] == "push":
        queue.append(int(command[1]))

    elif command[0] == "pop":
        if queue:
            pop = queue[0]
            del queue[0]
            print(pop)
        else:
            print(-1)

    elif command[0] == "size":
        print(len(queue))
    
    elif command[0] == "empty":
        if queue: print(0)
        else: print(1)

    elif command[0] == "front":
        if queue:
            print(queue[0])
        else: print(-1)

    elif command[0] == "back":
        if queue:
            print(queue[-1])
        else: print(-1)
