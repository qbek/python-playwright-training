import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect
from time import sleep

def test_exercise1(page: Page):
    page.goto("https://qbek.github.io/selenium-exercises/pl/basic_form.html")

    page.locator("#firstname").fill("Kuba")
    # page.locator("#lastname").fill("Szewczyk")
    # page.locator("#email").fill("kuba@wp.pl")

    # alternatywa w postaci nawigacji TAB'em
    page.keyboard.press("Tab")
    page.locator('input:focus').fill("Szewczykaaaaaa")
    page.keyboard.press("Tab")
    page.locator('input:focus').fill("kuba@wp.plaaaaaa")

    page.locator(".btn-success").click()

    # alternatywa do expect: 1. pobierz wszystkie dane 2. sprawdz wszystko za jednym zamachem
    dataFromPage = {
        'fname': page.locator("#firstname-check").text_content(),
        'lname': page.locator("#lastname-check").text_content(),
        'mail': page.locator(".form-control-plaintext").input_value()
    }

    expected = {
        'fname': "Kuba",
        'lname': "Szewczyk",
        'mail': "kuba@wp.pl"
    }

    assert dataFromPage == expected

    # expect(page.locator("#firstname-check")).to_have_text("Kuba")
    # expect(page.locator("#lastname-check")).to_have_text("Szewczyk")
    # expect(page.locator(".form-control-plaintext")).to_have_value("kuba@wp.pl")

def test_color_mixer(page: Page):
    page.goto("https://qbek.github.io/selenium-exercises/pl/check_boxes.html")

    # zabezpieczenie przed 'flaky' tests -> pełna kontrola warunków początkowych
    # nie tylko to co ma byc zaznaczone, ale również kontrola tego co ma być odznaczone
    page.locator('[name="red"]').check()
    page.locator('[name="green"]').uncheck()
    page.locator('[name="blue"]').check()
    
    expect(page.locator('#light')).to_have_attribute('data-color', '#FF00FF')


def test_exercise2b(page: Page):
    page.goto("https://qbek.github.io/selenium-exercises/pl/check_boxes.html")

    expect(page.locator('#text')).to_be_disabled()

    # jeżeli docelowy element jest przysłonięty
    # page.locator('#switch').check()
    # wtedy trzeba kliknac w obiek przysłaniający
    page.locator('[for="switch"]').click()
    expect(page.locator('#text')).to_be_enabled()

def test_exercise3(page: Page):
    page.goto('https://qbek.github.io/selenium-exercises/pl/radio_buttons.html')

    page.locator('[value="radiozet"]').check()
    # antywzorzec - nie klikamy w linki prowadzace do zew. zasobów
    # page.locator('#radiozet-details a').click()
    # linki testujemy statycznie - czy sama wartosc jest poprawna
    expect(page.locator('#radiozet-details a')).to_have_attribute('href', 'https://www.radiozet.pl')
    expect(page.locator('#radiozet-details a')).to_be_visible()