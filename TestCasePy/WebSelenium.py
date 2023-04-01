from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from apscheduler.schedulers.background import BlockingScheduler
from selenium import webdriver
import yaml


class BossSelenium:
    def __init__(self):
        with open(file='../TestCaseYaml/Webselenium.yaml', mode='r', encoding='utf-8') as e:
            self.result = yaml.load_all(e.read(), yaml.FullLoader)
        option = webdriver.ChromeOptions()
        option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
        self.driver = webdriver.Chrome(options=option)

    # 解析yaml文件，完成对应的selenium操作
    def boss_selenium(self):
        driver = self.driver
        re_li = []
        for i in self.result:
            re_li.append(i)
        driver.get(re_li[0]['Url'])
        for j in range(1, len(re_li)):
            le = re_li[j]
            Position = le['BossSelenium']['PositionMode']
            Event = le['BossSelenium']['PositionMode']
            TimeSwicth = le['BossSelenium']['TimeSwitch']
            if TimeSwicth == 'off':
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((le['BossSelenium']['PositionMode'], le['BossSelenium']['Element'])))
                if Position == 'By.XPATH' and Event == 'Click':
                    driver.find_element(le['BossSelenium']['PositionMode'], le['BossSelenium']['Element']).click()
                elif Position == 'By.LINK_TEXT' and Event == 'send_key':
                    driver.find_element(le['BossSelenium']['PositionMode'], le['BossSelenium']['Element']).send_keys()
                elif Position == 'By.XPATH' and Event == 'Get':
                    driver.find_element(le['BossSelenium']['PositionMode'], le['BossSelenium']['Element']).get_attribute()
                elif Position == 'By.SCRIPT' and Event == 'None':
                    driver.execute_script(le['BossSelenium']['Element'])
                else:
                    print('None')
            else:
                if Position == 'By.XPATH' and Event == 'Click':
                    driver.find_element(le['BossSelenium']['PositionMode'], le['BossSelenium']['Element']).click()
                elif Position == 'By.LINK_TEXT' and Event == 'send_key':
                    driver.find_element(le['BossSelenium']['PositionMode'], le['BossSelenium']['Element']).send_keys()
                elif Position == 'By.XPATH' and Event == 'Get':
                    driver.find_element(le['BossSelenium']['PositionMode'], le['BossSelenium']['Element']).get_attribute()
                elif Position == 'By.SCRIPT' and Event == 'None':
                    driver.execute_script(le['BossSelenium']['Element'])
                else:
                    print('None')

    # 运行方式选择，是否使用定时任务运行
    def run_time(self):
        with open(file='../TestCaseYaml/Webselenium.yaml', mode='r', encoding='utf-8') as e:
            result = yaml.load_all(e.read(), yaml.FullLoader)
        ls = []
        for i in result:
            ls.append(i)
        if ls[0]['TimingSwitch'] is not None:
            scheduler = BlockingScheduler(timezone='Asia/Shanghai')
            time = ls[0]['Timeing']
            scheduler.add_job(self.boss_selenium, trigger='cron', hour=time)
            scheduler.start()
        else:
            self.boss_selenium()
