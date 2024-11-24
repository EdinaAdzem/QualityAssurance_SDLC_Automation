import pytest
from unittest.mock import MagicMock, patch
def register_user(username, password):
    if username == "EdinaAdzem":
        return "Username already exists"
    return "User registered successfully"

def search_product(query):
    if query == "validProduct":
        return ["Product 1", "Product 2"]
    return []

def add_to_cart(product_id):
    cart.append(product_id)

def remove_from_cart(product_id):
    cart.remove(product_id)

def get_cart_items():
    return cart

def calculate_cart_total():
    return sum(product_prices[item] for item in cart)

def complete_checkout():
    if not cart:
        return "Cart is empty"
    return "Order placed successfully"

def process_payment(card_details):
    if card_details["number"] == "validCard":
        return "Payment processed successfully"
    return "Payment failed"

def reset_password(email):
    return "Password reset link sent to email"


cart = []
product_prices = {1: 50, 2: 35}

# Test cases
@pytest.mark.parametrize("username, password, expected", [
    ("validUser", "validPass123", "confirmation"),
    ("existingUser", "validPass123", "error")
])
def test_user_registration(username, password, expected):
    result = register_user(username, password)
    if expected == "confirmation":
        assert result == "User registered successfully"
    else:
        assert result == "Username already exists"

@pytest.mark.parametrize("search_query, expected", [
    ("validProduct", "product_list"),
    ("invalidProduct", "no_results")
])
def test_product_search(search_query, expected):
    result = search_product(search_query)
    if expected == "product_list":
        assert len(result) > 0
    else:
        assert result == []

def test_add_remove_from_cart():
    product_id = 1
    add_to_cart(product_id)
    assert product_id in get_cart_items()
    remove_from_cart(product_id)
    assert product_id not in get_cart_items()

def test_cart_total():
    add_to_cart(1)
    add_to_cart(2)
    expected_total = product_prices[1] + product_prices[2]
    total_price = calculate_cart_total()
    assert total_price == expected_total
    cart.clear()  # Cleanup for subsequent tests

def test_checkout():
    add_to_cart(1)
    result = complete_checkout()
    assert result == "Order placed successfully"
    cart.clear()  # Cleanup for subsequent tests

@pytest.mark.parametrize("card_details, expected", [
    ({"number": "validCard", "expiry": "12/25"}, "success"),
    ({"number": "invalidCard", "expiry": "12/25"}, "failure")
])
def test_payment(card_details, expected):
    result = process_payment(card_details)
    assert result == "Payment processed successfully" if expected == "success" else "Payment failed"

def test_reset_password():
    email = "user@example.com"
    result = reset_password(email)
    assert result == "Password reset link sent to email"
