print('  |  1  2  3  4  5  6  7  8  9')
print('--+---------------------------')
for b in range(1, 10):
    print(' {}|'.format(b), end=' ')
    for i in range(1, 10):
        print(str(i * b).rjust(2), end=' ')
    print()
