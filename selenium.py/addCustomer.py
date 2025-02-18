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
        driver.get("https://demoqa.com/text-box")
        # time.sleep(2)  # Pause for 2 seconds to let the page load

        # Create a wait object with 10-second timeout
        wait = WebDriverWait(driver, 10)

        # Handle the name field
        name_field = wait.until(
            EC.presence_of_element_located((By.ID, "userName"))
        )  # Wait until name field is present
        name_field.send_keys("John")  # Type "John"
        time.sleep(1)  # Wait 1 second
        name_field.send_keys(" Doe")  # Add "Doe"
        time.sleep(1)  # Wait again

        # Handle the email field
        email_field = driver.find_element(By.ID, "userEmail")  # Find email input field
        email_field.send_keys("john")  # Type first part
        time.sleep(1)
        email_field.send_keys(".doe@")  # Type second part
        time.sleep(1)
        email_field.send_keys("example.com")  # Type third part
        time.sleep(1)

        # Handle current address field
        current_address = driver.find_element(
            By.ID, "currentAddress"
        )  # Find address input
        current_address.send_keys("123 Main Street")  # Type street
        time.sleep(1)
        current_address.send_keys(", City")  # Add city
        time.sleep(1)
        current_address.send_keys(", Country")  # Add country
        time.sleep(1)

        # Handle permanent address field
        permanent_address = driver.find_element(
            By.ID, "permanentAddress"
        )  # Find permanent address input
        permanent_address.send_keys(
            "456 Second Street, City, Country"
        )  # Type full address
        time.sleep(1)

        # Handle form submission
        submit_button = driver.find_element(By.ID, "submit")  # Find submit button
        # Scroll to make button visible
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        time.sleep(1)  # Wait after scrolling
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