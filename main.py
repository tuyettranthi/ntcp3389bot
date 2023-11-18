import telebot
import datetime
import time
import os,sys,re
import subprocess
import requests
import datetime

bot_token = '6542193363:AAGhRQ5K_egCR6kJ8oF5-q_Msve-CJLoKKk' 
bot = telebot.TeleBot(bot_token)
processes = []
ADMIN_ID = '6347230217'

def TimeStamp():
    now = str(datetime.date.today())
    return now

@bot.message_handler(commands=['getkey'])
def startkey(message):
    bot.reply_to(message, text='VUI LÒNG ĐỢI TRONG GIÂY LÁT!')
    
    # Replace the key with your desired link
    key = "Liên Hệ /admin Để Lấy"
    
    text = f'''
- LINK LẤY KEY {TimeStamp()} LÀ: {key} -
- KHI LẤY KEY XONG, DÙNG LỆNH /key <key> ĐỂ TIẾP TỤC -
    '''
    bot.reply_to(message, text)



@bot.message_handler(commands=['key'])
def key(message):
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP KEY.')
        return

    user_id = message.from_user.id

    key = message.text.split()[1]
    username = message.from_user.username
    expected_key = key = "TQN"
    if key == expected_key:
        bot.reply_to(message, 'KEY HỢP LỆ. BẠN ĐÃ ĐƯỢC PHÉP SỬ DỤNG LỆNH /spam.')
    else:
        bot.reply_to(message, 'KEY KHÔNG HỢP LỆ.')



@bot.message_handler(commands=['superspam'])
def superspam(message):
    user_id = message.from_user.id
    if not os.path.exists(f"./vip/{user_id}.txt"):
        bot.reply_to(message, 'Bạn chưa đăng ký VIP, vui lòng liên hệ admin')
        return

    fo = open(f"./vip/{user_id}.txt")
    data = fo.read().split("|")
    qua_khu = data[0]
    ngay_hien_tai = datetime.date.today()

    # Convert the date strings to datetime objects for comparison
    qua_khu_date = datetime.datetime.strptime(qua_khu, '%Y-%m-%d').date()

    so_ngay = (ngay_hien_tai - qua_khu_date).days

    if so_ngay < 0:
        bot.reply_to(message, 'Key VIP cài vào ngày khác')
        return

    hethan_date = datetime.datetime.strptime(data[1], '%Y-%m-%d').date()

    if ngay_hien_tai > hethan_date:
        bot.reply_to(message, 'Key VIP đã hết hạn. Vui lòng liên hệ admin.')
        os.remove(f"./vip/{user_id}.txt")
        return

    # Check command arguments
    if len(message.text.split()) != 3:
        bot.reply_to(message, 'Vui lòng nhập đúng cú pháp: /superspam [số điện thoại] [số lần spam]')
        return

    lap = message.text.split()[2]
    if not lap.isnumeric():
        bot.reply_to(message, "Sai dữ kiện !!!")
        return

    phone_number = message.text.split()[1]
    if not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$", phone_number):
        bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
        return

    if phone_number in ["0365956335"]:
        bot.reply_to(message, "Spam cái đầu buồi tao huhu")
        return

    file_path = os.path.join(os.getcwd(), "spamsms.py")
    process = subprocess.Popen(["python", file_path, phone_number, lap])
    processes.append(process)
    bot.reply_to(message, f'🚀 Gửi Yêu Cầu Tấn Công Thành Công 🚀 \n+ Bot 👾: @AltsformeBot \n+ Số Tấn Công 📱: [ {phone_number} ]\n+ Lặp lại : {lap}\n+ Chủ sở hữu 👑: @Akunbg\n+ Zalo : Akunbg\n+ Key : vip')

# The rest of your code...
  
  
@bot.message_handler(commands=['spam'])
def spam(message):
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP SỐ ĐIỆN THOẠI ')
        return
    if len(message.text.split()) == 2:
        bot.reply_to(message, 'Thiếu dữ kiện !!!')
        return
    lap = message.text.split()[2]
    if lap.isnumeric():
      if not (int(lap) > 0 and int(lap) <= 40):
        bot.reply_to(message,"Vui lòng spam trong khoảng 1-40. Nếu nhiều hơn mua vip để sài :))")
        return
    else:
      bot.reply_to(message,"Sai dữ kiện !!!")
      return
    phone_number = message.text.split()[1]
    if not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",phone_number):
        bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
        return

    if phone_number in ["0365956335"]:
        # Số điện thoại nằm trong danh sách cấm
        bot.reply_to(message,"Spam cái đầu buồi tao huhu")
        return

    file_path = os.path.join(os.getcwd(), "sms.py")
    process = subprocess.Popen(["python", file_path, phone_number, lap])
    processes.append(process)
    bot.reply_to(message, f'🚀 Gửi Yêu Cầu Tấn Công Thành Công 🚀 \n+ Bot 👾: @AltsformeBot \n+ Số Tấn Công 📱: [ {phone_number} ]\n+ Lặp lại : {lap}\n+ Chủ sở hữu 👑: @Akunbg\n+ Zalo : Akunbg\n+ Key : free')



@bot.message_handler(commands=['help'])
def help(message):
    help_text = '''
Danh sách lệnh:
- /getkey: Lấy key để sử dụng các lệnh.
- /key {key}: Kiểm tra key và xác nhận quyền sử dụng các lệnh.
- /spam {số điện thoại} {so lan}: Gửi tin nhắn SMS Call.
- /superspam {số điện thoại} {so lan}: Gửi tin nhắn SMS Call.(vip)
- /help: Danh sách lệnh.
- /mua : Mua Bot
- /status (admin)
- /restart (admin)
- /stop (admin)
- /them (admin)
- /admin
'''
    bot.reply_to(message, help_text)
    
# status
@bot.message_handler(commands=['status'])
def status(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    process_count = len(processes)
    bot.reply_to(message, f'Số quy trình đang chạy: {process_count}.')



# khoir dong lai bot
@bot.message_handler(commands=['restart'])
def restart(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    bot.reply_to(message, 'Bot sẽ được khởi động lại trong giây lát...')
    time.sleep(2)
    python = sys.executable
    os.execl(python, python, *sys.argv)


# stop chuongw trinhf
@bot.message_handler(commands=['stop'])
def stop(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    bot.reply_to(message, 'Bot sẽ dừng lại trong giây lát...')
    time.sleep(2)
    bot.stop_polling()

    
@bot.message_handler(commands=['them'])
def them(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    
    # Check if there are enough command arguments
    command_args = message.text.split()
    if len(command_args) != 4:
        bot.reply_to(message, 'Vui lòng cung cấp đầy đủ thông tin.')
        return

    idvip = command_args[1]
    ngay = command_args[2]
    hethan = command_args[3]

    # Validate date formats
    try:
        datetime.datetime.strptime(ngay, '%Y-%m-%d')
        datetime.datetime.strptime(hethan, '%Y-%m-%d')
    except ValueError:
        bot.reply_to(message, 'Định dạng ngày không hợp lệ. Sử dụng định dạng YYYY-MM-DD.')
        return

    # Create the directory for VIP files if it doesn't exist
    vip_directory = './vip'
    os.makedirs(vip_directory, exist_ok=True)

    # Write user information to a file
    vip_file_path = f"{vip_directory}/{idvip}.txt"
    if os.path.exists(vip_file_path):
        bot.reply_to(message, f'User {idvip} đã tồn tại trong danh sách VIP.')
        return

    with open(vip_file_path, "w") as fii:
        fii.write(f"{ngay}|{hethan}")

    bot.reply_to(message, f'Thêm Thành Công {idvip} vào danh sách VIP.')

    # Write user information to a file
    vip_file_path = f"./vip/{idvip}.txt"
    if os.path.exists(vip_file_path):
        bot.reply_to(message, f'User {idvip} đã tồn tại trong danh sách VIP.')
        return

    with open(vip_file_path, "w") as fii:
        fii.write(f"{ngay}|{hethan}")

    bot.reply_to(message, f'Thêm Thành Công {idvip} vào danh sách VIP.')

if __name__ == "__main__":
    bot.polling()

@bot.message_handler(commands=['admin'])
def admin_info(message):
    # Thay thế các giá trị sau bằng thông tin liên hệ của bạn
    facebook_url = "https://www.facebook.com/USER.TUQUANGNAM"
    zalo_url = "https://zalo.me/tuquangnam"
    zalo_box = "zalo.me/g/hhkxlz379a"

    admin_message = f"Thông tin liên hệ của Admin:\n\nFacebook: {facebook_url}\nZalo: {zalo_url}\nBox Zalo: {zalo_box}"

    bot.reply_to(message, admin_message)



# mua
@bot.message_handler(commands=['mua'])
def mua(message):
    reply_text = 'Giá cả của các gói dịch vụ tất cả đều chát admin:\n\n'
    reply_text += '- Gói /spam: 20k/1 tháng\n'
    reply_text += '- Gói /spam: 60k/6 tháng\n'
    reply_text += '- Gói /spam: 350k/1 năm\n'
    reply_text += '- Gói /spam: 555k/ Không giới hạn\n'
    reply_text += '- Mua source bot giống bot 150k Không giới hạn\n'
    bot.reply_to(message, reply_text)


# lenh lo 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Lệnh không hợp lệ. Vui lòng sử dụng lệnh /help để xem danh sách lệnh.')

bot.polling()
