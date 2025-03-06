import pytest
from selenium import webdriver
from _pytest.config import Config
# from pytest_html.plugin import metadata_key as pytest_html_metadata_key

@pytest.fixture()
def setup(browser):
    if browser=="Chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Edge()
        return driver

    yield driver  # Ensure driver is returned
    driver.quit()  # Close browser after test execution

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request) :
    return request.config.getoption("--browser")





@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)
    metadata.pop("Plugins", None)

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session: Config, exitstatus):
    metadata = getattr(session.config, '_metadata', None)
    if metadata is not None:
        metadata["Project Name"] = "Mercury Tours"


