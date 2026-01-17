from ui.pages.login_page import LoginPage

def test_login_with_invalid_credentials(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("wrong_user", "wrong_password")

    error_text = login_page.get_error_text()
    assert "Epic sadface" in error_text