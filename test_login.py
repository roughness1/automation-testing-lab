from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
CART_URL = "https://www.saucedemo.com/cart.html"


def login_as_standard_user(page: Page) -> None:
    page.goto(BASE_URL)
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()


def test_login_page_is_displayed(page: Page):
    page.goto(BASE_URL)

    expect(page.locator('[data-test="username"]')).to_be_visible()
    expect(page.locator('[data-test="password"]')).to_be_visible()
    expect(page.locator('[data-test="login-button"]')).to_be_visible()


def test_successful_login(page: Page):
    login_as_standard_user(page)

    expect(page).to_have_url(INVENTORY_URL)
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()


def test_add_product_to_cart(page: Page):
    login_as_standard_user(page)
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")


def test_product_is_displayed_in_cart(page: Page):
    login_as_standard_user(page)
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")

    page.locator('[data-test="shopping-cart-link"]').click()

    expect(page).to_have_url(CART_URL)
    expect(page.get_by_text("Sauce Labs Backpack", exact=True)).to_be_visible()


def test_login_with_invalid_password(page: Page):
    page.goto(BASE_URL)
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("wrong_password")
    page.locator('[data-test="login-button"]').click()

    error = page.locator('[data-test="error"]')
    expect(error).to_be_visible()
    expect(error).to_contain_text("Username and password do not match")
