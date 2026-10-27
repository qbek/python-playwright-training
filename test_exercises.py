import time
import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect

def test_exercise_1(page: Page):
    page.goto('https://qbek.github.io/selenium-exercises/pl/basic_form.html')

    # Podstawowe podejscie z lokalizacja kazdego input fielda
    # page.locator('#lastname').fill('Szewc')
    # page.locator('#email').fill('wp@wp.pl')
    # page.locator('#firstname').fill('Kuba')
    
    
    page.locator('#firstname').fill('Kuba')
    page.keyboard.press('Tab')
    page.locator('input:focus').fill('Szewc')
    page.keyboard.press('Tab')
    page.locator('input:focus').fill('wp@wp.pl')

    page.locator('.btn-success').click()


    expect(page.locator('#firstname-check')).to_have_text('Kuba')
    expect(page.locator('#lastname-check')).to_have_text('Szewc')
    expect(page.locator('.form-control-plaintext')).to_have_value('wp@wp.pl')


    # document.querySelectorAll('css idzie tutaj')

def test_exercise_2a(page: Page):
    page.goto('https://qbek.github.io/selenium-exercises/pl/check_boxes.html')
    page.locator('[name="green"]').uncheck()

    page.locator('[name="red"]').check()
    page.locator('[name="blue"]').check()

    expect(page.locator('#light')).to_have_attribute('data-color', '#FF00FF')
    

def test_exercise_2b(page: Page):
    page.goto('https://qbek.github.io/selenium-exercises/pl/check_boxes.html')
    expect(page.locator('#text')).not_to_be_enabled()
    # page.locator('#switch').check(force=True)
    page.locator('[for="switch"]').check()
    expect(page.locator('#text')).to_be_enabled()

def test_exercise_3(page: Page):
    page.goto('https://qbek.github.io/selenium-exercises/pl/radio_buttons.html')
    page.locator('[value="radiozet"]').check()
    expect(page.locator('#radiozet-details a')).to_have_attribute('href', 'https://www.radiozet.pl')
    expect(page.locator('#radiozet-details a')).to_be_visible()