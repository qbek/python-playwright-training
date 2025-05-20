import pytest, time
from playwright.sync_api import Page, expect

def test_zadanie1(page: Page):
  page.goto('https://qbek.github.io/selenium-exercises/pl/basic_form.html')
  page.locator('#firstname').fill('Kuba')
  page.keyboard.press('Tab')
  page.locator('input:focus').fill('Szewcz')
  page.keyboard.press('Tab')
  page.locator('input:focus').fill('ab@a.b')
  # page.locator('#lastname').fill('Szewcz')
  # page.locator('#email').fill('ab@a.b')
  page.locator('.btn-success').click()
  # expect(page.locator('#firstname-check')).to_have_text('Kuba')
  # expect(page.locator('#lastname-check')).to_have_text('Szewcz')
  # expect(page.locator('.form-control-plaintext')).to_have_value('ab@a.b...')
  pageData = {
    'fname': page.locator('#firstname-check').text_content(),
    'lnamne': page.locator('#lastname-check').text_content(),
    'email': page.locator('.form-control-plaintext').input_value()
  }
  expected = {
    'fname': 'Kuba',
    'lnamne': 'Szecz',
    'email': 'adsfadsf'
  }

  assert pageData == expected


def test_zadanie2(page: Page):
  page.goto('https://qbek.github.io/selenium-exercises/pl/check_boxes.html')
  # klikanie w checkboxy jest antypatternem
  page.locator('[name="blue"]').click()
  page.locator('[name="red"]').check()
  time.sleep(5)
  page.locator('[name="blue"]').click()
  page.locator('[name="red"]').check()
  time.sleep(5)

def test_zadanie3(page: Page):
  page.goto('https://qbek.github.io/selenium-exercises/pl/radio_buttons.html')
  page.locator('[value="rmffm"]').check()
  href = page.locator('#radiozet-details a').get_attribute('href')
  expect(page.locator('#radiozet-details [href="https://www.radiozet.pl"]')).to_be_visible()
  
