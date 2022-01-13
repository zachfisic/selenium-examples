from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# set options for headless browser
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/usr/local/bin/chromedriver'

# We create a function since we can't use a shared driver while multiprocessing
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver
 
def print_title(link):
    driver = browser()  # Each instance uses a different driver.
    driver.get(link)
    print(driver.title)
    driver.quit()

def process():
    links = ["https://rehabs.com/", "https://rehabs.com/about/getting-sober/", "https://rehabs.com/alcoholism-and-fear/"]
    pool = Pool(processes=3)
    for i in range(0, len(links)):  
        pool.apply_async(print_title, args={links[i]})
    pool.close()
    pool.join()
    
if __name__ == '__main__':
    process()