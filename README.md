# SauceDemo QA Automation Project

Automated UI test suite for SauceDemo using Python, pytest, and Selenium.

## Coverage
- Login
- Inventory
- Cart
- Checkout

## Key scenarios
- Valid login
- Invalid login
- Locked out user
- Inventory items display
- Add item to cart
- Remove item from cart
- Complete checkout
- Checkout validation error

## Run all SauceDemo tests
```powershell
pytest tests/saucedemo -v

## 2. Add smoke markers cleanly

Only mark these four:

- `test_valid_login`
- `test_inventory_items_display`
- `test_add_item_to_cart`
- `test_complete_checkout`

Add `import pytest` at the top of those files, then add:

```python
@pytest.mark.smoke