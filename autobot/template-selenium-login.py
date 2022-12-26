from selenium import webdriver
from helium import *
import base64
import time
import ddddocr
def open_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    # options.add_argument('--proxy-server=socks5://127.0.0.1:1080')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(chrome_optinotallow=options)
    driver.maximize_window()

    set_driver(driver)
    go_to("http://127.0.0.1:8000/login/")
    write("admin","账号")
    write("admin","密码")
    code_base64 = driver.find_element_by_css_selector("#code + img").get_attribute('src').split("data:image/png;base64,")[-1]
    img = base64.b64decode(code_base64)
    # 识别验证码
    ocr = ddddocr.DdddOcr(show_ad=False)
    code = ocr.classification(img)
    # code = res['pic_str']
    write(code, '验证码')
    time.sleep(3)
    click(Button('登 录'))
    driver.get_screenshot_as_file("test.png")


    time.sleep(5)
    kill_browser()
if __name__ == '__main__':
    open_chrome()
