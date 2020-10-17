
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def test_set(request):

    dt = webdriver.Firefox(executable_path="C:\\Users\Alkesh\Desktop\PALAKH\geckodriver.exe")
    dt.implicitly_wait(5)

    dt.get("https://rahulshettyacademy.com/angularpractice/")
    dt.maximize_window()
    request.cls.dt = dt
    yield
    dt.close()

