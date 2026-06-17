from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_registration_form():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/courses/1/")  # URL trang chi tiết khóa học

    try:
        wait = WebDriverWait(driver, 10)

        # 1. Nhấn nút Đăng ký ngay
        register_btn = wait.until(EC.element_to_be_clickable((By.ID, "register-btn")))
        register_btn.click()

        # 2. Điền thông tin vào form
        name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
        phone_input = wait.until(EC.presence_of_element_located((By.ID, "phone")))
        email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))

        test_name = "Nguyễn Văn A"
        test_phone = "0912345678"
        test_email = "vana@example.com"

        name_input.send_keys(test_name)
        phone_input.send_keys(test_phone)
        email_input.send_keys(test_email)

        # 3. Nhấn nút Save
        save_btn = wait.until(EC.element_to_be_clickable((By.ID, "save-btn")))
        save_btn.click()

        # 4. Kiểm tra thông tin hiển thị ở confirm-container
        confirm_name = wait.until(EC.presence_of_element_located((By.ID, "confirm-name"))).text
        confirm_phone = wait.until(EC.presence_of_element_located((By.ID, "confirm-phone"))).text
        confirm_email = wait.until(EC.presence_of_element_located((By.ID, "confirm-email"))).text

        assert confirm_name == test_name, f"Expected {test_name}, got {confirm_name}"
        assert confirm_phone == test_phone, f"Expected {test_phone}, got {confirm_phone}"
        assert confirm_email == test_email, f"Expected {test_email}, got {confirm_email}"

        print("✅ Thông tin hiển thị đúng với dữ liệu đã nhập")

        # 5. Nhấn nút Đồng ý
        agree_btn = wait.until(EC.element_to_be_clickable((By.ID, "agree-btn")))
        agree_btn.click()

        # 6. Kiểm tra alert hiển thị
        alert = wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        assert "🎉 Đăng ký thành công cho khóa học!" in alert_text
        print(f"✅ Alert hiển thị đúng: {alert_text}")
        alert.accept()

    finally:
        driver.quit()
        print("🔒 Đã đóng trình duyệt")

if __name__ == "__main__":
    test_registration_form()
