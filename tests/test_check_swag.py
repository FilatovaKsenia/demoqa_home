from pages.swag_labs import SwagLabs
from conftest import browser

def visit_site(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.exist_icon()

def found_field_name(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.exist_name()

def found_field_password(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.exist_password()
