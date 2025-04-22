# Пример минимального проекта с использованием ядра pyqaunicore
## Приведены следующие примеры тестов:
- API-тесты (HTTP)
- API-тесты (WS)
- UI-тесты
- работа с DB
- скриншотные тесты

## Запуск тестов
```
.venv\Scripts\python.exe -m pytest -v
```

## Для перехода с Playwright на Selene нужно:
1. В conftest.py раскомментировать плагин для Playwright и закомментировать для Selene
2. Удалить пакет pytest-playwright
3. Раскомментировать нужный импорт в ui\ui_engine.py

## Для перехода с Selene на Playwright нужно:
1. В conftest.py раскомментировать плагин для Selene и закомментировать для Playwright
2. Установить пакет pytest-playwright
3. Раскомментировать нужный импорт в ui\ui_engine.py