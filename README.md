# Automation Testing Lab

Лабораторная работа №5 по автоматизированному тестированию веб-приложений.

Проект содержит пять UI-тестов сайта [SauceDemo](https://www.saucedemo.com/), реализованных на Python с использованием Pytest и Playwright. Тесты запускаются локально и в GitHub Actions.

## Локальный запуск

```bash
python -m venv .venv
pip install -r requirements.txt
python -m playwright install chromium
pytest -v
```
