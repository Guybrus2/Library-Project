# /opt/anaconda3/bin/python sel.py
# Import statements
from selenium import webdriver  # Main Se


# lenium package for browser automation
# Manages ChromeDriver service
from selenium.webdriver.chrome.service import Service

# Chrome-specific configuration options
from selenium.webdriver.chrome.options import Options

# Provides locator strategies (ID, CLASS, etc.)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # Implements explicit waits

# Conditions for WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # For adding delays between actions

# Function to set up the Chrome WebDriver


def setup_driver():
    chrome_options = Options()  # Create a new Options object for Chrome
    service = Service()  # Create a new Service object to manage ChromeDriver
    # Initialize Chrome with our settings
    return webdriver.Chrome(service=service, options=chrome_options)


def interact_with_form():
    driver = setup_driver()  # Create a new browser instance

    try:
        # Open the website
        # Navigate to the specified URL
        driver.get("http://127.0.0.1:5500/frontend/index.html")
        time.sleep(2)  # Pause for 2 seconds to let the page load

        # Create a wait object with 10-second timeout
        wait = WebDriverWait(driver, 10)
        time.sleep(3)
        username = driver.find_element(By.ID,"username")
        username.send_keys('nigga')
        time.sleep(1)
        password = driver.find_element(By.ID,"password")
        password.send_keys("123")

        button = driver.find_element(By.XPATH, "//button[@onclick='login()']")
        button.click()

        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()


        # Handle the name field
        name_field = wait.until(
            EC.presence_of_element_located((By.ID, "game-name"))
        )  # Wait until name field is present
        name_field.send_keys("John")  # Type "John"
        time.sleep(1)  # Wait 1 second
        name_field.send_keys(" Doe")  # Add "Doe"
        time.sleep(1)  # Wait again

        # Handle the email field
        creator_field = driver.find_element(By.ID, "game-creator")  # Find email input field
        creator_field.send_keys("john")  # Type first part


        # Handle current address field
        year_published =  driver.find_element(By.ID,"game-year-published")
        year_published.send_keys(2019)
        time.sleep(1)
        genre = driver.find_element(By.ID,"game-genre")
        year_published.send_keys("action")
        time.sleep(1)
        pic_url = driver.find_element(By.ID,"game-picture-url")
        pic_url.send_keys("https://upload.wikimedia.org/wikipedia/en/4/44/Red_Dead_Redemption_II.jpg")
        time.sleep(2)
        # Handle form submission
        submit_button = driver.find_element(By.ID, "add-game-btn")  # Find submit button
        submit_button.click()  # Click the submit button

        time.sleep(3)  # Wait to see the results

        # Wait for user input before closing
        input("Press Enter to close the browser...")

    except Exception as e:
        print(f"An error occurred: {str(e)}")  # Print any errors that occur

    finally:
        driver.quit()  # Close the browser, regardless of success or failure


# Script entry point
# Only run if this file is run directly (not imported)
if __name__ == "__main__":
    interact_with_form()  # Start the form interaction process