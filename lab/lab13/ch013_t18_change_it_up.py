fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape', 'potato']

print('You have...')
for f in fruits:
    if f == 'potato':
        print('A tomato is not a fruit!')  # (It actually is.)

        print('A', f)

        break
    else:
        print('A fine selection of fruits!')
