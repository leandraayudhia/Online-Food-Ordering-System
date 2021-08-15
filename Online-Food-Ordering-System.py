t_order = []
mu = 'Marugame Udon'
k_udon = 'Kake Udon (Rp.54.000)'
n_udon = 'Niku Udon (Rp.50.000)'
c_udon = 'Curry Udon (Rp.45.000)'
h_ocha = 'Hot Ocha (Rp.15.000)'

bk = 'Burger King'
c_bur = 'Cheese Burger (Rp.25.000)'
bbq = 'BBQ Beef Burger (Rp.33.000)'
chick = 'Chicken Burger (Rp.22.000)'
milo = 'Milo (Rp.12.000)'
mocc = 'Mocca Float (Rp.15.000)'

y = 'Yoshinoya'
ori_bowl = 'Original Beef Bowl (Rp.50.000)'
y_bowl = 'Yakiniku Beef Bowl (Rp.47.000)'
cs = 'Creamy Spinach (Rp.52.000)'
sp = 'Sparkling Mango (Rp.14.000)'

ct = 'Chatime'
haz = 'Hazelnut Chocolate Milk Tea (Rp.34.000)'
g_jelly = 'Grass Jelly With Fresh Milk (Rp.32.000)'
b_sugar = 'Brown Sugar with Fresh Milk (Rp.35.000)'
roast = 'Roasted Milk Tea (Rp.28.000)'

kkm = 'Kokumi'
uni = 'Unicorn Drink (Rp.35.000)'
lemon = 'Lemonade Stardust (Rp.33.000)'
mc = 'Matcha Macchiato Chocolate (Rp.31.000)'

gl = 'Gulu - Gulu'
rasp = 'Fruity Milk Tea Raspberry (Rp.28.000)'
win = 'Fruity Milk Tea Wintermelon (Rp.27.000)'
mang = 'Fruity Milk Tea Mango (Rp.32.000)'
pin = 'Fruity Milk Tea Pineapple (Rp.29.000)'

xft = 'Xing Fu Tang'
bboba = 'Brown Sugar Boba Milk (Rp.38.000'
ltea = 'Lemon Black Tea (Rp.32.000)'
soda = 'Soda and Handmade Jelly (Rp.35.000)'

price_m = {'Kake Udon': 54000, 'Niku Udon': 50000, 'Curry Udon': 45000, 'Hot Ocha': 15000,
         'Cheese Burger': 25000 , 'BBQ Beef Burger': 33000, 'Chicken Burger': 22000, 'Milo': 12000, 'Mocca Float': 15000,
         'Original Beef Bowl': 50000, 'Yakiniku Beef Bowl': 47000, 'Creamy Spinach': 52000, 'Sparkling Mango': 14000,
         'Hazelnut Chocolate Milk Tea': 34000, 'Grass Jelly With Fresh Milk': 32000, 'Brown Sugar with Fresh Milk': 35000, 'Roasted Milk Tea': 28000,
         'Unicorn Drink': 35000, 'Lemonade Stardust' : 33000, 'Matcha Macchiato Chocolate' : 31000,
         'Brown Sugar Boba Milk' : 38000, 'Lemon Black Tea' : 32000, 'Soda and Handmade Jelly': 35000}

def mu_menu():
    print('Menu:\n', ('1. '+ k_udon), ('\n 2. '+ n_udon), ('\n 3. ' + c_udon), ('\n 4. ' + h_ocha))

def bk_menu():
    print('Menu:\n', ('1. '+ c_bur), ('\n 2. '+ bbq), ('\n 3. ' + chick), ('\n 4. ' + milo), ('\n 5. ' + mocc))

def y_menu():
    print('Menu:\n', ('1. '+ ori_bowl), ('\n 2. '+ y_bowl), ('\n 3. ' + cs), ('\n 4. ' + sp))

def ct_menu():
    print('Menu:\n', ('1. '+ haz), ('\n 2. '+ g_jelly), ('\n 3. ' + b_sugar), ('\n 4. ' + roast))

def kkm_menu():
    print('Menu:\n', ('1. '+ uni), ('\n 2. '+ lemon), ('\n 3. ' + mc))

def xft_menu():
    print('Menu:\n', ('1. '+ bboba), ('\n 2. '+ ltea), ('\n 3. ' + soda))

def main_order():
    f_o =('ORDER')
    print(f_o.center(175))
    print('_'*180)
    print('Pick Location: ')
    print('1. 23Paskal')
    print('2. Paris Van Java')
    print('3. Trans Studio Mall')
    try:
        loc = int(input('Please enter the Location number: '))
    except ValueError:
        print("Please type corectly!")
        loc = int(input('Please enter the Location number: '))
    price = 0
    total = 0
    L = int(loc)

    if L == 1:
        print('Choose Restaurant: \n', ('1. '+ mu), ('\n 2. '+ bk), ('\n 3. ' + y), ('\n 4. ' + ct), ('\n 5. '+ kkm))
        r = str(input('Input the Restaurant Number here: '))
        if r == '1':
            mu_menu()
            o = str(input("Input Menu number: "))
            if o == '1':
                price = price_m['Kake Udon']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '2':
                price = price_m['Niku Udon']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '3':
                price = price_m['Curry Udon']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '4':
                price = price_m['Hot Ocha']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            else:
                print('Please input numbers only')

        elif r == '2':
            bk_menu()
            o = str(input("Input Menu number: "))
            if o == '1':
                price = price_m['Cheese Burger']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '2':
                price = price_m['BBQ Beef Burger']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '3':
                price = price_m['Chicken Burger']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '4':
                price = price_m['Milo']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '5':
                price = price_m['Mocca Float']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            else:
                print('Please input numbers only')

        elif r == '3':
            y_menu()
            o = str(input("Input Menu number: "))
            if o == '1':
                price = price_m['Original Beef Bowl']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '2':
                price = price_m['Yakiniku Beef Bowl']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '3':
                price = price_m['Creamy Spinach']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '4':
                price = price_m['Sparkling Mango']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            else:
                print('Please input numbers only')

        elif r == '4':
            ct_menu()
            o = str(input("Input Menu number: "))
            if o == '1':
                price = price_m['Hazelnut Chocolate Milk Tea']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '2':
                price = price_m['Grass Jelly With Fresh Milk']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '3':
                price = price_m['Brown Sugar with Fresh Milk']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '4':
                price = price_m['Roasted Milk Tea']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            else:
                print('Please input numbers only')

        elif r == '5':
            kkm_menu()
            o = str(input("Input Menu number: "))
            if o == '1':
                price = price_m['Unicorn Drink']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '2':
                price = price_m['Lemonade Stardust']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '3':
                price = price_m['Matcha Macchiato Chocolate']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            else:
                print('Please input numbers only')
        else:
            print('Please input numbers only')

    elif L == 2:
        print('Choose Restaurant: \n', ('1. '+ mu), ('\n 2. '+ y), ('\n 3. ' + xft))
        r = str(input('Input the Restaurant Number here: '))
        if r == '1':
            mu_menu()
            o = str(input("Input Menu number: "))
            if o == '1':
                price = price_m['Kake Udon']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '2':
                price = price_m['Niku Udon']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '3':
                price = price_m['Curry Udon']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '4':
                price = price_m['Hot Ocha']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            else:
                print('Please input numbers only')

        elif r == '2':
            y_menu()
            o = str(input("Input Menu number: "))
            if o == '1':
                price = price_m['Original Beef Bowl']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '2':
                price = price_m['Yakiniku Beef Bowl']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '3':
                price = price_m['Creamy Spinach']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '4':
                price = price_m['Sparkling Mango']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            else:
                print('Please input numbers only')

        elif r == '3':
            xft_menu()
            o = str(input("Input Menu number: "))
            if o == '1':
                price = price_m['Brown Sugar Boba Milk']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '2':
                price = price_m['Lemon Black Tea']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '3':
                price = price_m['Soda and Handmade Jelly']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            else:
                print('Please input numbers only')
        else:
            print('Please input numbers only')

    elif L == 3:
        print('Choose Restaurant: \n', ('1. '+ y), ('\n 2. '+ ct))
        r = str(input('Input the Restaurant Number here: '))
        if r == '1':
            y_menu()
            o = str(input("Input Menu number: "))
            if o == '1':
                price = price_m['Original Beef Bowl']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '2':
                price = price_m['Yakiniku Beef Bowl']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '3':
                price = price_m['Creamy Spinach']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '4':
                price = price_m['Sparkling Mango']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            else:
                print('Please input numbers only')

        elif r == '2':
            ct_menu()
            o = str(input("Input Menu number: "))
            if o == '1':
                price = price_m['Hazelnut Chocolate Milk Tea']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '2':
                price = price_m['Grass Jelly With Fresh Milk']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '3':
                price = price_m['Brown Sugar with Fresh Milk']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '4':
                price = price_m['Roasted Milk Tea']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            else:
                print('Please input numbers only')

        elif r == '3':
            xft_menu()
            o = str(input("Input Menu number: "))
            if o == '1':
                price = price_m['Brown Sugar Boba Milk']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '2':
                price = price_m['Lemon Black Tea']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            elif o == '3':
                price = price_m['Soda and Handmade Jelly']
                qty = int(input('Input Qty: '))
                t_order.append(qty*price)
            else:
                print('Please input numbers only')
        else:
            print('Please input numbers only')
    else:
        print('Please enter correctly!')

    order = "yes"
    while order == "yes":
        order = input("Do you want to order again? (yes/no): ")
        if order == "yes":
            main_order()
        elif order == "no":
            s = str(input('Do you want to delivery it to your home or pick up in location? (delivery/pick up): '))
            for i in range (len(t_order)):
                total = total + t_order[i]
            tax = (15*total/100)
            bill = total + tax
            print('Total Order: ', bill)
            print('Orders will be made soon, please wait for 15 minutes, thank you.')
            exit()
    for i in range (len(t_order)):
        total = total + t_order[i]
    tax = (15*total/100)
    bill = total + tax
    print('Total Order: ', bill)

    print("Thank You")

def main():
    f_o =('ORDER')
    print(f_o.center(175))
    print('_'*180)
    print('Pick Location: ')
    print('1. 23Paskal')
    print('2. Paris Van Java')
    print('3. Trans Studio Mall')
    loc = str(input('Please enter the Location number: '))
    if loc == '1' or '2' or '3':
        main_order()
    else:
        print('Please type correctly!')

main_order()
