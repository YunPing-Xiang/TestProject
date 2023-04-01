import uiautomator2 as u2
import yaml
from apscheduler.schedulers.background import BlockingScheduler


class AndroidUi:
    def __init__(self):
        with open(file='../TestCaseYaml/AndroidUI.yaml', mode='r', encoding='utf-8') as e:
            result = yaml.load_all(e.read(), yaml.FullLoader)
        self.ls = []
        for i in result:
            self.ls.append(i)
        if self.ls[0][''] == 'connect_mode':
            self.d = u2.connect_usb(self.ls[0]['connect_address'])
        else:
            self.d = u2.connect_wifi(self.ls[0]['connect_address'])
        self.d.app_start(self.ls[0]['package_name'])

    def android_ui(self):
        driver = self.d
        for z in range(1, len(self.ls)):
            dic = self.ls[z]
            position_mode = dic['android_ui']['position_mode']
            event = dic['android_ui']['event']
            if position_mode == 'text' and event == 'click':
                driver(text=dic['android_ui']['element']).click()
            elif position_mode == 'text' and event == 'set_text':
                driver(text=dic['android_ui']['element']).set_text()
            elif position_mode == 'xpath' and event == 'set_text':
                driver.xpath(dic['android_ui']['element']).set_text()
            elif position_mode == 'xpath' and event == 'click':
                driver.xpath(dic['android_ui']['element']).click()
            elif position_mode == 'xpath' and event == 'set_text':
                driver(description=dic['android_ui']['element']).set_text()
            elif position_mode == 'xpath' and event == 'click':
                driver(description=dic['android_ui']['element']).click()
            else:
                print('None')

    def run(self):
        if self.ls[0]['TimingSwitch'] == 'off':
            scheduler = BlockingScheduler(timezone='Asia/Shanghai')
            time = self.ls[0]['Timeing']
            scheduler.add_job(self.android_ui(), trigger='cron', hour=time)
            scheduler.start()
        else:
            self.android_ui()



