import requests
from selenium import webdriver
import time;
import sys


class Mi:

    def __init__(self, input_id, input_pw):
        self.id = input_id
        self.pw = input_pw

    def main(self):
        options = webdriver.ChromeOptions()
        # chrome 參數
        options.add_argument("--no-sandbox")
        options.add_argument('disable-infobars')
        driver = webdriver.Chrome(chrome_options=options)
        # 小米帳號登入 URL
        url = 'https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Fbuy.mi.com%2Ftw%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252Ftw%252Findex.html%26sign%3DNWQwMWFkYmFmYTNjYzJjOWE4OTAwMWM4ZDEyODFhYWVlYzZlNTY0Zg%2C%2C&sid=mi_xiaomitw&_locale=zh_TW&checkSafePhone=false'
        code = requests.get(url)  # 小米帳號登入 URL
        if code.status_code == requests.codes.ok:  # 判斷小米網站是否存活
            print("無私分享，只求有一份中工作謀求生活\n開始執行")
            try:
                driver.get(url)  # 小米帳號登入 URL
                # 登入小米帳號
                driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.id)
                driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(self.pw)
                driver.find_element_by_xpath('//*[@id="login-button"]').click()
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="J_curtain"]/div/div[1]/div[2]/a').click()
                count = 0
                while (count < 1000):
                    driver.find_element_by_xpath('//*[@id="sec_1"]/div/div/ul/li/ol/li[3]/a').click()
                    time.sleep(0.5)
                    driver.find_element_by_xpath('//*[@id="sec_1"]/div/div/ul/li/ol/li[2]/a').click()
                    count = count + 1
                    print("無私分享，只求有一份中工作謀求生活\n執行次數 %d" % count)
                    time.sleep(0.5)
                    driver.refresh()
                driver.quit()
                print("個無私分享，只求有一份中工作謀求生活\n結束")

            except Exception as e:
                print(e)
        else:
            print("網站掛了")


if __name__ == "__main__":
    mi = Mi(sys.argv[1], sys.argv[2])
    mi.main()
