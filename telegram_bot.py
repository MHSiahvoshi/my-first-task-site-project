import telebot
import csv
token_bot = '6661030292:AAGr3rBA9KP2dIgfuGvTEiagCOcL0jlD78U'
bot = telebot.TeleBot(token_bot)
list_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'all']
data_for_save = []


def read_admin_log():
    data = []
    try:
        with open('admin_data_log.csv', 'r', newline='\n', encoding='utf-8') as admin_csv:
            csv_reader = csv.reader(admin_csv)
            next(csv_reader)
            for row in csv_reader:
                data.append(row)
    except Exception as x:
        print(x)
    return data


def read_csv(number: str):
    request = number[1:]
    data = read_admin_log()

    if request == 'all':
        return data
    elif request in list_number[0: -2]:
        # request = number[1:]
        num = int(request)
        out = data[-1: -num - 1: -1]
        return out
    else:
        return None


def write_csv(operation: tuple):
    data = read_admin_log()
    result_flag = False
    global data_for_save
    for i in data:
        # print(i[2])
        if operation[0] == i[2]:
            # print('ok')
            temp = data.index(i)
            # print(temp)
            data[temp][-1] = operation[2]
            # print(data[temp][-1])/
            # print(data)
            result_flag = True
        elif operation[0] not in i[2]:
            result_flag = False

    if result_flag:
        data_for_save = data
        return True
    else:
        return False


def csv_save():

    try:
        with open('admin_data_log.csv', 'w', newline='\n', encoding='utf-8') as admin_csv:
            csv_writer = csv.writer(admin_csv)
            csv_writer.writerow(('id', 'full_name', 'username', 'password', 'phone', 'national_code', 'is_staff'))
            csv_writer.writerows(data_for_save)
    except Exception as x:
        print(x)


@bot.message_handler(commands=['start'], chat_types=['private'], func=lambda message: message.chat.id == 393402158)
def welcome(message):
    bot.send_message(message.chat.id, 'welcome to admin checker bot')


@bot.message_handler(commands=list_number, chat_types=['private'], func=lambda message: message.chat.id == 393402158)
def user_want(message):
    bot.send_message(message.chat.id, f'{read_csv(message.text)}')


@bot.message_handler(chat_types=['private'], func=lambda message: message.chat.id == 393402158)
def ac_or_re(message):
    if ':' in message.text:
        mes: str = message.text
        mess = mes.partition(':')
        # print(write_csv(mess))
        if write_csv(mess):
            csv_save()
            bot.send_message(message.chat.id, 'done')
        else:
            bot.send_message(message.chat.id, 'this username is not exists!!!!!')

    else:
        bot.send_message(message.chat.id, 'you should give me (username:0 or 1)')


if __name__ == '__main__':
    bot.infinity_polling()
