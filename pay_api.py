# import requests
#
# # مشخصات حساب کاربری درگاه زرین پال
# merchant_id = 'your_merchant_id'
# api_key = 'your_api_key'
# callback_url = 'your_callback_url'
#
# # آدرس اتصال به درگاه زرین پال
# base_url = 'https://sandbox.zarinpal.com/pg/rest/WebGate/'
#
# # مبلغ تراکنش به ریال
# amount = 10000
#
# # توضیحات تراکنش
# description = 'Test payment'
#
# # آدرس بازگشت به وبسایت شما بعد از پرداخت
# return_url = 'your_return_url'
#
# # آدرس صفحه‌ی پرداخت در درگاه زرین پال
# payment_url = base_url + 'PaymentRequest.json'
#
# # اطلاعات پرداخت
# data = {
#     'MerchantID': merchant_id,
#     'Amount': amount,
#     'Description': description,
#     'CallbackURL': callback_url,
#     'ReturnURL': return_url,
# }
#
# # ارسال درخواست به درگاه زرین پال
# response = requests.post(payment_url, json=data)
#
# # بررسی وضعیت درخواست
# if response.status_code == 200:
#     result = response.json()
#     if result['Status'] == 100:
#         # اتصال موفق، انتقال به صفحه‌ی پرداخت
#         print('Payment URL:', result['Authority'])
#         payment_redirect_url = f'https://sandbox.zarinpal.com/pg/StartPay/{result["Authority"]}'
#         print('Redirect to payment page:', payment_redirect_url)
#     else:
#         # خطا در اتصال
#         print('Error:', result['Status'])
# else:
#     # خطا در اتصال به درگاه زرین پال
#     print('Connection Error:', response.status_code)

# import flask
# app = flask.Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return 'please pay'
#
#
# if __name__ == '__main__':
#     app.run()

# -*- coding: utf-8 -*-

def pay():
    return 1
