import pytest
from lab2.src.driver.driver_factory import DriverFactory


@pytest.fixture(scope="session")
def browser():
    driver = DriverFactory('chrome').get_driver_instance()
    yield driver
    driver.quit()
