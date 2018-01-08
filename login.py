from selenium import webdriver
import requests

#---------------------------------TESTING--------------------------------------#
def web_site_online(url='http://www.facebook.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        # HTTP errors are not raised by default, this statement does that
        req.raise_for_status()
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False
#-------------------------------------------------------------------------------#
browser  = webdriver.Chrome()

browser.get('http://172.16.1.3:8090/')

user = browser.find_element_by_name('username')
user.send_keys('cs2015021104')
pas  = browser.find_element_by_name('password')
pas.send_keys('hexa123')
pas.submit()



