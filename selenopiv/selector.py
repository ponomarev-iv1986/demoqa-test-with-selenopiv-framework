from typing import Tuple

from selenium.webdriver.common.by import By


def to_locator(selector: str) -> Tuple[str, str]:
    return (By.XPATH, selector) if (
            selector.startswith('/')
            or selector.startswith('//')
            or selector.startswith('./')
            or selector.startswith('..')
            or selector.startswith('(')
    ) else (By.CSS_SELECTOR, selector)
