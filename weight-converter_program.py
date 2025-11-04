weight=int(input('Weight :'))
unit=input('(L)bs or K(g) ?').upper()

if unit=='L':
    converted=weight*0.45
    print(f'converted weight is: {converted}')
elif unit=='K':
    converted=weight/ 0.45
    print(f'converted weight is: {converted}')
else:
    print('Please write either "L" or "K"')