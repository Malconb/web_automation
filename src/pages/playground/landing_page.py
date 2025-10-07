from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from utils.logger import get_logger
from pages.playground.base_page import BasePage

logger = get_logger(__name__)

class LandingPage(BasePage):

    dynamic_id_option = (By.LINK_TEXT, "Dynamic ID")
    class_attribute_option = (By.LINK_TEXT, "Class Attribute")    
    hidden_layers_option = (By.LINK_TEXT, "Hidden Layers")    
    
    def __init__(self, driver):
        super().__init__(driver)        
        self.url = "http://uitestingplayground.com/"
        self.driver.get(self.url)
        logger.info("Navigating to the page: " + self.url)

    # dynamic_id_option
    def get_dynamic_id_option(self):
        return self.find_element(self.dynamic_id_option)
        
    
    # class_attribute_option
    def get_class_attribute_option(self):
        return self.find_element(self.class_attribute_option)
        
    # hidden_layers_option
    def get_hidden_layers_option(self):
        return self.find_element(self.hidden_layers_option)