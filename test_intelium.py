import time
from intelium import DesktopAutomation, BrowserAutomation, InteractionType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_standalone():
    print("Testing standalone functionality...")
    automation = DesktopAutomation()
    
    # Get screen center coordinates
    import pyautogui
    screen_width, screen_height = pyautogui.size()
    center = {'x': screen_width // 2, 'y': screen_height // 2}
    
    # Test mouse movement
    print("Testing mouse movement...")
    automation.move_to(center)
    time.sleep(1)
    
    # Test clicking
    print("Testing clicking...")
    automation.click_at(center)
    time.sleep(1)
    
    print("Standalone tests completed!")

def test_selenium():
    print("Testing Selenium integration...")
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)
    automation = BrowserAutomation(driver)
    
    try:
        # Navigate to DuckDuckGo
        driver.get('https://duckduckgo.com/')
        
        # Find and interact with search box
        print("Testing typing...")
        search_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-state="suggesting"]')))
        automation.type_at(search_box, 'Intelium automation test')
        time.sleep(2)
        
        # Find and click search button
        print("Testing clicking in browser...")
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Search"]')))
        automation.click_at(search_button)
        time.sleep(2)
        
        print("Selenium tests completed!")
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Starting Intelium tests...")
    
    try:
        test_standalone()
        print("\n" + "="*50 + "\n")
        test_selenium()
        print("\nAll tests completed successfully!")
    except Exception as e:
        print(f"\nTest failed with error: {str(e)}") 