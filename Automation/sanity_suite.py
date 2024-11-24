import pytest
"""Execute in Pytest"""


def get_homepage_links():
    return ["https://grocerymate.com/home", "https://grocerymate.com/shop"]

def check_link(link):
    return True

def is_keyboard_navigable():
    return True

def check_images_alt_text():
    return True

def check_color_contrast():
    return True

def load_login_page():
    return "Login page loaded successfully"

def load_registration_page():
    return "Registration page loaded successfully"

def load_product_page(product_id):
    return "Product page loaded successfully"

def load_cart_page():
    return "Cart page load successfull"

def get_footer_links():
    return ["https://grocerymate.com/privacy", "https://grocerymate.com/terms"]

@pytest.mark.sanity
def test_homepage_links():
    links = get_homepage_links()
    for link in links:
        assert check_link(link), f"Homepage link {link} is broken."

@pytest.mark.accessibility
def test_accessibility_keyboard_navigation():
    assert is_keyboard_navigable(), "Site is not keyboard-navigable."

@pytest.mark.accessibility
def test_accessibility_alt_text():
    assert check_images_alt_text(), "Images are missing alt text."

@pytest.mark.accessibility
def test_accessibility_color_contrast():
    assert check_color_contrast(), "Color contrast does not meet standards."

@pytest.mark.sanity
def test_login_page_loads():
    result = load_login_page()
    assert result == "Login page loaded successfully", "Login page failed to load."

@pytest.mark.sanity
def test_registration_page_loads():
    result = load_registration_page()
    assert result == "Registration page loaded successfully", "Registration page failed to load."

@pytest.mark.sanity
def test_product_page_loads():
    product_id = 1
    result = load_product_page(product_id)
    assert result == "Product page loaded successfully", f"Product page for ID {product_id} failed to load."

@pytest.mark.sanity
def test_cart_page_loads():
    result = load_cart_page()
    assert result == "Cart page loaded successfully", "Cart page failed to load."

@pytest.mark.sanity
def test_footer_links():
    footer_links = get_footer_links()
    for link in footer_links:
        assert check_link(link), f"Footer link {link} is broken."
