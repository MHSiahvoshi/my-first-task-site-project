try:
    from my_sql import *
    import shop_mod
    import colorama
    import csv
    import schedule
    import time
    import os
    import factor
    import pay_api
    import payment
    import openpyxl
except Exception as x:
    print(x)

wb = openpyxl.Workbook()


try:
    if not os.path.exists(r'C:\Users\MohammadHossein\PycharmProjects\pythonProject6\admin_data_log.csv'):
        admin_csv = open('admin_data_log.csv', 'w', newline='\n', encoding='utf-8')
        csv_writer = csv.writer(admin_csv)
        csv_writer.writerow(('id', 'full_name', 'username', 'password', 'phone', 'national_code', 'is_staff'))
        admin_csv.close()
except Exception as x:
    print(x)


def admin_username_checker(username: str):
    csv_reader = []
    with open('admin_data_log.csv', 'r', encoding='utf-8') as username_checker:
        username_reader = csv.reader(username_checker)
        try:
            next(username_reader)
            for c in username_reader:
                csv_reader.append(c[2])
        except:
            return True
    try:
        for i in csv_reader:
            if username == i:
                return False
        else:
            return True
    except:
        return True


def admin_accept():
    temp, out = [], []
    with open('admin_data_log.csv', 'r', encoding='utf-8', newline='\n') as data_log:
        data_reader = csv.reader(data_log)
        next(data_reader)
        for c in data_reader:
            temp.append(c)
    for i in temp:
        if i[-1] == '1':
            i[-1] = int(i[-1])
            out.append(i)
    admin_signup_db(data=out)


schedule.every(1).minutes.do(admin_accept)
schedule.every(1).days.do(factor.manage_time)
# schedule.every(2).minutes.do(factor.check_if_paid)


def csv_reader_id():
    out = []
    with open('admin_data_log.csv', 'r', encoding='utf-8') as data:
        csv_reader = csv.reader(data)
        next(csv_reader)
        # if csv_reader.line_num >= 2:
        try:
            for row in csv_reader:
                out.append(row)
            if out[0][0] == '1' or len(out[0]) != 0:
                return int(out[-1][0])
            else:
                return 0
        except:
            return 0


colorama.init()
customer_data, employee_data = [], []


def customer_definition():
    global customer_data
    customer.name = input('please enter your name: ')
    customer.family = input('please enter your family: ')
    customer.username = input('please enter your username: ')
    while not check_username(customer.username):
        customer.username = input('please enter your username or type(exit): ')

    customer.password = input('please enter your password: ')
    customer.email = input('please enter your email: ')
    customer.phone = input('please enter your phone: ')
    customer.address = input('please enter your address: ')
    try:
        customer.national_code = int(input('please enter your national code: '))
        customer.post_code = int(input('please enter your post code: '))
    except Exception as x:
        print(x)
    customer_flag = input('are you sure to save these?(y/n) ')
    if customer_flag == 'y':
        # if shop_mod.check_parameters():
        customer_data = [customer.name, customer.family, customer.username, customer.password, customer.email,
                         customer.phone, customer.address, customer.national_code, customer.post_code]

        if import_customer(customer_data) == 'customer added':
            print(f'{colorama.Fore.GREEN}registered{colorama.Fore.RESET}')
            customer_data = []
        else:
            print(f'{colorama.Fore.RED}your data is wrong!!!!!{colorama.Fore.RESET}')
    else:
        print(f'{colorama.Fore.YELLOW}your data lost{colorama.Fore.RESET}')


def employee_definition():
    global employee_data
    employee.name = input('please enter your name: ')
    employee.family = input('please enter your family: ')
    employee.username = input('please enter your username: ')
    while not check_username(employee.username):
        employee.username = input('please enter your username: ')
    employee.password = input('please enter your password: ')
    employee.email = input('please enter your email: ')
    employee.phone = input('please enter your phone: ')
    employee.address = input('please enter your address: ')
    try:
        employee.job_position = input('please enter your job position: ')
        employee.salary = int(input('please enter your salary: '))
        employee.job_guarantee = int(input('please enter your job guarantee: '))
    except Exception as x:
        print(x)
    employee_flag = input('are you sure to save these?(y/n) ')
    if employee_flag == 'y':
        # if shop_mod.check_parameters():
        employee_data = [employee.name, employee.family, employee.username, employee.password, employee.email,
                         employee.phone, employee.address, employee.job_position, employee.salary,
                         employee.job_guarantee]

        if import_employee(employee_data) == 'employee added':

            print(f'{colorama.Fore.GREEN}registered{colorama.Fore.RESET}')
        else:
            print(f'{colorama.Fore.RED}your data is wrong!!!!!{colorama.Fore.RESET}')
    else:
        print(f'{colorama.Fore.YELLOW}your data lost{colorama.Fore.RESET}')


def admin_definition():
    admin.admin_full_name = input('please enter admin full name: ')
    admin.admin_user = input('please enter admin username: ')
    admin.admin_pass = input('please enter admin password: ')
    admin.admin_phone = input('please enter admin phone: ')
    try:
        admin.admin_national_code = int(input('please enter admin national code: '))
    except Exception as x:
        print(x)
    make_sure = input('are you sure?(y/n): ')
    if make_sure == 'y':
        row_id = csv_reader_id()
        if admin_username_checker(admin.admin_user):
            admin_data = (row_id + 1, admin.admin_full_name, admin.admin_user, admin.admin_pass, admin.admin_phone,
                            admin.admin_national_code, 0)
            with open('admin_data_log.csv', 'a', newline='\n', encoding='utf-8') as admin_csv2:
                csv_writer2 = csv.writer(admin_csv2)
                csv_writer2.writerow(admin_data)
            print(f'{colorama.Fore.CYAN}your data sent.\nif data registered by admin we tell you.{colorama.Fore.RESET}'
                  f' {colorama.Fore.YELLOW}:){colorama.Fore.RESET}')
        else:
            print('this username is already exists please choose another!!!!!')
    else:
        print('your data lost!!!!!')


def admin_login():
    ws = wb.active
    admin.admin_user = input('please enter admin username: ')
    admin.admin_pass = input('please enter admin password: ')
    if admin_login_db([admin.admin_user, admin.admin_pass]):
        print(f'{colorama.Fore.GREEN}you are logged in{colorama.Fore.RESET}')
        out = []
        while True:
            try:
                sale = int(input('please give me your sale: '))
            except Exception as x:
                print(x)
            else:
                pro_name = input('please enter your product name: ')
                pro_com = input('please enter your product company: ')
                pro_pri = input('please enter your product price:')
                out.extend([pro_name, pro_com, pro_pri])
                ws.append(out)
                wb.save('data for twitter.xlsx')
                exit_advertisement = input(
                    f'{colorama.Fore.YELLOW}if you want to exit, type (exit):{colorama.Fore.RESET} ')
                if exit_advertisement == 'exit':
                    break

    else:
        print(f"{colorama.Fore.RED}invalid username or password!!!!!\nplease create one{colorama.Fore.RESET}")


def product_definition(product_type: int):
    product.product_name = input('please enter name: ')
    product.barcode = input('please enter barcode: ')
    product.product_type = input('please enter type: ')
    product.company = input('please enter company: ')
    product.production = input('please enter production in this format(yyyy-mm-dd): ')
    try:
        product.price = eval(input('please enter price: '))
        product.guarantee = int(input('please enter guarantee in day: '))
    except Exception as x:
        print(x)
    product.address_company = input('please enter address of company: ')
    product.description = input('please enter description: ')

    product_db = Products(product.product_code(), product.product_name, product.barcode,
                          product.product_type, product.company,
                          product.production, product.price, product.guarantee,
                          product.address_company, product.description)

    if product_type == 1:
        digital_product.cpu = input('please enter cpu: ')
        digital_product.ram = input('please enter ram: ')
        digital_product.internal_storage = input('please enter internal storage: ')
        digital_product.dimention_lcd = input('please enter dimension of lcd: ')
        digital_product.graphic = input('please enter graphic: ')
        digital_product.color = input('please enter color: ')
        digital_product.charger = input('please enter charger: ')
        digital_product.os = input('please enter os: ')
        digital_product.type_sound = input('please enter type of sound: ')
        try:
            digital_product.touch = bool(int(input('please enter touch, only 0 or 1: ')))
            digital_product.aux = bool(int(input('please enter aux, only 0 or 1: ')))
            digital_product.sd_card = bool(int(input('please enter sd card, only 0 or 1: ')))
            digital_product.ir = bool(int(input('please enter IR, only 0 or 1: ')))
        except Exception as x:
            print(x)
        product_db.digital_product([product_db.product(login.login_employee())[0][0], digital_product.cpu,
                                    digital_product.ram, digital_product.internal_storage,
                                    digital_product.dimention_lcd, digital_product.graphic, digital_product.color,
                                    digital_product.charger, digital_product.os, digital_product.type_sound,
                                    digital_product.touch, digital_product.aux,
                                    digital_product.sd_card, digital_product.ir])
    elif product_type == 2:
        headphone.type_of_socket = input('please enter type of socket: ')
        try:
            headphone.cable = bool(int(input('please say if headphone has cable, only 0 or 1: ')))
        except Exception as x:
            print(x)
        product_db.headphone([product_db.product(login.login_employee())[0][0],
                              headphone.type_of_socket, headphone.cable])
    elif product_type == 3:
        camera.quality_lenz = input('please enter quality lenz: ')
        camera.type_of_video = input('please enter type of video: ')
        camera.type_of_photo = input('please enter type of photo: ')
        try:
            camera.digital = bool(int(input('please say if camera is digital, only 0 or 1: ')))
        except Exception as x:
            print(x)
        product_db.camera([product_db.product(login.login_employee())[0][0],
                           camera.quality_lenz, camera.type_of_video, camera.type_of_photo, camera.digital])
    elif product_type == 4:
        home_appliance.watt = input('please enter watt: ')
        home_appliance.material = input('please enter material: ')
        product_db.home_appliance([product_db.product(login.login_employee())[0][0],
                                   home_appliance.watt, home_appliance.material])


def product_delete(username: list):
    df = get_products_employee(username)
    print(df)
    try:
        delete_item = int(input('please enter id that you want to delete: '))
    except Exception as x:
        print(x)
    else:
        # print(df['id'].values)
        if delete_item not in df['id'].values:
            print(f'{colorama.Fore.RED}invalid id!!!!!{colorama.Fore.RESET}')
        else:
            sure = input('are you sure(yes/no)? ')
            if sure == 'yes':
                print(delete_product(delete_item))
                df = df.drop(df[df['id'] == delete_item].index)
                print(df)


def product_update(username: list):
    df = get_products_employee(username)
    print(df)
    try:
        update_item = int(input('please enter id that you want to update: '))
    except Exception as x:
        print(x)
    else:
        pass


if __name__ == '__main__':
    create_table()
    customer = shop_mod.Customer()
    employee = shop_mod.Employee()
    admin = shop_mod.Admin()
    product = shop_mod.Product()
    digital_product = shop_mod.DigitalProduct()
    headphone = shop_mod.Headphone()
    camera = shop_mod.Camera()
    home_appliance = shop_mod.HomeAppliance()
    while True:
        schedule.run_pending()
        choose_sl = input('please choose signup or login (1 2):\n1. signup\n2. login\n>>>> ')
        if choose_sl == '1':
            choose_ec = input('please enter your way (1 2):\n1. define customer\n2. define employee\n>>>> ')
            if choose_ec == '1':
                customer_definition()
            elif choose_ec == '2':
                employee_definition()

            else:
                print('your choice invalid!!!!')
        elif choose_sl == '2':
            username = input('please enter your username: ')
            password = input('please enter your password: ')
            login = Login(username, password)
            if login.login():
                print(f'{colorama.Fore.GREEN}welcome {login.show_name()}\nyou are logged in{colorama.Fore.RESET}')

                if login.login_employee():
                    while True:
                        try:
                            choose_adu_e = int(input('please choose if you want:\n1. add product\n2. delete product\n'
                                                     '3. update product\n>>>>'))
                        except Exception as x:
                            print(x)
                        else:
                            if choose_adu_e == 1:
                                try:
                                    choose_type_product = int(input('please choose type of product:\n'
                                                                    '1. digital products'
                                                                    '\n2. headphone\n3. camera\n'
                                                                    '4. home appliance\n>>>>'))
                                except Exception as x:
                                    print(x)
                                else:
                                    if 0 < choose_type_product < 5:
                                        product_definition(choose_type_product)
                                    else:
                                        print('your choice is invalid!!!!!')

                            elif choose_adu_e == 2:
                                product_delete(login.login_employee())
                            elif choose_adu_e == 3:
                                product_update(login.login_employee())
                            else:
                                print('your choice is invalid!!!!!')
                        exit_person = input(f'{colorama.Fore.BLUE}if you want to log out,'
                                            f' type (log_out):{colorama.Fore.RESET} ')
                        if exit_person == 'log_out':
                            break
                        else:
                            continue
                elif login.login_customer():
                    print(get_all_products())
                    while True:
                        try:
                            buy = int(input(f"if you want to {colorama.Fore.GREEN}buy{colorama.Fore.RESET} "
                                            f"product please enter only product's id: "))
                            number_of_product = int(input("please enter number of your product: "))
                        except Exception as x:
                            print(x)
                        else:
                            factor.add_product_to_tf([login.login_customer()[0][0], buy, number_of_product])
                        basket = input('if you want to see your basket type (basket): ')

                        if basket == 'basket':
                            print(factor.get_basket(login.login_customer()[0][0]))
                        try:
                            delete_from_basket = int(input(f'if you want to '
                                                           f'{colorama.Fore.RED}delete{colorama.Fore.RESET} '
                                                           f'product from basket'
                                                           f' please enter only(id): '))
                        except Exception as x:
                            print(x)
                        else:
                            print(len(factor.get_basket(login.login_customer()[0][0])))
                            if -1 < delete_from_basket < len(factor.get_basket(login.login_customer()[0][0])):
                                factor.delete_product(login.login_customer()[0][0], delete_from_basket)
                            else:
                                print('invalid number!!!!!')
                        pay = input('if you want to pay please enter(pay): ')
                        exit_person = input(f'{colorama.Fore.BLUE}if you want to log out,'
                                            f' type (log_out):{colorama.Fore.RESET} ')
                        if exit_person == 'log_out':
                            break
                        if pay == 'pay':
                            paid = payment.pay()
                            if paid:
                                factor.paid(login.login_customer()[0][0], 1)
                                print(f'{colorama.Fore.GREEN}paid{colorama.Fore.RESET}')
                                factor.check_if_paid()
                            else:
                                continue

            else:
                print(f'{colorama.Fore.RED}your username or password wrong{colorama.Fore.RESET}')

        elif choose_sl == 'admin':

            try:
                choose_ad_sl = int(input('please choose signup or login (1 2):\n1. signup admin\n2. login_admin\n'
                                         '>>>> '))
            except Exception as x:
                print(x)

            else:
                if choose_ad_sl == 1:
                    admin_definition()
                elif choose_ad_sl == 2:
                    admin_login()
                else:
                    print('your choice invalid!!!!!')
            
        else:
            print('your choice invalid!!!!')
