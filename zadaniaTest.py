import pytest
from playwright.sync_api import Page, expect

def test_cwiczenie1(page: Page):
  page.goto('https://qbek.github.io/selenium-exercises/pl/basic_form.html')
  page.locator('#firstname').fill('Kuba')
  page.keyboard.press('Tab')

  page.locator('input:focus').fill('Szewczyk')
  page.keyboard.press('Tab')

  page.locator('input:focus').fill('wp@wp2.pl')
  page.keyboard.press('Enter')
  
  # page.locator('#lastname').fill('Szewczyk')
  # page.locator('#email').fill('wp@wp.pl')
  # page.locator('.btn-success').click()

  pageData = {
    'name': page.locator('#firstname-check').text_content(),
    'last': page.locator('#lastname-check').text_content(),
    'email': page.locator('.form-control-plaintext').input_value()
  }

  expected = {
    'name': 'Kuba!!!',
    'last': 'Szewczyk',
    'email': 'wp@wp.pl!!!'
  }

  assert pageData == expected

  
  expect(page.locator('#firstname-check')).to_have_text('Kuba!!!')
  expect(page.locator('#lastname-check')).to_have_text('Szewczyk!!!')
  expect(page.locator('.form-control-plaintext')).to_have_value('wp@wp.pl')
  

def test_cwiczenie2(page: Page):
  page.goto('https://qbek.github.io/selenium-exercises/pl/radio_buttons.html')
  # page.locator('[value="rmffm"]').click()
  page.locator('[value="radiozet"]').click()
  expect(page.locator('#radiozet-details a')).to_have_attribute('href', 'https://www.radiozet.pl')
  expect(page.locator('#radiozet-details a')).to_be_visible()

  expect(page.locator('#radiozet-details a[href="https://www.radiozet.pl"]')).to_be_visible()

