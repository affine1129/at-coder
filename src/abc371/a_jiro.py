S1, S2, S3 = input().split()

if S1 == '<' and S2 == '>' or S1 == '>' and S2 == '<':
    print('A')
elif S1 == '<' and S2 == '<' and S3 == '<' or S1 == '>' and S2 == '>' and S3 == '>':
    print('B')
else:
    print('C')
