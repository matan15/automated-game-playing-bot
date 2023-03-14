from selenium import webdriver
import time
from selenium.webdriver.common.by import By

minutes = int(input("enter the time (in minutes) that you want that the game will work: "))

chrome_driver_path = input("enter your chrome driver path:\n")

driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = 'http://orteil.dashnet.org/experiments/cookie/'
driver.get(url)

cookie = driver.find_element(by=By.ID, value='cookie')
game_timeout = time.time() + 60 * minutes
buy_item_timeout = time.time() + 5

while True:
    cookie.click()
    store = driver.find_elements(by=By.CSS_SELECTOR, value='#store div')

    if time.time() >= buy_item_timeout:
        try:
            upgrade = [upgrade for upgrade in store if
                       upgrade.get_attribute('class') != 'grayed' and upgrade.get_attribute(
                           'class') != 'amount'][-1]
        except IndexError:
            pass
        else:
            upgrade_price = upgrade.text.splitlines()[0].split(' ')[2]
            money = driver.find_element(by=By.ID, value='money').text.replace(',', '')
            if int(money) > int(upgrade_price):
                print(f'upgrade price: {upgrade_price}\n money : {money}')
                upgrade.click()
        buy_item_timeout = time.time() + 5

    if time.time() >= game_timeout:
        break

cps = driver.find_element(by=By.ID, value='cps').text
print(cps)

driver.quit()