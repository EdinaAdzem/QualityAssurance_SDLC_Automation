def test_homepage_links():
    links = get_homepage_links()
    for link in links:
        assert check_link(link)

def test_accessibility_keyboard_navigation():
    assert is_keyboard_navigable()

def test_accessibility_alt_text():
    assert check_images_alt_text()

def test_accessibility_color_contrast():
    assert check_color_contrast()

def test_login_page_loads():
    result = load_login_page()
    assert result == "Login page loaded successfully"

def test_registration_page_loads():
    result = load_registration_page()
    assert result == "Registration page loaded successfully"

def test_product_page_loads():
    product_id = 1
    result = load_product_page(product_id)
    assert result == "Product page loaded successfully"

def test_cart_page_loads():
    result = load_cart_page()
    assert result == "Cart page loaded successfully"

def test_footer_links():
    footer_links = get_footer_links()
    for link in footer_links:
        assert check_link(link)
