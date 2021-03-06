import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_adoption(parser):
    parser.adoption("--browser", action="store", default="firefox")
    parser.adoption("--baseURL", action="store", default="http://localhost/addressbook/addressbook/")