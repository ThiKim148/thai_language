from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_signin():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        driver.get("https://courses.ultimateqa.com/users/sign_in")  # URL form đăng nhập

        wait = WebDriverWait(driver, 10)

        # Điền email
        email_box = wait.until(EC.presence_of_element_located((By.ID, "user[email]")))
        email_box.send_keys("nguyenvana@example.com")

        # Điền password
        password_box = wait.until(EC.presence_of_element_located((By.ID, "user[password]")))
        password_box.send_keys("StrongPassword123!")

        # Tick "Remember me" nếu muốn
        remember_me = wait.until(EC.element_to_be_clickable((By.ID, "user[remember_me]")))
        remember_me.click()

        # Nút submit (không dùng id động, chọn theo text hoặc class)
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(),'Sign in')]"))
        )

        # Scroll và click bằng JS để tránh bị intercept
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        driver.execute_script("arguments[0].click();", submit_button)

        # Chờ trang sau khi đăng nhập load (ví dụ chờ heading Welcome biến mất hoặc dashboard xuất hiện)
        wait.until(EC.presence_of_element_located((By.ID, "main-content")))
        
    except Exception as e:
        print(f"Test failed: {e}")
    
    finally:
        driver.quit()
