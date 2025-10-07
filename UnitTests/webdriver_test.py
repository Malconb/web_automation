from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome driver using Webdriver Manager
driver = webdriver.Chrome(ChromeDriverManager().install())

# Now you can use the driver to interact with Chrome
driver.get("http://www.google.com")

# ... perform your automation tasks ...

driver.quit()