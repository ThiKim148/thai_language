from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_typing_effect():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/")
    
    wait=WebDriverWait(driver, 10)

    try:
        expected_title = "Chào mừng bạn đến với website học tiếng Thái"
        expected_text = "Bạn có thể bắt đầu học từ vựng, ngữ pháp và giao tiếp ngay hôm nay!"

        start_time = time.time()

        # Chờ cho đến khi text của cả hai phần hiện ra đầy đủ
        wait.until(
            EC.text_to_be_present_in_element((By.ID, "typing-title"), expected_title)
        )

        wait.until(
            EC.text_to_be_present_in_element((By.ID, "typing-text"), expected_text)
        )

        end_time = time.time()
        elapsed = end_time - start_time

        expected_duration = (len(expected_title) + len(expected_text)) * 0.08  # speed=80ms
        tolerance = 2.0

        print(f"⏱ Thời gian thực tế: {elapsed:.2f}s")
        print(f"🎯 Thời gian mong đợi: ~{expected_duration:.2f}s")

        if abs(elapsed - expected_duration) <= tolerance:
            print("✅ Hiệu ứng typing hoạt động bình thường, tốc độ hợp lý")
        elif elapsed < expected_duration - tolerance:
            print("⚡ Hiệu ứng typing chạy quá nhanh")
        else:
            print("🐢 Hiệu ứng typing chạy quá chậm")

    finally:
        driver.quit()
        print("🔒 Đã đóng trình duyệt")

if __name__ == "__main__":
    test_typing_effect()

