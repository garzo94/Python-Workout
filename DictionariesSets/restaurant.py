#my solution
def restaurant():
    total = 0
    menu = {'sandwich':10,
            'tea':7,
            'pizza':15}
    while True:
        order = input('order: ')
        if not order :
            print(f'your total is {total}')
            break
        elif order not in menu.keys():
            print(f'Sorry, we are fresh out of {order} today.')
        else:
            total += menu[order]
            print(f'{order} costs {menu[order]}, total is {total}')

restaurant()

#book solution
MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}
def restaurant():
    total = 0
    while True:
        order = input('Order: ').strip() # strip  removes spaces at the end and the beginning
        if not order:
            break
        if order in MENU:
            price = MENU[order]
            total += price
            print(f'{order} is {price}, total is {total}')
        else:
            print(f'We are fresh out of {order} today')
            print(f'Your total is {total}')
restaurant()