import asyncio
import random
from ..core.automation import AutomationCore, InteractionType

class BrowserAutomation(AutomationCore):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    async def _initialize_viewport_properties(self):
        await super()._initialize_viewport_properties(self.driver.save_screenshot)

    def get_center(self, element):
        asyncio.run(self._initialize_viewport_properties())

        element_location = element.location
        element_size = element.size

        return self._calculate_center_point(element_location, element_size)

    def move_to(self, element, offset_x=random.uniform(0.0, 1.5), offset_y=random.uniform(0.0, 1.5)):
        center = self.get_center(element)
        self._move_cursor(center, offset_x, offset_y)

    def click_at(self, element, click_type=InteractionType.LEFT):
        center = self.get_center(element)
        self._perform_click([center['x'], center['y']], click_type=click_type)

    def type_at(self, element, text, characters_per_minute=280, offset=20, click_type=InteractionType.LEFT):
        center = self.get_center(element)
        self._perform_click([center['x'], center['y']], click_type=click_type)
        self._simulate_typing(text, characters_per_minute, offset)

    def scroll_to(self, element):
        asyncio.run(self._initialize_viewport_properties())

        element_rect = element.rect
        self._smooth_scroll(element_rect)


class AsyncBrowserAutomation(AutomationCore):
    def __init__(self, page):
        super().__init__()
        self.page = page

    async def _initialize_viewport_properties(self):
        async def screenshot_func(path):
            await self.page.screenshot(path=path)
        await super()._initialize_viewport_properties(screenshot_func)

    async def get_center(self, element):
        await self._initialize_viewport_properties()

        rect = await element.boundingBox()
        if rect is None:
            return None

        return self._calculate_center_point(rect, rect)

    async def move_to(self, element, offset_x=random.uniform(0.0, 1.5), offset_y=random.uniform(0.0, 1.5)):
        center = await self.get_center(element)
        self._move_cursor(center, offset_x, offset_y)

    async def click_at(self, element, click_type=InteractionType.LEFT):
        center = await self.get_center(element)
        self._perform_click([center['x'], center['y']], click_type=click_type)

    async def type_at(self, element, text, characters_per_minute=280, offset=20, click_type=InteractionType.LEFT):
        center = await self.get_center(element)
        self._perform_click([center['x'], center['y']], click_type=click_type)
        self._simulate_typing(text, characters_per_minute, offset)

    async def scroll_to(self, element):
        await self._initialize_viewport_properties()

        element_rect = await element.boundingBox()
        if element_rect is None:
            return None

        self._smooth_scroll(element_rect)


class SeleniumAutomation(BrowserAutomation):
    pass

class PyppeteerAutomation(AsyncBrowserAutomation):
    pass

class PlaywrightAutomation(AsyncBrowserAutomation):
    pass 