import asyncio
import math
import os
import random
import tempfile
import time
import struct

try:
    import keyboard
except ImportError:
    keyboard = None

import pyautogui
from humancursor import SystemCursor
from enum import Enum

def _get_image_dimensions(file_path):
    with open(file_path, "rb") as file:
        file.seek(16)
        width_bytes = file.read(4)
        height_bytes = file.read(4)
        width = struct.unpack(">I", width_bytes)[0]
        height = struct.unpack(">I", height_bytes)[0]
        return (width, height)

class InteractionType(Enum):
    LEFT = 0
    RIGHT = 1
    MIDDLE = 2
    DOUBLE = 3

class AutomationCore:
    def __init__(self):
        self.cursor = SystemCursor()
        self.viewport_offsets = ()
        self.viewport_dimensions = ()

    async def _initialize_viewport_properties(self, screenshot_func):
        if not self.viewport_offsets or not self.viewport_dimensions:
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                temp_screen_path = temp_file.name
            if asyncio.iscoroutinefunction(screenshot_func):
                await screenshot_func(temp_screen_path)
            else:
                screenshot_func(temp_screen_path)

            location = pyautogui.locateOnScreen(temp_screen_path, confidence=0.6)
            if location is not None:
                self.viewport_offsets = (location.left, location.top)
            else:
                self.viewport_offsets = (0, 0)
            self.viewport_dimensions = _get_image_dimensions(temp_screen_path)
            os.remove(temp_screen_path)

    def _calculate_center_point(self, element_location, element_size):
        offset_x, offset_y = self.viewport_offsets if self.viewport_offsets else (0, 0)
        element_x = element_location["x"] + offset_x
        element_y = element_location["y"] + offset_y
        centered_x = element_x + (element_size["width"] // 2)
        centered_y = element_y + (element_size["height"] // 2)
        return {"x": centered_x, "y": centered_y}

    def _move_cursor(self, center, offset_x=None, offset_y=None):
        if offset_x is None:
            offset_x = random.uniform(0.0, 1.5)
        if offset_y is None:
            offset_y = random.uniform(0.0, 1.5)
        target_x = round(center["x"] + offset_x)
        target_y = round(center["y"] + offset_y)
        self.cursor.move_to([target_x, target_y])

    def _perform_click(self, coordinate, click_type=InteractionType.LEFT, click_duration=0):
        if click_type == InteractionType.LEFT:
            self.cursor.click_on(coordinate, click_duration=click_duration)
        elif click_type == InteractionType.RIGHT:
            pyautogui.click(x=coordinate[0], y=coordinate[1], button="right")
        elif click_type == InteractionType.MIDDLE:
            pyautogui.click(x=coordinate[0], y=coordinate[1], button="middle")
        elif click_type == InteractionType.DOUBLE:
            self.cursor.click_on(coordinate)
            time.sleep(0.1)
            self.cursor.click_on(coordinate)

    def _simulate_typing(self, text, characters_per_minute=280, offset=20):
        time_per_char = 60 / characters_per_minute
        for char in text:
            randomized_offset = random.uniform(-offset, offset) / 1000
            delay = time_per_char + randomized_offset
            if keyboard is None:
                pyautogui.press(char)
            else:
                keyboard.write(char)
            time.sleep(delay)

    def _smooth_scroll(self, element_rect):
        if self.viewport_dimensions:
            window_width, window_height = self.viewport_dimensions
        else:
            screen_size = pyautogui.size()
            window_width, window_height = screen_size.width, screen_size.height

        scroll_amount = element_rect["y"] - window_height // 2
        scroll_steps = abs(scroll_amount) // 100
        scroll_direction = -1 if scroll_amount > 0 else 1

        for _ in range(scroll_steps):
            pyautogui.scroll(scroll_direction * 100)
            time.sleep(random.uniform(0.05, 0.1))

        remaining_scroll = scroll_amount % 100
        if remaining_scroll != 0:
            pyautogui.scroll(scroll_direction * remaining_scroll)
            time.sleep(random.uniform(0.05, 0.1))

    def drag_and_drop(self, start_coords, end_coords):
        self.cursor.drag_and_drop(start_coords, end_coords) 