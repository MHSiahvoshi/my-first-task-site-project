try:
    import hashlib
    import mysql.connector
    import pandas as pd
    from sqlalchemy import create_engine
    import colorama
except Exception as x:
    print(x)
else:
    try:
        con = mysql.connector.connect(user='root', password='02081998', host='127.0.0.1', port=3306)
        connection = mysql.connector.connect(user='root', password='02081998', database='shop')
    except Exception as x:
        print(x)


def hash_data(data: str):
    sha = hashlib.sha256()
    sha.update(data.encode())
    hashed = sha.hexdigest()
    return hashed


def create_database():
    # global con
    check_db_flag = False
    cur = con.cursor()
    try:
        cur.execute('SHOW DATABASES')
    except Exception as x:
        print(x)
    list_dbs = cur.fetchall()

    for i in list_dbs:
        if 'shop' == i[0]:
            check_db_flag = True

    if check_db_flag:
        print('database was created!')
    else:
        cur.execute('CREATE DATABASE shop')
        print('database created......ok')


def create_table():
    create_database()
    check_table_flag = False
    # connect_to_mysql = mysql.connector.connect(user='root', password='02081998', host='localhost', database='shop')
    global connection
    cur = connection.cursor()
    try:
        cur.execute('SHOW TABLES')
    except Exception as x:
        print(x)
    lst_tables = cur.fetchall()

    for i in lst_tables:
        if 'person' == i[0]:
            check_table_flag = True
    if check_table_flag:
        print('table of person was created!')
    else:
        try:
            cur.execute("""
                CREATE TABLE person(
                id int auto_increment primary key ,
                name nvarchar(30) NOT NULL,
                family nvarchar(30) NOT NULL,
                username nvarchar(30) NOT NULL,
                password nvarchar(100) NOT NULL,
                email nvarchar(40) NOT NULL,
                phone nvarchar(14) NOT NULL,
                address nvarchar(100) NOT NULL
                )
            """)
        except Exception as x:
            print(x)
        else:

            print('table person created.....ok')

    for i in lst_tables:
        if 'customer' == i[0]:
            check_table_flag = True
    if check_table_flag:
        print('table of customer was created!')
    else:
        try:
            cur.execute("""
                    CREATE TABLE customer( 
                    customer_code int primary key ,                  
                    national_code BIGINT NOT NULL,
                    post_code BIGINT NULL,                    
                    foreign key (customer_code) references person(id)
                    )
                """)
        except Exception as x:
            print(x)
        else:

            print('table customer created.....ok')
    try:
        cur.execute("""
                CREATE TABLE IF NOT EXISTS employee(
                personally_code int primary key ,
                job_position nvarchar(50) NULL,
                salary int NOT NULL,
                job_guarantee int NULL ,
                foreign key (personally_code) references person(id)
                )
            """)
    except Exception as x:
        print(x)
    else:

        print('table employee created.....ok')
    try:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS admin(
        id tinyint auto_increment primary key,
        full_name nvarchar(40) NOT NULL,
        username nvarchar(50) NOT NULL,
        password varchar(100) NOT NULL,
        phone varchar(15) NOT NULL,
        national_code bigint NULL,
        is_staff bit default 0,
        super_admin bit default 0 
        )
        """)
    except Exception as x:
        print(x)
    else:
        print('table of admin created.....ok')
    admin_command = "INSERT INTO admin(full_name, username, password, phone, national_code, is_staff, super_admin) " \
                    "values (%s, %s, %s, %s, %s, %s, %s)"

    admin_data = ['Mohammadhossein Siahvoshi', 'MHS', hash_data('Mh$11051377'), '09304376517', 3920701623, 1, 1]
    try:
        cur.execute('select username, password from admin')
    except Exception as x:
        print(x)
    admin_check_db = cur.fetchall()
    try:
        # if not (admin_check_db[0][0] == 'MHS' and admin_check_db[0][1] == hash_data('Mh$11051377')):
        if len(admin_check_db) != 0:
            if "MHS" not in admin_check_db[0] and hash_data('Mh$11051377') not in admin_check_db[0]:
                cur.execute(admin_command, tuple(admin_data))
        else:
            cur.execute(admin_command, tuple(admin_data))
    except Exception as x:
        print(x)
    else:
        connection.commit()
        print('admin created.....ok')

    try:
        cur.execute("""
        create table if not exists product(
        id int auto_increment primary key ,
        product_code char(9) not null,
        product_name nvarchar(50) not null,
        barcode varchar(20) not null,
        product_type nvarchar(40) not null,
        company nvarchar(40) not null,
        production date not null,
        price float not null,
        guarantee int not null,
        address_company nvarchar(100),
        description nvarchar(100) null,
        employee_id int ,
        foreign key (employee_id) references employee(personally_code)
        )
        """)
    except Exception as x:
        print(x)
    else:

        print('table of product created.....ok')
    try:
        cur.execute("""
            create table if not exists digital_product(
            dp_id int primary key ,
            cpu nvarchar(30) not null,
            ram nvarchar(30) not null,
            internal_storage nvarchar(30) not null,
            dimention_lcd nvarchar(30) not null,
            graphic nvarchar(30)  null,
            color nvarchar(20) not null,
            charger nvarchar(30),
            os nvarchar(20),
            type_sound nvarchar(20),
            touch bit default 0,
            aux bit default 0,
            sd_card bit default 0,
            ir bit default 0,
            foreign key (dp_id) references product(id)
            )
            """)
    except Exception as x:
        print(x)
    else:

        print('table of digital_product created.....ok')
    try:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Headphone(
        h_id int PRIMARY KEY,
        type_of_socket nvarchar(30) null,
        cable bit default 0,
        FOREIGN KEY (h_id) REFERENCES product(id)
        )
        """)

    except Exception as x:
        print(x)

    else:
        print('table of headphone created.....ok')

    try:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS camera(
        c_id int PRIMARY KEY,
        quality_lenz nvarchar(50) not null,
        type_of_video nvarchar(50) not null,
        type_of_photo nvarchar(50) not null,
        digital bit default 0,
        FOREIGN KEY (c_id) REFERENCES product(id)
        )
        """)

    except Exception as x:
        print(x)

    else:
        print('table of camera created.....ok')

    try:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS homeAppliance(
        ha_id int PRIMARY KEY,
        watt nvarchar(20) not null,
        material nvarchar(30),
        FOREIGN KEY (ha_id) REFERENCES product(id)
        )
        """)

    except Exception as x:
        print(x)
    else:
        print('table of homeAppliance created.....ok')

    try:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS factor(
        f_id int PRIMARY KEY,
        customer_code int,
        total int not null,
        factor_date char(10) not null,
        FOREIGN KEY (customer_code) REFERENCES customer(customer_code)
        )
        """)
    except Exception as x:
        print(x)
    else:
        print('table of factor created.....ok')


def check_username(username: str):
    username_data = []
    try:
        if len(username) != 0:
            username_data.append(username)
        else:
            return False
    except Exception as x:
        print(x)
    # connect_to_mysql = mysql.connector.connect(user='root', password='02081998', host='localhost', database='shop')

    username_command = "SELECT username FROM person WHERE username = %s"
    cur = connection.cursor()
    try:
        cur.execute(username_command, tuple(username_data))
        username_response = cur.fetchall()
    except Exception as x:
        print(x)
    else:
        for i in username_response:
            if len(i) != 0:

                print('نام کاربری تکراری است!!!!!\nنام کاربری دیگری انتخاب کنید.')
                return False
        else:
            return True


def import_customer(data: list):
    try:
        national_code = data.pop(-2)
        post_code = data.pop(-1)
    except Exception as x:
        print(x)

    # data.append(0)
    person_data = tuple(data)

    person_command = "INSERT INTO person(name, family, username, password, email, phone, address)" \
                     " VALUES (%s, %s, %s, %s, %s, %s, %s)"
    customer_command = "INSERT INTO customer(customer_code, national_code, post_code) VALUES (%s, %s, %s)"
    try:
        # connection = mysql.connector.connect(user='root', password='02081998', database='shop')
        connection
    except Exception as x:
        print(x)
    else:
        cur = connection.cursor()
        customer_username = []
        try:
            cur.execute(person_command, person_data)
            connection.commit()

            customer_username.append(data[2])

            cur.execute("SELECT id FROM person WHERE username = %s", tuple(customer_username))
            customer_code = cur.fetchall()[0][0]

            customer_data = [customer_code, national_code, post_code]
            cur.execute(customer_command, tuple(customer_data))
            connection.commit()
        except Exception as x:
            print(x)
        else:
            return 'customer added'


def import_employee(data: list):
    employee_username = []
    try:
        job_position = data.pop(-3)
        salary = data.pop(-2)
        job_guarantee = data.pop(-1)
    except Exception as x:
        print(x)

    # data.append(0)
    person_data = tuple(data)
    person_command = "INSERT INTO person(name, family, username, password, email, phone, address)" \
                     " VALUES (%s, %s, %s, %s, %s, %s, %s)"
    employee_command = "INSERT INTO employee(personally_code, job_position, salary, job_guarantee)" \
                       " VALUES (%s, %s, %s, %s)"
    try:
        # connection = mysql.connector.connect(user='root', password='02081998', database='shop')
        connection
    except Exception as x:
        print(x)
    else:
        cur = connection.cursor()

        try:
            cur.execute(person_command, person_data)
            connection.commit()
            employee_username.append(data[2])
            cur.execute("SELECT id FROM person WHERE username = %s", tuple(employee_username))
            personally_code = cur.fetchall()[0][0]

            employee_data = (personally_code, job_position, salary, job_guarantee)
            cur.execute(employee_command, employee_data)
            connection.commit()
        except Exception as x:
            print(x)
        else:
            return 'employee added'


class Login:
    def __init__(self, username: str, password: str):
        self._username = [username]
        self._password = [password]

    def login(self):

        hashed = hash_data(self._password[0])

        temp = [[self._username[0]], [hashed]]

        # connection
        username_command = "SELECT username FROM person WHERE username = %s"
        password_command = "SELECT password FROM person WHERE password = %s"
        cur = connection.cursor()
        try:
            cur.execute(username_command, tuple(temp[0]))
            username_response = cur.fetchall()
            cur.execute(password_command, tuple(temp[1]))
            password_response = cur.fetchall()

        except Exception as x:
            print(x)
        else:

            try:
                for i in range(len(username_response)):
                    if len(username_response[i]) != 0:
                        for j in range(len(password_response)):
                            if password_response[j][0] == hashed:
                                return True
                        else:
                            return False
                else:
                    return False
            except Exception as x:
                print(x)

    def login_customer(self):
        customer_command = 'SELECT id FROM person WHERE username = %s'
        customer_data = tuple(self._username)
        try:
            # connect_to_mysql = mysql.connector.connect(user='root', password='02081998', database='shop')
            connection
        except Exception as x:
            print(x)
        else:
            cur = connection.cursor()
            try:
                cur.execute(customer_command, customer_data)
                customer_response = cur.fetchall()
                cur.execute('SELECT customer_code FROM customer WHERE customer_code = %s', customer_response[0])
                response = cur.fetchall()
                if len(response[0]) != 0:
                    return response
                else:
                    return False

            except:
                pass

    def login_employee(self):
        employee_command = 'SELECT id FROM person WHERE username = %s'
        employee_data = tuple(self._username)
        try:
            connection
            # connect_to_mysql = mysql.connector.connect(user='root', password='02081998', database='shop')
        except Exception as x:
            print(x)
        else:
            cur = connection.cursor()
            try:
                cur.execute(employee_command, employee_data)
                employee_response = cur.fetchall()
                cur.execute('SELECT personally_code FROM employee WHERE personally_code = %s', employee_response[0])
                response = cur.fetchall()
                if len(response[0]) != 0:
                    return response
                else:
                    return None

            except:
                pass

    def show_name(self):
        try:
            connection
        except Exception as x:
            print(x)
        else:
            cur = connection.cursor()
            cur.execute('SELECT name FROM person WHERE username = %s', tuple(self._username))
            data = cur.fetchall()
            return data[0][0]


def admin_signup_db(data: list):
    admin_check_command = 'SELECT username FROM admin'
    admin_command = 'INSERT INTO admin(full_name, username, password, phone, national_code, is_staff, super_admin)' \
                    ' VALUES (%s, %s, %s, %s, %s, %s, %s)'

    for c in data:
        c.remove(c[0])
        c.append(0)
    # print(data)

    admin_data = tuple(data)

    try:

        cur = connection.cursor()
        cur.execute(admin_check_command)
        admin_check_response = cur.fetchall()
        # print(admin_check_response)
        temp = list(map(lambda y: [p for p in y][0], admin_check_response))
        # print(temp)
        if len(admin_check_response) != 0:
            for i in admin_data:
                if i[1] in temp:
                    # print('exists')
                    continue
                else:
                    cur.execute(admin_command, tuple(i))
                    connection.commit()
                    # print('not exists')
                    continue
        else:
            cur.executemany(admin_command, admin_data)
            connection.commit()

    except Exception as x:
        print(x)


def admin_login_db(data: list):
    admin_username_command = 'SELECT id FROM admin WHERE username = %s'
    admin_password_command = 'SELECT password FROM admin WHERE password = %s'
    admin_username_data = [data[0]]
    admin_password_data = [data[1]]

    try:
        connection
        # connection = mysql.connector.connect(user='root', password='02081998', database='shop')
    except Exception as x:
        print(x)
    else:
        cur = connection.cursor()
        try:
            cur.execute(admin_username_command, tuple(admin_username_data))
            admin_username_response = cur.fetchall()

        except Exception as x:
            print(x)
        else:
            if len(admin_username_response[0]) == 1:
                # print('username ok')
                try:
                    cur.execute(admin_password_command, tuple(admin_password_data))
                    admin_password_response = cur.fetchall()

                except Exception as x:
                    print(x)
                else:
                    if admin_password_response[0][0] == data[1]:
                        return True
                    else:
                        return False
            else:
                return False


class Products:
    def __init__(self, code, name, barcode, product_type, company, production, price,
                 guarantee, address_company, description):
        self._code = code
        self._name = name
        self._barcode = barcode
        self._product_type = product_type
        self._company = company
        self._production = production
        self._price = price
        self._guarantee = guarantee
        self._address_company = address_company
        self._description = description

    def product(self, user: list):
        product_command = 'INSERT INTO product(product_code, product_name, barcode, product_type, company, production,' \
                          ' price, guarantee, address_company, description, employee_id) ' \
                          'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        product_data = (self._code, self._name, self._barcode, self._product_type, self._company,
                        self._production, self._price,
                        self._guarantee, self._address_company, self._description, user[0][0])

        cur = connection.cursor()
        try:
            cur.execute(product_command, product_data)
            connection.commit()
            cur.execute('SELECT id FROM product WHERE product_code = %s', tuple([self._code]))
            id_response = cur.fetchall()
        except Exception as x:
            print(x)
        else:
            return id_response

    def digital_product(self, data: list):
        digital_product_command = 'INSERT INTO digital_product(dp_id, cpu, ram, internal_storage, dimention_lcd,' \
                                  ' graphic, color, charger, os, type_sound, touch, aux, sd_card, ir) VALUES (%s, %s,' \
                                  ' %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cur = connection.cursor()
        try:
            cur.execute(digital_product_command, tuple(data))
            connection.commit()
        except Exception as x:
            print(x)
        else:
            print('digital product added')

    def headphone(self, data: list):
        headphone_command = 'INSERT INTO headphone(h_id, type_of_socket, cable) VALUES (%s, %s, %s)'

        cur = connection.cursor()
        try:
            cur.execute(headphone_command, tuple(data))
            connection.commit()
        except Exception as x:
            print(x)
        else:
            print('headphone added')

    def camera(self, data: list):
        camera_command = 'INSERT INTO camera(c_id, quality_lenz, type_of_video, type_of_photo, digital)' \
                         ' VALUES (%s, %s, %s, %s, %s)'
        cur = connection.cursor()
        try:
            cur.execute(camera_command, tuple(data))
            connection.commit()
        except Exception as x:
            print(x)
        else:
            print('camera added')

    def home_appliance(self, data: list):
        home_appliance_command = 'INSERT INTO homeappliance(ha_id, watt, material) VALUES (%s, %s, %s)'
        cur = connection.cursor()
        try:
            cur.execute(home_appliance_command, tuple(data))
            connection.commit()
        except Exception as x:
            print(x)
        else:
            print('home appliance added')


def get_products_employee(username: list):
    try:
        engine = create_engine('mysql+mysqlconnector://root:02081998@localhost/shop')

        df = pd.read_sql(f'SELECT id, product_code, product_name,'
                         f' price FROM product WHERE employee_id = {username[0][0]}', engine)
    except Exception as x:
        print(x)
    else:
        return df


def delete_product(number: int):
    # print(number)
    temp = []
    temp.append(number)
    # print(temp)
    check_digital_product = 'SELECT dp_id FROM digital_product WHERE dp_id = %s'
    check_headphone = 'SELECT h_id FROM headphone WHERE h_id = %s'
    check_camera = 'SELECT c_id FROM camera WHERE c_id = %s'
    check_home_appliance = 'SELECT ha_id FROM homeappliance WHERE ha_id = %s'
    delete_command = 'DELETE FROM product WHERE id = %s'
    cur = connection.cursor()
    try:
        cur.execute(check_digital_product, tuple(temp))
        digital_product_response = cur.fetchall()
        # print(digital_product_response)
        cur.execute(check_headphone, tuple(temp))
        headphone_response = cur.fetchall()
        # print(headphone_response)
        cur.execute(check_camera, tuple(temp))
        camera_response = cur.fetchall()
        # print(camera_response)
        cur.execute(check_home_appliance, tuple(temp))
        home_appliance_response = cur.fetchall()
        # print(home_appliance_response)
        if len(digital_product_response) != 0:
            # print('ok')
            try:
                cur.execute('DELETE FROM digital_product WHERE dp_id = %s', tuple(temp))
                connection.commit()
            except Exception as x:
                print(x)

        elif len(headphone_response) != 0:
            try:
                cur.execute('DELETE FROM headphone WHERE h_id = %s', tuple(temp))
                connection.commit()
            except Exception as x:
                print(x)

        elif len(camera_response) != 0:
            try:
                cur.execute('DELETE FROM camera WHERE c_id = %s', tuple(temp))
                connection.commit()
            except Exception as x:
                print(x)
        elif len(home_appliance_response) != 0:
            try:
                cur.execute('DELETE FROM homeappliance WHERE ha_id = %s', tuple(temp))
                connection.commit()
            except Exception as x:
                print(x)

    except Exception as x:
        print(x)
    else:
        try:
            cur.execute(delete_command, tuple(temp))
            connection.commit()
        except Exception as x:
            print(x)
        else:
            return 'item deleted'


def get_all_products():
    out = []
    get_products_command = ('SELECT product.id, product.product_name, product.product_type, product.company,' \
                            ' product.price, digital_product.cpu, digital_product.ram FROM product JOIN' \
                            ' digital_product ON product.id = digital_product.dp_id',
                            'SELECT product.id, product.product_name, product.product_type, product.company,' \
                            ' product.price, headphone.type_of_socket, headphone.cable FROM product JOIN' \
                            ' headphone ON product.id = headphone.h_id',
                            'SELECT product.id, product.product_name, product.product_type, product.company,' \
                            ' product.price, camera.type_of_video, camera.type_of_photo FROM product JOIN' \
                            ' camera ON product.id = camera.c_id',
                            'SELECT product.id, product.product_name, product.product_type, product.company,' \
                            ' product.price, homeappliance.watt, homeappliance.material FROM product JOIN' \
                            ' homeappliance ON product.id = homeappliance.ha_id'
                            )

    cur = connection.cursor()
    try:
        for i in get_products_command:
            cur.execute(i)
            response = cur.fetchall()
            out.extend(response)

        df = pd.DataFrame(out, columns=['id', 'name', 'type', 'company', 'price', 'detail', 'detail'])
                                        # f'{colorama.Fore.LIGHTBLUE_EX}name{colorama.Fore.RESET}',
                                        # f'{colorama.Fore.LIGHTBLUE_EX}type{colorama.Fore.RESET}',
                                        # f'{colorama.Fore.LIGHTBLUE_EX}company{colorama.Fore.RESET}',
                                        # f'{colorama.Fore.LIGHTBLUE_EX}price{colorama.Fore.RESET}',
                                        # f'{colorama.Fore.LIGHTBLUE_EX}detail{colorama.Fore.RESET}',
                                        # f'{colorama.Fore.LIGHTBLUE_EX}detail{colorama.Fore.RESET}'])

    except Exception as x:
        print(x)
    else:
        return df


def get_product_detail(number: list):
    product_command = 'SELECT product_code, product_name, price FROM product WHERE id = %s'
    cur = connection.cursor()
    try:
        cur.execute(product_command, tuple(number))
        response = cur.fetchall()
    except Exception as x:
        print(x)
    else:
        return response


def register_factor(data):
    print(data)
    factor_command = 'INSERT INTO factor(customer_code, total, factor_date) VALUES (%s, %s, %s)'
    cur = connection.cursor()
    try:
        cur.executemany(factor_command, tuple(data))
        connection.commit()
    except Exception as x:
        print(x)
