S = input()
T = input()

if S == T:
    print(0)
else:
    for i, (s, t) in enumerate(zip(S, T)):
        if s != t:
            print(i + 1)
            break
    else:
        print(min(len(S), len(T)) + 1)
