# from collections import deque

# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue)
# queue.reverse()
# print(queue)

# print(list(queue))

# def factorial_iterative(n):
#     result = 1
    
#     for i in range(1, n+1):
#         result *= i
#     return result

# def factorial_recursive(n):
#     if n<=1:
#         return 1
#     return n *factorial_recursive(n-1)

# print('반복적으로 구현:', factorial_iterative(5))
# print('재귀적으로 구현:', factorial_recursive(5))

# INF = 999999999

# graph =[
#     [0, 7, 5],
#     [7, 0, INF],
#     [5, INF, 0]
# ]

# print(graph)

graph = [[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))
graph[2].append((0,5))

print(graph)