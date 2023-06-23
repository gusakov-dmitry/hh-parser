from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import pickle
import os

def hh_parser(x,y):
    if os.path.isfile('cookies'):
        options = Options()
        options.add_argument('--headless=new')
    
    df = pd.DataFrame(columns=['name', 'xp_req', 'remote', 'company', 'description'])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.get('https://hh.ru/applicant/negotiations?filter=all')

    try:
        for cookie in pickle.load(open('cookies', 'rb')):
            driver.add_cookie(cookie)
            
    except:
        time.sleep(60)
        pickle.dump(driver.get_cookies(), open('cookies', 'wb'))
        
    driver.refresh()

    for page in range(x,y):
        url = f'https://hh.ru/applicant/negotiations?filter=all&page={page}'
        driver.switch_to.new_window()
        driver.get(url)
        main = driver.window_handles
        table = driver
        table = table.find_element(By.CLASS_NAME, 'responses-table-tbody--GA5nMRIjZv1vAE3pRtUZ')
            
        for row in table.find_elements(By.CLASS_NAME, 'responses-table-row--nt2CTesRhLfQSD4j36rt'):
            
            try:
                row.find_element(By.CSS_SELECTOR, 'button').click()
                time.sleep(3)
                
                try:
                    iframe = driver.find_element(By.CLASS_NAME, 'chatik-integration-iframe-container')
                    iframe = iframe.find_element(By.CSS_SELECTOR, 'iframe')
                    driver.switch_to.frame(iframe)
                    link = driver.find_element(By.CLASS_NAME, 'k38b1ZG___bloko-link').get_attribute('href')
                    driver.switch_to.new_window()
                    driver.get(link)
                        
                    try:
                        df.loc[len(df)] = [
                        driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div/div[1]/h1/span').get_attribute('innerHTML'),
                        driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div/p[1]/span').get_attribute('innerHTML'),
                        driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div/p[2]').get_attribute('innerHTML'),
                        driver.find_element(By.CLASS_NAME, 'vacancy-company-name').get_attribute('innerHTML'),
                        driver.find_element(By.CLASS_NAME, 'vacancy-description').get_attribute('innerHTML')
                        ]
                        
                    except:
                        try:
                            driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[3]/div/button').click()
                            df.loc[len(df)] = [
                            driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div/div[1]/h1/span').get_attribute('innerHTML'),
                            driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div/p[1]/span').get_attribute('innerHTML'),
                            driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div/p[2]').get_attribute('innerHTML'),
                            driver.find_element(By.CLASS_NAME, 'vacancy-company-name').get_attribute('innerHTML'),
                            driver.find_element(By.CLASS_NAME, 'vacancy-description').get_attribute('innerHTML')
                            ]
                        
                        except:
                            continue
                                    
                except: 
                    continue
            
            except:
                continue
            
            driver.close()
            driver.switch_to.window(main[1])

        driver.close()
        driver.switch_to.window(main[0])
    
    return df