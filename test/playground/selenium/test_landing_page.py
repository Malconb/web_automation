from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.playground.landing_page import LandingPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestPlaygroundLandingPage:
    
    @classmethod
    def setup_class(self):
        # start the session
        self.driver = webdriver.Chrome()
        logger.info("Starting the session")
        self.driver.implicitly_wait(10)
    
    def test_playground_landing_page(self):
        """
        Test that UI playground landing page is displayed with all options
        """                
        
        # create the page object
        landing_page = LandingPage(self.driver)
        
        # verify the elements displayed
        logger.info("Verifying the elements displayed")
        logger.debug("Dynamic ID option: " + landing_page.get_dynamic_id_option().text)
        logger.debug("Class Attribute option: " + landing_page.get_class_attribute_option().text)
        logger.debug("Hidden Layers option: " + landing_page.get_hidden_layers_option().text)
        assert landing_page.get_dynamic_id_option().text == "Dynamic ID", "Dynamic ID option is not displayed" 
        assert landing_page.get_class_attribute_option().text == "Class Attribute", "Class Attribute option is not displayed"
        assert landing_page.get_hidden_layers_option().text == "Hidden Layers", "Hidden Layers option is not displayed"
                    
    
    @classmethod
    def teardown_class(self):
        # Close the browser
        logger.info("Closing the browser")
        self.driver.quit()