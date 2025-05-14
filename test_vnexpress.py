from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_vnexpress_homepage():
    # Khởi tạo trình duyệt
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://vnexpress.net/")

    # Chờ tiêu đề trang
    WebDriverWait(driver, 10).until(EC.title_contains("VnExpress"))
    assert "VnExpress" in driver.title

    # Chờ mục "Mới nhất" xuất hiện (dùng XPATH cho mọi thẻ chứa text)
    latest_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Mới nhất')]"))
    )
    assert latest_section is not None

    # Kiểm tra có ít nhất 1 tin bài trong mục "Mới nhất"
    articles = driver.find_elements(By.CSS_SELECTOR, ".section_topstory .item-news")
    assert len(articles) > 0

    print("Test passed!")
    driver.quit()

if __name__ == "__main__":
    test_vnexpress_homepage() 