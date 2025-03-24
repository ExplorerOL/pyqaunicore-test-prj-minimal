# Пример минимального проекта с использованием pyqaunicore

## Запуск тестов
```
.venv\Scripts\python.exe -m pytest -v
```

## Для перехода с Playwright на Selene нужно:
1. В conftest.py раскомментировать соотвествующий плагин
2. Удалить пакет pytest-playwright
3. Раскомментировать нужный импорт в ui\ui_engine.py