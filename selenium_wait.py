import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# set options for headless browser
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://rehabs.com/'
xpath = '/html/body/div[1]/div[2]/header/section/div/div[3]/div/button/span'

'''
Method 1: Using `time.sleep()`

This would not be a recommended approach without some way to throw an exception for timeout. A general pattern for halting further exection until an element is found.
'''
def find_with_sleep(url, xpath):
    response = driver.get(url)
    elem = driver.find_element(By.XPATH, xpath)
    while not elem:
        print('element not found...')
        # # [deprecated]
        # elem = driver.find_element_by_xpath(modal_xpath)
        elem = driver.find_element(By.XPATH, xpath)
        time.sleep(10)
    print(elem.text == 'Helpline Information')
    driver.quit()


'''
Method 2: Using implicit wait

By implicitly waiting, the WebDriver polls the DOM for a certain duration when trying to find any element. This can be useful when certain elements on the webpage are not available immediately and need some time to load. Implicit waiting for elements to appear is disabled by default and will need to be manually enabled on a per-session basis. Mixing explicit waits and implicit waits is not recommended and will cause unintended consequences, namely waits sleeping for the maximum time even if the element is available or condition is true. For example, setting an implicit wait of 10 seconds and an explicit wait of 15 seconds could cause a timeout to occur after 20 seconds.

An implicit wait is to tell WebDriver to poll the DOM for a certain amount of time when trying to find an element or elements if they are not immediately available. The default setting is 0, meaning disabled. Once set, the implicit wait is set for the life of the session.
'''
def find_with_implicit_wait(url, xpath):
    driver.implicitly_wait(10)
    driver.get(url)
    elem = driver.find_element(By.XPATH, xpath)
    print(elem.text == 'Helpline Information')
    driver.quit()



'''
Method 3: Using explicit wait

When you use an explicit wait, the WebDriver is directed to wait until a certain condition occurs before proceeding with executing the code. In effect, you halt program execution, or freeze the thread, until the condition you specify has resolved. The condition is called with a certain frequency until the timeout of the wait is elapsed. This means that for as long as the condition returns a falsy value, it will keep trying and waiting.

Explicit wait is more intelligent, but can only be applied against elements you've specified. However, it is an improvement on implicit wait since it allows the program to pause for dynamically loaded elements. With implicit waits, the browser will always wait for the same amount of time before trying to find any element

Some methods used in conjuction with explicit waits:

alertIsPresent()
elementSelectionStateToBe()
elementToBeClickable()
elementToBeSelected()
frameToBeAvaliableAndSwitchToIt()
invisibilityOfTheElementLocated()
invisibilityOfElementWithText()
presenceOfAllElementsLocatedBy()
presenceOfElementLocated()
textToBePresentInElement()
textToBePresentInElementLocated()
textToBePresentInElementValue()
titleIs()
titleContains()
visibilityOf()
visibilityOfAllElements()
visibilityOfAllElementsLocatedBy()
visibilityOfElementLocated()
'''
def find_with_explicit_wait(url, xpath):
    driver.get(url)
    wait = WebDriverWait(driver, 30)
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    print(elem.text == "Helpline Information")
    driver.quit()


if __name__ == '__main__':
    find_with_explicit_wait(url, xpath)