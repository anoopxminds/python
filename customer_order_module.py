#customer_order_module

# Menu

menu = {
            1: {"name": "sandwich regular", "quantity": 10, "price": 75}, 
            2: {"name": "sandwich medium", "quantity": 10, "price": 150}, 
            3: {"name": "sandwich full", "quantity": 10, "price": 300}
        }

def display_menu():
    print("------- Menu List -------")
    selection = len(menu);
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : > 5}")

def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    #print("string : " + str(order))
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number : ')
        count += 1
        print(str(menu[int(item)]))
        order.append(menu[int(item)])
    return order

def main():
    order = take_order()
    print_order(order)
main()

