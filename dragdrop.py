from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
class Dragdrop:
    def __init__(self):
        self.url = "https://jqueryui.com/droppable/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def drag(self):
        try:
            sleep(2)
            self.driver.maximize_window()
            sleep(2)
            self.driver.get(self.url)
            sleep(2)
            # to select the frame first
            frame = self.driver.find_element(by= By.XPATH,value= "//*[@id='content']/iframe")
            self.driver.switch_to.frame(frame)
            # to locate draggable box
            source = self.driver.find_element(by=By.ID, value="draggable")
            # to locate droppable box
            destination = self.driver.find_element(by=By.ID, value="droppable")
            #Action chain to perform placing whitebox into the yellow box
            Actions = ActionChains(self.driver)
            Actions.drag_and_drop(source, destination).perform()
            sleep(3)

        except NoSuchElementException as selenium_error:
            print(selenium_error)
        finally:
            self.driver.close()

drop= Dragdrop()
drop.drag()
