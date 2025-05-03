import time
from intelium import DesktopAutomation, BrowserAutomation, InteractionType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
import random
from bs4 import BeautifulSoup
import requests

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

def test_chrome_automation():
    """Test advanced Chrome automation capabilities"""
    # Initialize browser automation
    automation = BrowserAutomation()
    
    try:
        # Navigate to a complex website (GitHub)
        automation.navigate_to("https://github.com")
        
        # Wait for and interact with dynamic search
        search_box = automation.find_element("input[type='search']")
        automation.move_to(search_box)
        automation._perform_click(search_box, InteractionType.CLICK)
        automation.type_text("intelium automation framework")
        time.sleep(1)  # Wait for search results
        
        # Test scrolling and dynamic content loading
        automation.scroll_to(0, 500)
        time.sleep(1)
        
        # Find and click a repository link
        repo_links = automation.find_elements("a[data-testid='result-repo-link']")
        if repo_links:
            first_repo = repo_links[0]
            repo_name = first_repo.text
            automation.move_to(first_repo)
            automation._perform_click(first_repo, InteractionType.CLICK)
            
            # Wait for repository page to load
            time.sleep(2)
            
            # Test multiple interaction types
            # 1. Regular click
            automation._perform_click(automation.find_element("button[data-testid='star-button']"), 
                                   InteractionType.CLICK)
            
            # 2. Double click
            automation._perform_click(automation.find_element("button[data-testid='star-button']"), 
                                   InteractionType.DOUBLE_CLICK)
            
            # 3. Right click
            automation._perform_click(automation.find_element("button[data-testid='star-button']"), 
                                   InteractionType.RIGHT_CLICK)
            
            # Test file navigation
            files = automation.find_elements("a[role='rowheader']")
            if files:
                # Click on a file
                automation.move_to(files[0])
                automation._perform_click(files[0], InteractionType.CLICK)
                
                # Wait for file content to load
                time.sleep(2)
                
                # Test scrolling in file view
                automation.scroll_to(0, 300)
                time.sleep(1)
                automation.scroll_to(0, 600)
                
                # Test text selection
                code_element = automation.find_element("table.highlight")
                if code_element:
                    automation.move_to(code_element)
                    automation._perform_click(code_element, InteractionType.CLICK)
                    # Simulate text selection (this would need to be implemented in the framework)
                    # automation.select_text(code_element, start=0, end=100)
        
        # Test navigation
        automation.navigate_to("https://github.com/trending")
        time.sleep(2)
        
        # Test multiple element interaction
        trending_repos = automation.find_elements("article.Box-row")
        if trending_repos:
            for repo in trending_repos[:3]:  # Interact with first 3 trending repos
                automation.move_to(repo)
                time.sleep(0.5)
                automation.scroll_to(0, automation.get_scroll_position()[1] + 100)
        
        # Test form interaction
        automation.navigate_to("https://github.com/contact")
        time.sleep(2)
        
        # Fill out contact form
        name_field = automation.find_element("input[name='name']")
        email_field = automation.find_element("input[name='email']")
        message_field = automation.find_element("textarea[name='message']")
        
        if all([name_field, email_field, message_field]):
            automation.type_text("Test User", name_field)
            automation.type_text("test@example.com", email_field)
            automation.type_text("This is a test message from Intelium automation framework.", message_field)
            
            # Test checkbox interaction
            checkbox = automation.find_element("input[type='checkbox']")
            if checkbox:
                automation._perform_click(checkbox, InteractionType.CLICK)
        
        # Test error handling
        try:
            automation.navigate_to("https://github.com/nonexistent-page-123456789")
            time.sleep(2)
        except Exception as e:
            print(f"Expected error when navigating to non-existent page: {e}")
        
        # Test screenshot capability
        screenshot_path = "test_screenshot.png"
        automation.take_screenshot(screenshot_path)
        assert os.path.exists(screenshot_path), "Screenshot was not saved"
        os.remove(screenshot_path)  # Clean up
        
    finally:
        # Clean up
        automation.quit()

def random_sleep(min_seconds=0.05, max_seconds=0.2):
    """Faster random sleep for more natural interactions"""
    time.sleep(random.uniform(min_seconds, max_seconds))

def setup_browser():
    """Set up and configure the browser with anti-detection measures"""
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Set custom user agent
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    
    # Remove webdriver flag
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

def handle_google_consent(driver, wait):
    """Handle Google's consent popup if present"""
    try:
        consent_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept all')]")))
        consent_button.click()
        random_sleep()
        return True
    except:
        return False

def search_google(driver, wait, query):
    """Search Google for a specific query"""
    try:
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.click()
        random_sleep()
        
        # Type with random delays
        for char in query:
            search_box.send_keys(char)
            random_sleep(0.1, 0.3)
        
        random_sleep()
        search_box.send_keys(Keys.RETURN)
        random_sleep(2, 3)
        return True
    except Exception as e:
        print(f"Error searching Google: {str(e)}")
        driver.save_screenshot("google_search_error.png")
        return False

def find_amazon_link(driver, wait):
    """Find and click the Amazon link in Google search results"""
    selectors = [
        "//a[contains(@href, 'amazon.com')]",
        "//a[contains(@href, 'amazon.com') and not(contains(@href, 'amazon.com/s'))]",
        "//a[contains(@href, 'amazon.com') and contains(text(), 'Amazon')]"
    ]
    
    for selector in selectors:
        try:
            amazon_link = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
            amazon_link.click()
            random_sleep(3, 4)
            return True
        except:
            continue
    
    driver.save_screenshot("amazon_link_error.png")
    return False

def search_amazon(driver, wait, query):
    """Search Amazon for a specific query"""
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            # Wait for page to be fully loaded
            wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
            random_sleep(2, 3)
            
            # Try multiple selectors for the search box
            search_box = None
            search_selectors = [
                (By.ID, "twotabsearchtextbox"),
                (By.NAME, "field-keywords"),
                (By.CSS_SELECTOR, "input[type='text']"),
                (By.CSS_SELECTOR, "input[aria-label='Search']")
            ]
            
            for by, selector in search_selectors:
                try:
                    search_box = wait.until(EC.presence_of_element_located((by, selector)))
                    if search_box.is_displayed() and search_box.is_enabled():
                        break
                except:
                    continue
            
            if not search_box:
                raise Exception("Could not find search box")
            
            # Clear the search box first
            search_box.clear()
            random_sleep()
            
            # Click the search box
            try:
                search_box.click()
            except:
                driver.execute_script("arguments[0].click();", search_box)
            random_sleep()
            
            # Type with random delays
            for char in query:
                search_box.send_keys(char)
                random_sleep(0.1, 0.3)
            
            random_sleep()
            
            # Press Enter to search
            search_box.send_keys(Keys.RETURN)
            random_sleep(3, 4)
            
            # Verify search results loaded
            wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-component-type='s-search-result']")))
            
            return True
            
        except Exception as e:
            print(f"Attempt {retry_count + 1} failed: {str(e)}")
            driver.save_screenshot(f"amazon_search_error_attempt_{retry_count + 1}.png")
            retry_count += 1
            if retry_count < max_retries:
                print("Retrying...")
                random_sleep(2, 3)
                continue
            else:
                print("All retry attempts failed")
                return False

def find_and_click_product(driver, wait):
    """Find and click on a product in Amazon search results"""
    product_selectors = [
        "h2 a span",
        ".a-size-medium.a-color-base.a-text-normal",
        ".a-link-normal .a-text-normal"
    ]
    
    for selector in product_selectors:
        try:
            products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
            if products:
                product = products[0]
                # Scroll product into view
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", product)
                random_sleep()
                
                # Click with JavaScript as fallback
                try:
                    product.click()
                except:
                    driver.execute_script("arguments[0].click();", product)
                
                random_sleep(2, 3)
                return True
        except:
            continue
    
    driver.save_screenshot("product_click_error.png")
    return False

def tool_google_search(driver=None, wait=None):
    """Tool 1: Navigate to Google and search for Wikipedia"""
    print("\nStarting Tool 1: Google Search...")
    
    try:
        if driver is None:
            print("Setting up browser...")
            driver = setup_browser()
            wait = WebDriverWait(driver, 5)  # Reduced wait time
            print("Browser setup complete")
        
        # Initialize BrowserAutomation
        print("Initializing BrowserAutomation...")
        automation = BrowserAutomation(driver)
        print("BrowserAutomation initialized")
        
        print("\nNavigating to Google...")
        driver.get('https://www.google.com')
        random_sleep(0.2, 0.3)  # Shorter wait for page load
        
        # Handle Google consent if present
        try:
            consent_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept all')]")))
            automation.click_at(consent_button, InteractionType.LEFT)
            random_sleep(0.1, 0.2)
        except Exception as e:
            print(f"No consent popup found: {str(e)}")
        
        print("\nSearching for Wikipedia...")
        try:
            search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
            automation.click_at(search_box, InteractionType.LEFT)
            random_sleep(0.1, 0.2)
            
            search_query = "wikipedia artificial intelligence"
            automation.type_at(search_box, search_query, characters_per_minute=600)  # Faster typing
            random_sleep(0.1, 0.2)
            
            search_box.send_keys(Keys.RETURN)
            random_sleep(0.2, 0.3)  # Shorter wait for results
            
            print("\nTool 1 completed successfully!")
            return driver, wait, automation
        except Exception as e:
            print(f"Error during search: {str(e)}")
            if driver:
                driver.quit()
            return None, None, None
        
    except Exception as e:
        print(f"\nTool 1 Error: {str(e)}")
        if driver:
            driver.quit()
        return None, None, None

def tool_find_wikipedia(driver, wait, automation):
    """Tool 2: Find and click Wikipedia link"""
    try:
        print("\nTool 2: Finding Wikipedia link...")
        selectors = [
            "//a[contains(@href, 'wikipedia.org')]",
            "//a[contains(@href, 'wikipedia.org') and contains(text(), 'Artificial intelligence')]",
            "//h3[contains(., 'Artificial intelligence - Wikipedia')]"
        ]
        
        for selector in selectors:
            try:
                wiki_link = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                automation.click_at(wiki_link, InteractionType.LEFT)
                random_sleep(0.2, 0.3)
                return True
            except:
                continue
        
        print("Could not find Wikipedia link")
        return False
        
    except Exception as e:
        print(f"\nTool 2 Error: {str(e)}")
        return False

def tool_wiki_navigation(driver, wait, automation):
    """Tool 3: Navigate through Wikipedia article"""
    try:
        print("\nTool 3: Navigating Wikipedia article...")
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
        random_sleep(0.2, 0.3)
        
        # Get page content for analysis
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # First, let's find and click the History section
        print("Looking for History section...")
        history_selectors = [
            "//span[@id='History']",
            "//span[contains(text(), 'History')]",
            "//h2/span[contains(text(), 'History')]",
            "//h2[contains(., 'History')]",
            "//span[@id='history']",
            "//span[@id='History_of_artificial_intelligence']"
        ]
        
        history_found = False
        for selector in history_selectors:
            try:
                history = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", history)
                random_sleep(0.1, 0.2)
                automation.click_at(history, InteractionType.LEFT)
                print("Successfully found and clicked History section!")
                print("Pausing for 5 seconds...")
                time.sleep(5)  # Pause for 5 seconds
                return True
            except:
                continue
        
        if not history_found:
            print("Could not find History section, trying to find it in the table of contents...")
            toc_selectors = [
                "//div[@id='toc']//a[contains(text(), 'History')]",
                "//div[@id='toc']//span[contains(text(), 'History')]",
                "//div[contains(@class, 'toc')]//a[contains(text(), 'History')]"
            ]
            
            for selector in toc_selectors:
                try:
                    toc_link = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                    automation.click_at(toc_link, InteractionType.LEFT)
                    print("Successfully found and clicked History section in table of contents!")
                    print("Pausing for 5 seconds...")
                    time.sleep(5)  # Pause for 5 seconds
                    return True
                except:
                    continue
        
        print("Could not find History section")
        return False
        
    except Exception as e:
        print(f"\nTool 3 Error: {str(e)}")
        return False

def test_wikipedia_navigation():
    """Main test function that can run individual tools"""
    print("\nStarting Wikipedia navigation test...")
    
    # Run each tool separately
    driver, wait, automation = tool_google_search()
    if driver and wait and automation:
        if tool_find_wikipedia(driver, wait, automation):
            tool_wiki_navigation(driver, wait, automation)
    
    if driver:
        driver.quit()

if __name__ == "__main__":
    test_wikipedia_navigation()
