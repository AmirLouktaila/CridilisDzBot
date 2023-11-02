import telebot
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui

bot = telebot.TeleBot("token")

@bot.message_handler(commands=['start'])
def welcome(message):
    mes = '''
CridilisDzBot مرحبا بك في بوت 
😊يمكنكم إعادة تفعيل خدمة الأنترنت لمدة 96 ساعة إضافية
✨فقط ادخل الرقم وكلمة السر وسيتم مباشر تفعيل العرض👌
😎كيف تستعمل البوت :
🤷‍♂️NumberPhone:Password
اكتب رقم الهاتف وكلمة السر كما موضح اعلاه
    '''
    bot.send_message(message.chat.id, mes)

@bot.message_handler(func=lambda message: True)
def talk(message):
    bot.send_message(message.chat.id,'انتظر قليلا...')
    proxy_ip_port = 'host:port'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--proxy-server=http://{proxy_ip_port}')   
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://client.algerietelecom.dz/ar')
    except:
       driver.quit()
       bot.send_message(message.chat.id,'للاسف حدث خطأ اعد المحاولة لاحقا')
    sleep(1)
    x = 393
    y = 21230
    pyautogui.moveTo(x, y)
    pyautogui.write('username')
    sleep(1)
    pyautogui.press('tab')
    pyautogui.write('password')
    pyautogui.press('enter')
    def pe(ep):
        input_text = ep
        if ":" in input_text:
            parts = input_text.split(":")
            if len(parts) == 2:
                before = parts[0].strip()
                after = parts[1].strip()
                return [before, after]
            else:
                print("Text should contain only one colon.")
        else:
            print("Text does not contain a colon.")

    info_login = pe(message.text)
    number_phone = driver.find_element(By.ID, 'nd')
    number_phone.send_keys(info_login[0])
    password = driver.find_element(By.ID, 'password')
    password.send_keys(info_login[1])  # Use info_login[1] for the password
    sleep(1)
    login = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/div/form/input[4]')
    login.submit()
    driver.get('https://client.algerietelecom.dz/ar/RechargementSecours')
    login = driver.find_element(By.XPATH, '/html/body/section[3]/form/center[2]/button')
    login.submit()
    print('Done')
    t_element = driver.find_element(By.XPATH, '/html/body/section[3]/div/div/center/div/h4')
    t = t_element.text
    bot.send_message(message.chat.id,t)
    driver.quit()

        
   


    # Start the bot polling
bot.polling()
