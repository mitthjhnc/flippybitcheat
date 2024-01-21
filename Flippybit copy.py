import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

driver.get('https://flippybitandtheattackofthehexadecimalsfrombase16.com/')

time.sleep(6)
ActionChains(driver)\
    .send_keys(keys.Keys.ENTER)\
    .perform()
        

tappers = driver.find_elements(By.CSS_SELECTOR, ".tapper")[::-1]
for rounds in range(0,10000):   
    attack_value = int(driver.find_element(By.CSS_SELECTOR, "#attackValue").text, 16)
    if attack_value != 0:     
        for i in range(0, len(tappers)):
            if int(f'{str(bin(attack_value))[2:]:0>8}'[i]):
                tappers[i].click()     
    enemy = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.enemy:not(.under-attack)')))
    enemy_num_in_bin = f'{str(bin(int(enemy.text, 16)))[2:]:0>8}'
    for i in range(0, len(tappers)):
        if int(enemy_num_in_bin[i]):
            tappers[i].click()
time.sleep(5)

