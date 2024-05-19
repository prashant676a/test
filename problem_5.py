def boxy(n):
    if(n<1):
        print("box not possible for value less than 1")
        return
    print('  - '*n)
    print('-'*(4*n+1))
    for i in range(1,n+1):
        print(f'| {i} ', end='')
    print(' |')
    print('-'*(4*n+1))
    print('  - '*n)


boxy(1)


#i've done this using hit and trial , unaware of any other ideas.