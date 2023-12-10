import time
from typing import Callable, Literal, Union

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import D, T, WebDriverWait


class CustomWait(WebDriverWait):
    def until(self, method: Callable[[D], Union[Literal[False], T]], message: str = "") -> T:
        """Calls the method provided with the driver as an argument until the \
        return value does not evaluate to ``False``.

        :param method: callable(WebDriver)
        :param message: optional message for :exc:`TimeoutException`
        :returns: the result of the last call to `method`
        :raises: :exc:`selenium.common.exceptions.TimeoutException` if timeout occurs
        """
        screen = None
        stacktrace = None
        reason = None

        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
                reason = getattr(exc, 'msg', None)
            except AssertionError as err:
                reason = err.args[0]
            time.sleep(self._poll)
            if time.monotonic() > end_time:
                break
        raise TimeoutException(
            message + f'\n\nTimeout: {self._timeout}\nReason: {reason}', screen, stacktrace
        )
