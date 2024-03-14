from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
# Open Zillow website
driver.get("https://www.zillow.com/homes/")

# Sleep for 120 seconds to allow time for manual interaction (solve captcha)
sleep(120)

captcha_container = By.XPATH("//*[@id='px-captcha-wrapper']/div")

# Find up to 5 iframes containing captcha buttons and click and hold them
for i in range(1, 6):
    try:
        # Locate the captcha button inside iframe
        button_element = captcha_container.find_element(By.XPATH, f"//*[@id='px-captcha']//iframe[{i}]")

        # Switch to the iframe
        driver.switch_to.frame(button_element)

        # Perform click and hold action
        action_chains = ActionChains(driver)
        action_chains.click_and_hold(button_element).perform()

        # Sleep for up to 5 seconds (adjust sleep time as needed)
        sleep(min(5, 5 - (i - 1)))

        # Release the button
        action_chains.release().perform()

        # Switch back to the main document
        driver.switch_to.default_content()

    except Exception as e:
        print(f"An error occurred: {e}")

# Close the browser session
# driver.quit()


