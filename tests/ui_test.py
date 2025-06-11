import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def test_app_loads():

    driver = webdriver.Chrome()
    actionBuilder = ActionChains(driver)
    wait = WebDriverWait(driver, timeout=2)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()

    driver.get("https://www.amazon.com.tr/")
    assert "Amazon" in driver.title  # Assuming your app's title
    wait.until(EC.presence_of_element_located((By.ID, 'sp-cc-accept')))
    driver.find_element(By.ID, 'sp-cc-accept').click()
    driver.find_element(By.XPATH, '//a[text()="Elektronik"]').click()
    assert "Elektronik" in driver.title  # Assuming your app's title
    
    driver.find_element(By.ID, 's-refinements').find_element(By.XPATH, '//span[text()="Bilgisayarlar, Bileşenleri ve Aksesuarları"]').click()
    assert "Bilgisayarlar, Bileşenleri ve Aksesuarları" in driver.title  # Assuming your app's title
    
    hoverable = driver.find_element(By.CSS_SELECTOR, '#nav-subnav > a:nth-child(5)')
    actionBuilder.move_to_element(hoverable).perform()
    sleep(1)
    laptop = driver.find_element(By.XPATH, '//div[text()="Dizüstü Bilgisayarlar"]')
    actionBuilder.move_to_element(laptop).click().perform()
    assert "Dizüstü Bilgisayarlar" in driver.title  # Assuming your app's title
    
    wait.until(EC.presence_of_element_located((By.ID, 's-refinements')))
    driver.find_element(By.CSS_SELECTOR, '#s-refinements > div:nth-child(6) > ul > li:nth-child(7) > span > a').click()
    sleep(1)
    is_selected_check = driver.find_element(By.CSS_SELECTOR, "#p_123\\/241862 > span > a > div > label > input[type=checkbox]").is_selected()
    assert is_selected_check == True
    
    # Click the visible dropdown label instead of the select element to avoid click interception
    driver.find_element(By.CSS_SELECTOR, '.a-dropdown-label').click()
    driver.find_element(By.ID, 's-result-sort-select_2').click()
    high_to_low_element = driver.find_element(By.CLASS_NAME, "a-dropdown-prompt")
    hilow_element_text = high_to_low_element.text
    assert hilow_element_text == "Fiyat: Yüksekten Düşüğe"

    wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Dell Precision M7680"]')))
    first_of_model = driver.find_element(By.XPATH, '//span[text()="Dell Precision M7680"]')
    """ assert_first_entry = first_of_model.text
    first_of_model.click()
    assert assert_first_entry in driver.title """

    driver.quit()