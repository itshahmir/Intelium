from .core import AutomationCore, InteractionType
from .browser import (
    BrowserAutomation,
    AsyncBrowserAutomation,
    SeleniumAutomation,
    PyppeteerAutomation,
    PlaywrightAutomation
)
from .desktop import DesktopAutomation

__version__ = '1.0.0'

__all__ = [
    'AutomationCore',
    'InteractionType',
    'BrowserAutomation',
    'AsyncBrowserAutomation',
    'SeleniumAutomation',
    'PyppeteerAutomation',
    'PlaywrightAutomation',
    'DesktopAutomation'
]