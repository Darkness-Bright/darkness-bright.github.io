url = 'https://replit.com/@markzhere/OpenAI-Assistant'

usernames = ['abeyance','abreast','abscission','absecond']
password = 'replit()90'

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

def randint(a, b):
  return a + randbelow(b - a + 1)
def randbelow(n):
  k = n.bit_length()
  numbytes = (k + 7) // 8
  while True:
    r = int.from_bytes(random_bytes(numbytes), "big")
    r >>= numbytes * 8 - k
    if r < n:
      return r
def random_bytes(n):
  with open("/dev/urandom", "rb") as file:
    return file.read(n)

class PythonOrgSearch(unittest.TestCase):

  def setUp(self):
    ua = UserAgent()
    userAgent = ua.random
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # options.add_argument("--start-maximized")
    options.add_argument('user-agent='+userAgent)
    options.add_experimental_option("excludeSwitches", ['enable-automation']);
    self.driver = webdriver.Chrome(options=options)

  def test_search_in_python_org(self):
    driver = self.driver
    driver.get('https://replit.com/login')
    driver.minimize_window()
    self.assertIn("Log In - Replit", driver.title)
    time.sleep(randint(1,5)/2)
    usernameinput = driver.find_element(By.NAME, "username")
    for i in usernames[0]:
      time.sleep(randint(1,9)/10)
      usernameinput.send_keys(i)
    passwordinput = driver.find_element(By.NAME, "password")
    for i in password:
      time.sleep(randint(1,9)/10)
      passwordinput.send_keys(i)
    time.sleep(1)
    passwordinput.send_keys(Keys.RETURN)
    time.sleep(333)

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()