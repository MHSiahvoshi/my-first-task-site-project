try:
    from datetime import *
    import hashlib
    import random
except Exception as x:
    print(x)


class Person:
    def __init__(self):
        self._name = ''
        self._family = ''
        self._user_name = ''
        self._password = ''
        self._email = ''
        self._phone = ''
        self._address = ''

        self._alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
        self._alpha_upper = self._alpha_lower.upper()
        self._numerics = '0123456789'
        self._special_char = '!@#$%^&*()_+-=/*?\\\'\".'

    # --------------------set get name-----------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        value.strip()
        if 2 <= len(value) <= 30 and value.isalpha():
            self._name = value
        else:
            self._name = None
            print('invalid name!!!!!')

    # --------------------set get family-----------------
    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value: str):
        # value.strip()
        if 2 <= len(value) <= 30 and value.isalpha():
            self._family = value
            # check_parameters(True)
        else:
            self._family = None
            print('invalid family!!!!!')

    # --------------------set get user_name-----------------

    @property
    def username(self):
        return self._user_name

    @username.setter
    def username(self, value: str):
        value.strip()
        if len(value) != 0 and len(value) >= 6 and value.isalnum():
            self._user_name = value
        else:
            self._user_name = None
            print('invalid username!!!!!')

    # --------------------set get password-----------------

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        flag_alpha_lower = False
        flag_alpha_upper = False
        flag_numerics = False
        flag_special_char = False
        value.strip()
        if len(value) >= 8:
            for c in value:
                if c in self._alpha_lower:
                    flag_alpha_lower = True
                elif c in self._alpha_upper:
                    flag_alpha_upper = True
                elif c in self._numerics:
                    flag_numerics = True
                elif c in self._special_char:
                    flag_special_char = True
            if flag_alpha_lower and flag_alpha_upper and flag_numerics and flag_special_char:
                sha = hashlib.sha256()
                sha.update(value.encode())
                hashed = sha.hexdigest()
                self._password = hashed
                # check_parameters(True)
            else:
                self._password = None
                print('invalid password!!!!!')
        else:
            self._password = None
            print('invalid password!!!!!')

    # --------------------set get email-----------------

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        if (0 <= len(value) <= 50) and ('.com' or '.COM') in value and '@' in value:
            self._email = value
        else:
            self._email = None
            print('invalid email!!!!!')

    # --------------------set get phone-----------------

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value: str):
        if value.startswith('+98'):
            if len(value) == 13:
                self._phone = value
            else:
                print('invalid phone!!!!!')
        elif value.startswith('0'):
            if len(value) == 11:
                self._phone = value
                # check_parameters(True)
            else:
                self._phone = None
                print('invalid phone!!!!!')
        else:
            self._phone = None
            print('invalid phone!!!!!')

    # --------------------set get address-----------------

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value: str):
        if 0 < len(value) <= 100:
            self._address = value
            # check_parameters(True)
        else:
            self._address = None
            print('invalid address')


class Customer(Person):
    def __init__(self):
        super().__init__()
        # self._customer_code = ''
        self._national_code = 0
        self._post_code = 0

    # --------------------set get national_code-----------------
    @property
    def national_code(self):
        return self._national_code

    @national_code.setter
    def national_code(self, value: int):
        if len(str(value)) <= 10 and str(value).isdigit():
            self._national_code = value
            # check_parameters(True)
        else:
            self._national_code = None
            print('invalid national_code!!!!!')

    # --------------------set get post_code-----------------
    @property
    def post_code(self):
        return self._post_code

    @post_code.setter
    def post_code(self, value: int):
        if len(str(value)) == 10 and str(value).isdigit():
            self._post_code = value
            # check_parameters(customer_post_flag=True)
        else:
            self._post_code = None
            print('invalid post_code!!!!!')


class Employee(Person):
    def __init__(self):
        super().__init__()
        # self._personally_code = ''
        self._job_position = ''
        self._salary = 0
        self._job_guarantee = 0

    # --------------------set get job_position-----------------

    @property
    def job_position(self):
        return self._job_position

    @job_position.setter
    def job_position(self, value: str):
        if len(value) <= 80:
            self._job_position = value
            # check_parameters(True)
        else:
            self._job_position = None
            print('invalid job_position!!!!!')

    # --------------------set get salary-----------------

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: int):
        if isinstance(value, int):        # ????????????????????
            self._salary = value
            # check_parameters(employee_salary_flag=True)
        else:
            self._salary = None
            print('invalid salary!!!!!')

    # --------------------set get salary-----------------

    @property
    def job_guarantee(self):
        return self._job_guarantee

    @job_guarantee.setter
    def job_guarantee(self, value: int):
        if isinstance(value, int):           # ???????????????????????
            self._job_guarantee = value
            # check_parameters(True)
        else:
            self._job_guarantee = None
            print('invalid job_guarantee!!!!!')


class Admin:
    def __init__(self):
        self._admin_full_name = ''
        self._admin_user = ''
        self._admin_pass = ''
        self._admin_phone = ''
        self._admin_national_code = 0
        self._is_staff = False
        self._super_admin = False

    @property
    def admin_full_name(self):
        return self._admin_full_name

    @admin_full_name.setter
    def admin_full_name(self, value: str):
        if len(value) <= 40:
            self._admin_full_name = value
        else:
            print('invalid full name!!!!!')

    @property
    def admin_user(self):
        return self._admin_user

    @admin_user.setter
    def admin_user(self, value: str):
        if 0 < len(value) < 50 and not value.isdigit():
            self._admin_user = value
        else:
            print('invalid admin username!!!!!')

    @property
    def admin_pass(self):
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, value: str):
        if 8 <= len(value) < 50:
            # password = bytes(value)
            sha = hashlib.sha256()
            sha.update(value.encode())
            hashed = sha.hexdigest()
            self._admin_pass = hashed
            # print(self._admin_pass)
        else:
            print("admin's password must be 8 or higher characters!!!!!")

    @property
    def admin_phone(self):
        return self._admin_phone

    @admin_phone.setter
    def admin_phone(self, value: str):
        if (value.startswith('+98') or value.startswith('0')) and len(value) <= 13:
            self._admin_phone = value
        else:
            print('invalid admin phone!!!!!')

    @property
    def admin_national_code(self):
        return self._admin_national_code

    @admin_national_code.setter
    def admin_national_code(self, value: int):
        if value >= 0:
            self._admin_national_code = value
        else:
            print('invalid national code!!!!!')


class Product:
    def __init__(self):
        self._product_name = ''
        # self._product_code = ''
        self._barcode = ''
        self._product_type = ''
        self._company = ''
        self._production = ''
        self._price = 0.0
        self._guarantee = 0
        self._address_company = ''
        self._description = ''

    # ---------------set get name--------------------
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value: str):
        # global time_second_p, time_min_p
        if len(value) <= 50 and not value.isdigit():
            self._product_name = value
            # time_second_p = datetime.now()
            # time_min_p = datetime.now()

        else:
            print('نام کالا نباید بیشتر از 50 کاراکتر باشد.')

    # ---------------set get product_code--------------------

    def product_code(self):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chara = random.choice(alpha)
        product_code = chara + self.product_name[0: 2] + self._company[0: 2] + str(random.randint(1000, 9999))
        return product_code

    # ---------------set get barcode--------------------

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value: str):
        if value.isalnum() or value.isdigit():
            self._barcode = value
        else:
            print('بارکد نامعتبر است.')

    # --------set get type----------------

    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value: str):
        if len(value) <= 40:
            self._product_type = value
        else:
            print('نوع محصول حداکثر باید 40 کاراکتر باشد.')

    # ------------set get company----------------

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value: str):
        if len(value) <= 40:
            self._company = value
        else:
            print('نام شرکت سازنده حداکثر باید 40 کاراکتر باشد.')
    # --------------set get production--------------

    @property
    def production(self):
        return self._production

    @production.setter
    def production(self, value: str):
        # global production_date
        temp = value.split('-')
        if len(temp[0]) == 4 and len(temp[1]) == 2 and len(temp[2]) == 2 and value[4] == value[7] == '-':
            self._production = value
            # production_date = tuple(value)
        else:
            print('فرمت ورودی تاریخ باید به شکل زیر باشد:\n yyyy-mm-dd')

    # --------------set get price--------------

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if len(str(value)) != 0:
            self._price = value
        else:
            print('شما باید عدد مبلغ را وارد کنید.')

    @property
    def guarantee(self):
        return self._guarantee

    @guarantee.setter
    def guarantee(self, value: int):
        if value > 0:
            self._guarantee = value
        else:
            print('لطفا زمان گارانتی را وارد کنید.')

    # ----------set get company_address-------------------

    @property
    def address_company(self):
        return self._address_company

    @address_company.setter
    def address_company(self, value: str):
        if len(value) <= 100:
            self._address_company = value
        else:
            print('آدرس باید حداکثر 100 کاراکتر باشد.')

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        if len(value) < 100:
            self._description = value


class DigitalProduct(Product):
    def __init__(self):
        super().__init__()
        self._cpu = ''
        self._ram = ''
        self._internal_storage = ''
        self._dimention_lcd = ''
        self._graphic = ''
        self._touch = False
        self._charger = ''
        self._aux = False
        self._sd_card = True
        self._ir = False
        self._color = ''
        self._os = ''
        self._type_sound = ''

    @property
    def graphic(self):
        return self._graphic

    @graphic.setter
    def graphic(self, value: str):
        if 0 <= len(value) < 30:
            self._graphic = value
        else:
            print('لطفا توضیحات کارت گرافیک را وارد کنید.')

    @property
    def touch(self):
        return self._touch

    @touch.setter
    def touch(self, value: bool):
        self._touch = value

    @property
    def charger(self):
        return self._charger

    @charger.setter
    def charger(self, value: str):
        if 0 < len(value) < 30:
            self._charger = value
        else:
            print('لطفا توضیحات شارژر را وارد کنید.')

    @property
    def aux(self):
        return self._aux

    @aux.setter
    def aux(self, value: bool):
        self._aux = value

    @property
    def sd_card(self):
        return self._sd_card

    @sd_card.setter
    def sd_card(self, value: bool):
        self._sd_card = value

    @property
    def ir(self):
        return self._ir

    @ir.setter
    def ir(self, value: bool):
        self._ir = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: str):
        if 0 < len(value) < 20 and not value.isdigit():
            self._color = value
        else:
            print('رنگ باید کمتر از 20 کاراکتر باشد.')

    @property
    def os(self):
        return self._os

    @os.setter
    def os(self, value: str):
        if (0 < len(value) < 20) and not value.isdigit():
            self._os = value
        else:
            print('invalid os!!!!!')

    @property
    def type_sound(self):
        return self._type_sound

    @type_sound.setter
    def type_sound(self, value: str):
        if (0 < len(value) < 20) and not value.isdigit():
            self._type_sound = value
        else:
            print('invalid type sound!!!!!')

    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self, value: str):
        if 0 < len(value) < 30:
            self._cpu = value
        else:
            print('لطفا توضیحات cpu را وارد کنید.')

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, value: str):
        if 0 < len(value) < 30:
            self._ram = value
        else:
            print('لطفا توضیحات ram را وارد کنید.')

    @property
    def internal_storage(self):
        return self._internal_storage

    @internal_storage.setter
    def internal_storage(self, value: str):
        if 0 < len(value) < 30:
            self._internal_storage = value
        else:
            print('لطفا توضیحات حافظه داخلی یا هارد را وارد کنید.')

    @property
    def dimention_lcd(self):
        return self._dimention_lcd

    @dimention_lcd.setter
    def dimention_lcd(self, value: str):
        if 0 < len(value) < 30:
            self._dimention_lcd = value
        else:
            print('لطفا ابعاد نمایشگر را وارد کنید.')


class Laptop(DigitalProduct):
    def __init__(self):
        super().__init__()
        pass


class SmartPhone(DigitalProduct):
    def __init__(self):
        super().__init__()
        pass


class SmartWatch(DigitalProduct):

    def __init__(self):
        super().__init__()
        pass


class Headphone(Product):
    def __init__(self):
        super().__init__()
        self._cable = False
        self._type_of_socket = ''

    @property
    def cable(self):
        return self._cable

    @cable.setter
    def cable(self, value: bool):
        self._cable = value

    @property
    def type_of_socket(self):
        return self._type_of_socket

    @type_of_socket.setter
    def type_of_socket(self, value: str):
        if len(value) < 30:
            self._type_of_socket = value
        else:
            print('نوع سوکت نمیتواند بیشتر از 30 کاراکتر باشد.')


class Camera(Product):
    def __init__(self):
        super().__init__()
        self._quality_lenz = ''
        self._type_of_video = ''
        self._type_of_photo = ''
        self._digital = False

    @property
    def quality_lenz(self):
        return self._quality_lenz

    @quality_lenz.setter
    def quality_lenz(self, value: str):
        if len(value) <= 50:
            self._quality_lenz = value
        else:
            print('invalid quality lenz!!!!!')

    @property
    def type_of_video(self):
        return self._type_of_video

    @type_of_video.setter
    def type_of_video(self, value: str):
        if len(value) <= 50:
            self._type_of_video = value
        else:
            print('invalid type of video!!!!!')

    @property
    def type_of_photo(self):
        return self._type_of_photo

    @type_of_photo.setter
    def type_of_photo(self, value: str):
        if len(value) <= 50:
            self._type_of_photo = value
        else:
            print('invalid type of photo!!!!!')

    @property
    def digital(self):
        return self._digital

    @digital.setter
    def digital(self, value: bool):

        self._digital = value


class HomeAppliance(Product):
    def __init__(self):
        super().__init__()
        self._watt = ''
        self._material = ''

    @property
    def watt(self):
        return self._watt

    @watt.setter
    def watt(self, value: str):
        if (0 < len(value) < 20) and value.isalnum():
            self._watt = value
        else:
            print('invalid watt!!!!!')

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value: str):
        if (0 < len(value) < 30) and not value.isdigit():
            self._watt = value
        else:
            print('invalid material!!!!!')


if __name__ == '__main__':
    print('This is a module please run main!!!')
