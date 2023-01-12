name=input('Enter name')
for i in range(len(name)):
    for o in range(0, len(name)):
        if(i==o):
            print(name[o], sep=" ", end=" ")
        else:
            print('*', sep=" ", end=" ")
    print()