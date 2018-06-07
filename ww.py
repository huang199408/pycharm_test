import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('network.proxy.type', 1)
firefox_profile.set_preference('network.proxy.http', '119.28.194.66')
firefox_profile.set_preference('network.proxy.http_port', 8888)  # int
firefox_profile.update_preferences()
driver = webdriver.Firefox()
html = driver.get('https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20')

num = 1

# while num <= 2:
#     num = num + 1
#     time.sleep(2)
#     if driver.find_element_by_link_text("加载更多"):
#         driver.find_element_by_link_text("加载更多").click()
#     else:
#         break

number = 1
list = driver.find_elements_by_xpath(".//*[@id='content']/div/div[1]/div/div[4]/div/a")
handle = driver.current_window_handle
while number <= len(list):
    driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/div[4]/div/a["+str(number)+"]").click()
    windows = driver.window_handles
    number += 1
    for window in windows:
        if window != handle:
            driver.switch_to_window(windows[1])
            time.sleep(3)
            print(driver.title)
            driver.close()
            driver.switch_to.window(handle)


