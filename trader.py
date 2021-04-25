from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

def main(url):
    if url == True:
        start()
    else:
        trade(url)

options = None
driver = None
def start():
    # 設定此 option 可讓 chrome 記住已登入帳戶，成功後可以省去"#登入帳戶"的程式碼
    global options
    options = webdriver.ChromeOptions()
    options.add_argument(r"--user-data-dir=C:\\Users\\Hexplode\\AppData\\Local\\Google\\Chrome\\User Data\\Default")  # 可透過chrome://version/ 找到
    global driver
    driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

def trade(url):
    driver.get(url)
    
    try:
        #防止上线但是没有加入购物车按钮的刷新小循环
        waiting = True
        while waiting:
            #WebDriverWait(driver, 50).until(
            #    expected_conditions.presence_of_element_located((By.CLASS_NAME, "site_btn origncheckbutton orderReplenish"))
            #)
            time.sleep(0.1)
            try:
                # 放入購物車
                cart = driver.find_element_by_xpath("(//button[text()='加入24h購物車'])[2]")
                WebDriverWait(driver, 20).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, "(//button[text()='加入24h購物車'])[2]"))
                )
                cart.click()
                #等待0.3秒基本上都能进购物车
                time.sleep(0.3)
                break
            except:
                #WebDriverWait(driver, 10).until(
                #    expected_conditions.presence_of_element_located((By.CLASS_NAME, "site_btn origncheckbutton orderReplenish"))
                #)
                driver.refresh()

        # 前往購物車
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.ID, "ico_cart"))
        )
        driver.find_element_by_id('ico_cart').click()

        # 下一步
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.ID, "nextStep"))
        )    
        button = driver.find_element_by_id("nextStep")
        driver.execute_script("arguments[0].click();", button)

        # 送出訂單，要使用 JS (execute_script) 點擊
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[@id='btnSubmit']"))
        )    
        button = driver.find_element_by_xpath("//a[@id='btnSubmit']")
        driver.execute_script("arguments[0].click();", button)
    except Exception as e:
        print(e.__class__.__name__)

if __name__ == "__main__": 
    main(url)