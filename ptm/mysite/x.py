
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
 
option = webdriver.ChromeOptions()

option.add_experimental_option('excludeSwitches', ['enable-automation'])
 
# option.add_argument("--proxy-server=127.0.0.1:8080")
# 设置无头加载
# option.add_argument('--headless')
# 设置无图片模式
# prefs = {"profile.managed_default_content_settings.images": 2}
# option.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()
status = driver.get("https://login.taobao.com/member/login.jhtml")
print(status)
# pass
# 删除原来的cookie
driver.delete_all_cookies()
# cookie = "thw=cn; cna=yFJuFf/jBmkCAbRt3g+PNikw; v=0; t=ce6433b7d755f402b91d17670f77a2ef; sg=819; csg=d16db728; existShop=MTU2MTYwNzg5MQ%3D%3D; tracknick=%5Cu6843%5Cu6843520328; lgc=%5Cu6843%5Cu6843520328; dnk=%5Cu6843%5Cu6843520328; tg=0; mt=ci=9_1; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie21=VT5L2FSpdet1FS8C2gIFaQ%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTaGduh3ZQTWQ%3D%3D&tag=8&lng=zh_CN; _nk_=%5Cu6843%5Cu6843520328; _tb_token_=3ab35ef7b6b31; isg=BNrad6CZU8E-BN6SQyYSGTTBK4A8o13CtG3R4uRTgm04V3qRzJuu9aClIyNLgtZ9; l=bBNeS67nv7dTPyOoBOCanurza77OSIRYYuPzaNbMi_5LE6T_Z8bOkYnakF96Vj5RsUYB4ATie6p9-etkZ"
# c = cookie.split(';')
# ck = {}
# for i in c:
#     key = i.split('=')[0].strip()
#     val = i.split('=')[1].strip()
#     ck.setdefault(key, val)
# 携带cookie打开
# driver.add_cookie(ck)
 
 

user = driver.find_element_by_id("TPL_username_1")
user.send_keys('用户名')
password = driver.find_element_by_id("TPL_password_1")
 
password.send_keys('密码')
# 设置显示等待
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'nc_1__scale_text')))
bb = driver.find_element_by_id("nc_1__scale_text")
# ActionChains(driver).click_and_hold(bb).perform()
# for x in range(258):
#     ActionChains(driver).drag_and_drop_by_offset(
#         xoffset=x, yoffset=0).perform()
#     time.sleep(0.02)
bar_element = driver.find_element_by_id('nc_1__scale_text')
ActionChains(driver).drag_and_drop_by_offset(bar_element, 258, 0).perform()
time.sleep(0.5)
ActionChains(driver).release().perform()
# 点击提交按钮
butt = driver.find_element_by_id('J_SubmitStatic')
butt.click()
 
driver.get("https://www.taobao.com")
# 设置显示等待
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, 'search-combobox-input-wrap')))
search = driver.find_element_by_class_name('search-combobox-input')
search.send_keys("苏宁易购")
 
search_butt = driver.find_element_by_class_name('btn-search')
search_butt.click()
print(driver.page_source)

