import qrcode
buy=[]
PRODUCTS=[]
def read_from_database():
    f=open("text.txt","r")
    for line in f:
        result=line.split(",")
        my_dict={"code":result[0],"name":result[1],"price":result[2],"count":result[3]}
        PRODUCTS.append(my_dict)
    f.close()

def write_to_database():
    f = open("text.txt" , "w")
    f = open("text.txt" , "a")
    for product in PRODUCTS:
        f.write(product["code"]+ ','+ product['name']+ ','+ product['price']+ ','+ product['count']+'\n'.strip())
    f.close()


def make_QRcode():
    code_input = input("enter code: ")
    for product in PRODUCTS:
        if code_input == product["code"]:
            img = qrcode.make(product)
            img.save('qrcode.png')

def show_menu():
    print("1_add")
    print("2_edit")
    print("3_remove")
    print("4_search")
    print("5_show list")
    print("6_QRcode")
    print("7_buy")
    print("8_exit")

def add():
    Code=input("enter code: ")
    name=input("enter name: ")
    price=input("enter price: ")
    count=input("enter count: ")
    new_product={"code":Code , "name":name , "price":price , "count": count}
    PRODUCTS.append(new_product)


def edit():
    code_input = input("enter code: ")
    choice = input("1- Name\n2- Price\n3- Count\n enter choice: ")

    for product in PRODUCTS:
        if code_input == product['code']:
            if choice == '1':
                product['name'] = input("enter new name: ")
            elif choice == '2':
                product['price'] = input("enter new price: ")
            elif choice == '3':
                product['count'] = input("enter new count: ")

            print("Data is updated successfully!")
            break
    else:
        product("code not found!")

def remove():
    code_input = input("enter code: ")
    for product in PRODUCTS:
        if code_input == product["code"]:
            PRODUCTS.remove(product)
            print(product["name"], 'removed successfully!')
            break
    else:
        print('code not found!')


def search():
    user_input = input("type your kewword: ")
    for prodcct in PRODUCTS:
        if prodcct["code"] == user_input or prodcct['name'] == user_input:
            print(prodcct['code'], "\t\t", prodcct['name'], "\t\t", prodcct['price'])
            break
    else:
        print('not found')

def show_list():
    for product in PRODUCTS:
        print(product["code"], "\t", product["name"], "\t", product["price"])




def buy():
    total_product = 0
    total = 0
    print('After completing the purchase, type the word (n).')

    while True:
        select = input("type your kewword (n): ")
        if select == 'n':
            break
        else:
            code_input = select
            for product in PRODUCTS:
                if product['code'] == code_input:
                    number = int(input("how many do you want? "))
                    product_count = int(product['count'])
                    if 0 < number <= product_count:
                        product_count -= number
                        product['count'] = product_count
                        buy_dict = {'code':code_input , 'name': product['name'], 'price': product['price'], 'number': number}
                        print(buy)
                        print()
                    else:
                        print('Insufficient inventory')
                        print('Number of', product['name'],'available:', product['count'])
                    break
            else: 
                print("This product is not available.")

    f = open('factor.txt', 'w')
    for product in Buy:
        total_product = int(product['price']) * int(product['number'])
        total += total_product
        f.write('name: '+ product['name']+ ', '+ 'price: '+ str(product['price'])+ ', '+'total_product: '+ str(total_product) + '\n')
        print(product['name'], product['price'], total_product)
        
    f.write('factor_total:' + str(total))
    print('factor_total: ', total)
        

while True:
    show_menu()
    choice = int(input("enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        make_QRcode()
    elif choice == 8:
        write_to_database()
        exit(0)
    else:
        print("try again!")



