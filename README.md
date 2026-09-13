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
