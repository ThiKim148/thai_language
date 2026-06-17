from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Hàm xem chi tiết khóa học
def view_course_detail(driver, href, course_name, index):

    print(f"\n🔗 Kiểm tra khóa học {index}")
    print(f"Tên khóa học: {course_name}")
    print(f"Href: {href}")

    # Truy cập trang chi tiết
    driver.get(href)

    # Kiểm tra URL
    if href == driver.current_url:
        print("✅ Điều hướng đúng trang chi tiết")
    else:
        print("❌ Điều hướng sai")

    # In URL hiện tại
    print("Current URL:", driver.current_url)

    # Quay lại
    driver.back()


# Hàm test
def test_all_course_detail_buttons():

    driver = webdriver.Chrome()

    driver.get("http://localhost:8000/courses/")

    wait = WebDriverWait(driver, 10)

    try:

        # Lấy tất cả card khóa học
        course_cards = wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "course-card")
            )
        )

        print(f"Tìm thấy {len(course_cards)} khóa học")

        for idx in range(len(course_cards)):

            # Reload card sau khi back
            course_cards = driver.find_elements(By.CLASS_NAME, "course-card")

            card = course_cards[idx]

            # Lấy tên khóa học ngoài card
            course_name = card.find_element(By.TAG_NAME, "h3").text

            # Lấy thẻ a chứa button
            detail_button = card.find_element(
                By.XPATH, ".//a[button[contains(.,'Xem chi tiết')]]")

            # Lấy href
            href = detail_button.get_attribute("href")

            # Gọi hàm xem chi tiết
            view_course_detail(
                driver,
                href,
                course_name,
                idx + 1
            )

    finally:
        driver.quit()
        print("\n🔒 Đã đóng trình duyệt")


if __name__ == "__main__":
    test_all_course_detail_buttons()

