from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
import uuid
import time
from ctypes import windll


def scrape_followers(list_of_urls, quantity):
    driver = webdriver.Chrome(service=Service('./chromedriver.exe'))
    try:
        driver.get('https://x.com/login')
        input("\nLOG IN TO ACCOUNT X.com, AFTER SUCCESSFULLY LOGGING IN, PRESS ENTER")

        for url in list_of_urls:
            driver.get(url)
            time.sleep(3)
            print(f"Webpage: {driver.title}\n")
            
            for i in range(quantity):
                if i % 10 == 0:
                    driver.execute_script(f"window.scrollBy(0, {30*i})")
                    time.sleep(2)
                
                try:
                    user_name_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[{i+1}]/div/div/button/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]')))
                    user_name_text = user_name_element.text
                    image_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[{i+1}]/div/div/button/div/div[1]/div/div/div[2]/div/div[2]/div/a/div[3]/div/div[2]/div/img')))
                    
                    try:
                        image_url = image_element.get_attribute('src').replace('normal', '400x400')
                        image_name = str(uuid.uuid4()) + '.jpg'
                        image_path = os.path.join('./Avatars', image_name)
                        
                        img_data = requests.get(image_url).content
                        with open(image_path, 'wb') as handler:
                            handler.write(img_data)
                        
                        print(f"{user_name_text} | {image_name}")
                        
                        with open("nicknames.txt", 'a', encoding='utf-8') as f:
                            f.write(f"{user_name_text}:{image_name}\n")

                    except Exception as e:
                        print(user_name_text, "No picture", e)
                    
                except Exception as e:
                    print(f"Error finding element at index {i}: {e}")
                    break

                print(f"{i+1} profiles downloaded\n")
        
    finally:
        driver.quit()
        print(f"\n{quantity*len(list_of_urls)} Nicknames and avatars saved\n")

if __name__ == '__main__':
    windll.kernel32.SetConsoleTitleW('Avatar and Nickname Parser | by https://t.me/dmtrcrypto')
    print("\n\n\nTG Channel - https://t.me/dmtrcrypto")
    print("TG Channel - https://t.me/dmtrcrypto")
    print("TG Channel - https://t.me/dmtrcrypto\n")

    quantity = int(input("\n\nEnter the number of profiles to parse for each specified profile :\n\n"))

    with open('X_accounts.txt', 'r') as f:
        list_of_urls = [url.strip() for url in f.readlines()]

    if not os.path.exists("Avatars"):
        os.makedirs("Avatars")

    scrape_followers(list_of_urls, quantity)
