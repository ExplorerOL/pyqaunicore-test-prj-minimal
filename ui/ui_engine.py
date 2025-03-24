"""Модуль браузерного клиента"""

from pyqaunicore.ui import UIEngineContext  # noqa: F401

# ------------------------------------------------------------------
# Раскомментировать для работы с Playwright
from pyqaunicore.ui.ui_engine.ui_engine_playwright import UIEnginePlaywright as UIEngine  # noqa: F401
# ------------------------------------------------------------------
# Раскомментировать для работы с Selene (проверено с Selene 2.0.0rc9)
# from pyqaunicore.ui.ui_engine.ui_engine_selene import UIEngineSelene as UIEngine  # noqa: F401
