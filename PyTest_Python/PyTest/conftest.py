import pytest

@pytest.fixture (scope="session") # scope = session runs once per session, means once before all the files are executed in the directory
def preSetupWork():
    print("I setup session instance")