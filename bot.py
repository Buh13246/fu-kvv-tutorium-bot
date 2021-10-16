import selenium
import getpass
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from time import sleep

site_url = ''
wanted_tut_num = 0
username = input("Username: ")
passwort = getpass.getpass(prompt='Password: ', stream=None) 

elems = [];
list = [];

def chooseModule():
    global list
    global elems
    global site_url
    list = browser.find_elements_by_class_name('link-container')
    print("Please Choose!")
    for i in range(len(list)):
        print(str(i)+': '+list[i].find_element_by_xpath('./span').text)
    tmp = int(input("Please Choose: "))
    print('use: site_url=\''+list[tmp].get_attribute('href')+'\'')
    browser.get(list[tmp].get_attribute('href'))
    site_url = browser.find_element_by_class_name('icon-sakai--sakai-sections').find_element_by_xpath('./..').get_attribute('href')
    

def choose():
    global list
    global elems
    global wanted_tut_num
    list = browser.find_element_by_id('studentViewForm:studentViewSectionsTable:tbody_element').find_elements_by_tag_name("tr")
    print("Please Choose!")
    for i in range(len(list)-1):
        elems.append(browser.find_element_by_id('studentViewForm:studentViewSectionsTable:'+str(i)+':instructorName').find_elements_by_xpath('../../*'))
        print(str(i)+': '+elems[i][1].text+'('+elems[i][2].text+' '+elems[i][3].text+') '+elems[i][4].text)
    wanted_tut_num = input("Please Choose: ")


def getTut():
    global elems
    try:
        while(True):
            browser.get(site_url)
            try:
                el = browser.find_element_by_id('studentViewForm:studentViewSectionsTable:'+str(wanted_tut_num)+':_idJsp42')
                el.click()
                sleep(0.5)
                print("Link was avaible. Checking if it worked...")
                name = browser.find_element_by_id('studentViewForm:studentViewSectionsTable:'+str(wanted_tut_num)+':instructorName').find_elements_by_xpath('../../*')[0].text
                print("Got "+name)
                if name == browser.find_elements_by_class_name('studentSectionInfo')[0].text:
                    print("got the requestet tutorium")
                    print("thank you for using this tool. Philipp Wellner")
                    exit(0)
                else:
                    print("Sry it seems that it didnt work....")
                    exit(1)
            except Exception:
                print("waiting...")
                sleep(1)
                continue
    except KeyboardInterrupt:
        print("stopped")
                
    
options = Options();
options.add_argument("--headless");
browser = webdriver.Firefox(options=options)
browser.get('https://kvv.imp.fu-berlin.de/portal/login')
browser.find_element_by_id('username').send_keys(username)
browser.find_element_by_id('password').send_keys(passwort)
browser.find_element_by_name('_eventId_proceed').click()
sleep(1)
browser.get('https://kvv.imp.fu-berlin.de/portal')
if(site_url==''):
    chooseModule()
browser.get(site_url)
if wanted_tut_num == 0:
    choose()
    print("You chose "+str(wanted_tut_num))
