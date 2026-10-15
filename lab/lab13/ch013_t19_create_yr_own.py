fruits = ['0', '1', '2', 'End']

for f in fruits:
    if f == 'tomato':
        print('A tomato is not a fruit!')  # (It actually is.)
        # break
    print('A', f)
else:
    print('A fine selection of fruits!')
