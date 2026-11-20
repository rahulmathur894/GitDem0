import pytest

# Setup fixture to register the options we want to pass for different browser through command line (given on doc.pytest website)

def pytest_addoption(parser): # adding parser method
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
        # '--' is important to make it identify it as configuration option
        # help is option, does not matter if we dont pass
    )
    # similarly we can do for URL selection
    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client", help="url selection"
        # '--' is important to make it identify it as configuration option
        # help is option, does not matter if we dont pass
    )

@pytest.fixture(scope='session')
def user_credentials(request): # 'request' here is global request parameter
    return request.param

@pytest.fixture
def browserInstance(playwright, request):
    # getting access to configuration variables which are at the global level through .config method
    browser_name = request.config.getoption('browser_name')
    url_name=request.config.getoption('url_name')

    if browser_name == 'chrome':
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == 'edge':
        browser = playwright.chromium.launch(headless=False, channel='msedge')
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()
    # page.goto(url_name)

    yield page
    context.close()
    browser.close()