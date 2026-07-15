from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_signup():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://courses.ultimateqa.com/users/sign_up")

        wait = WebDriverWait(driver, 10)

        # First Name
        first_name = wait.until(
            EC.visibility_of_element_located((By.ID, "user[first_name]"))
        )
        first_name.send_keys("Nguyen")

        # Last Name
        last_name = wait.until(
            EC.visibility_of_element_located((By.ID, "user[last_name]"))
        )
        last_name.send_keys("Van A")

        # Email
        email = wait.until(
            EC.visibility_of_element_located((By.ID, "user[email]"))
        )
        email.send_keys("nguyenvana@example.com")

        # Password
        password = wait.until(
            EC.visibility_of_element_located((By.ID, "user[password]"))
        )
        password.send_keys("StrongPassword123!")

        # Checkbox Terms
        terms_checkbox = wait.until(
            EC.element_to_be_clickable((By.ID, "user[terms]"))
        )
        terms_checkbox.click()

        # Button Sign Up
        submit_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@type='submit']")
            )
        )

        # Scroll tới button
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            submit_button
        )

        # Chờ 1 chút cho animation hoàn thành
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit']")
            )
        )

        submit_button.click()

        print("Đã click Sign Up thành công")

        # Chờ trang load
        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        print("Đăng ký hoàn tất")

    except Exception as e:
        print(f"Lỗi: {e}")

    finally:
        driver.quit()