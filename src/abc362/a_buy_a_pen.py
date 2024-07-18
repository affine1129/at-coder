R, G, B = map(int, input().split())

C = input()

if C == 'Red':
    print(min(G, B))
elif C == 'Green':
    print(min(R, B))
elif C == 'Blue':
    print(min(R, G))
