# SauceDemo QA Automation Project

Automated UI test suite for SauceDemo using Python, pytest, and Selenium.

## Features
- Login testing
- Inventory testing
- Cart testing
- Checkout testing

## Test Coverage
- Valid login
- Invalid login
- Locked out user
- Inventory items display
- Inventory page title
- Add item to cart
- Remove item from cart
- Complete checkout
- Checkout validation error

## Framework Features
- Pytest fixtures for browser setup
- Smoke test markers
- Explicit waits for reliable UI checks
- Page Object Model:
  - `LoginPage`
  - `InventoryPage`
  - `CartPage`
  - `CheckoutPage`

## Run all tests
```powershell
pytest -v
