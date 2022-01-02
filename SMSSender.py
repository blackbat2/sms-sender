import time,os,sys
try:
    from colorama import *
except ImportError:
    os.system('pip install colorama')
    from colorama import *
try:
    import nexmo
except ImportError:
    os.system('pip install nexmo')
    import nexmo
from nexmo import Sms
from nexmo.sms import Sms
class SMSSender(object):
    def __init__(self):
        self.success = 0
        self.fail = 0
        self.phonenumbers = []
        self.fails = []
        self.successes = []
    def Intro(self):
        Logo = '''
        ____                           ____  __  __ ____ ____                 _
|  _ \ ___ _   _  ___ ___      / ___||  \/  / ___/ ___|  ___ _ __   __| | ___ _ __
| |_) / __| | | |/ __/ _ \ ____\___ \| |\/| \___ \___ \ / _ | '_ \ / _` |/ _ | '__|
|  __/\__ | |_| | (_| (_) |________) | |  | |___) ___) |  __| | | | (_| |  __| |
|_|   |___/\__, |\___\___/     |____/|_|  |_|____|____/ \___|_| |_|\__,_|\___|_|
        |___/'''
        print(f'{Back.BLACK}{Fore.MAGENTA}{Logo}')
        print(F"{Back.BLACK}{Fore.GREEN}\n1)(MASS) BULK SMS{Back.BLACK}{Fore.YELLOW}\n2)SINGLE SMS{Back.BLACK}{Fore.WHITE}\n3)Nexmo Settings\n")
        Choice = input('=>: ')
        if int(Choice)== 1:
            self.MassSMSSender()
        if int(Choice)== 2:
            self.SingleSMSSender()
        if int(Choice)== 3:
            self.Settings()
    def Settings(self):
        if os.path.isfile('Settings.txt')==False:
            APIKey = input(f"{Back.BLACK}{Fore.CYAN}API KEY => : ")
            APISecret = input(f"{Back.BLACK}{Fore.BLUE}API SECRET => : ")
            open('Settings.txt','w',errors='ignore',encoding='utf-8').write(f'{APIKey}|{APISecret}')
            print(f'{Back.MAGENTA}{Fore.BLACK}Settings Done Succesfully ')
            self.Intro()
        if os.path.isfile('Settings.txt')==True:
            print('There Are Already Settings you want Change Them y/n \n')
            Choice = input('=>: ')
            if Choice == 'n':
                self.Intro()
            if Choice == 'y':
                APIKey = input(f"{Back.BLACK}{Fore.CYAN}API KEY => : ")
                APISecret = input(f"{Back.BLACK}{Fore.BLUE}API SECRET => : ")
                open('Settings.txt','w',errors='ignore',encoding='utf-8').write(f'{APIKey}|{APISecret}')
                print(f'{Back.MAGENTA}{Fore.BLACK}Settings Done Succesfully ')
                self.Intro()
    def SingleSMSSender(self):
        if os.path.isfile('Settings.txt')==False:
            print('Please Setup Settings and Get Back')
            time.sleep(3)
            self.Settings()
        else:
            APIs = open('Settings.txt','r',errors='ignore',encoding='utf-8').read()
            APIs = APIs.replace('\n','')
            APIKey = APIs.split('|')[0]
            APISecret = APIs.split('|')[1]
            Name = input('Name or Phone you Should Send From => :')
            To = input('Phone you Should Send To => :')
            Letter = input('Give me Your Message File')
            Letter = open(Letter,'r',errors='ignore',encoding='utf-8').read()
            Letter = Letter.replace('{To}',To)
            client = nexmo.Client(key=APIKey, secret=APISecret)
            sms = Sms(client)
            sms.send_message({"from": Name,"to": To,"text": f'{Letter}','type': 'unicode',})
    def MassSMSSender(self):
        if os.path.isfile('Settings.txt')==False:
            print('Please Setup Settings and Get Back')
            time.sleep(3)
            self.Settings()
        else:
            APIs = open('Settings.txt','r',errors='ignore',encoding='utf-8').read()
            APIs = APIs.replace('\n','')
            APIKey = APIs.split('|')[0]
            APISecret = APIs.split('|')[1]
            Name = input('Name or Phone you Should Send From => :')
            To = input('SMS Leads you Should Send To => :')
            To = open(To,'r',errors='ignore',encoding='utf-8').read()
            Letter = input('Give me Your Message File')
            Letter = open(Letter,'r',errors='ignore',encoding='utf-8').read()
            client = nexmo.Client(key=APIKey, secret=APISecret)
            sms = Sms(client)
            for _To in To:
                Letter = Letter.replace('{To}',To)
                sms.send_message({"from": Name,"to": _To,"text": f'{Letter}','type': 'unicode'})
SMSSenderTool = SMSSender()
SMSSenderTool.Intro()
