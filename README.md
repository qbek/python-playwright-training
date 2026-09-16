# Szkolenie Playwright - Python

## Weryfikacja i przygotowanie środowiska:

W terminalu (lini poleceń) uruchamiamy komendy i sprawdzamy czy są zainstalowane potrzebne narzędzia

```
python --version
lub
python3 --version

pip --version
lub
pip3 --version
```


## Stworzenie wirtualnego środowiska (venv)

```
python -m venv
source .venv/bin/activate
```

## Instalacja Playwright / Python

[Playwright Intro](https://playwright.dev/python/docs/intro)

## Zapisanie wymaganych zależności w projekcie

```
pip freeze > pip-packages.txt
pip install -r pip-packages.txt
```

## HelloWorld

```
import pytest
from playwright.sync_api import Page

def test_helloWorld(page: Page):
     page.goto('https://google.com')
```

## pytest.ini

Stwórz w root'cie projektu plik pytest.ini z zawartością:
```
[pytest]
python_files = *Test.py
addopts = -s --headed
```

## Najważniejsze linki z dokumentacji:

* [Akcje](https://playwright.dev/python/docs/input)
* [Asercje](https://playwright.dev/python/docs/test-assertions)
* [Elementy](https://playwright.dev/python/docs/api/class-elementhandle)


## Flow implementacji testu:

1. Zaimplementuj test w możliwe najprostszy sposób (bez przydasiów)
2. Sprawdzić asercje (przetestować je!!!)
--- DOBRY KOD ---
3. Refaktor
4. Sprawdzi asercje ponownie
--- Bardzo DOBRY KOD ---