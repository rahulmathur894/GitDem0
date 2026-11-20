#Fixtures

import pytest

#@pytest.fixture
#def preWork():
#    print("I setup browser instance")

#def test_initialCheck(preWork):
#    print("This is first test.")


#@pytest.fixture (scope="function") # runs before each function
#def preWork():
#    print("I setup function instance")

#def test_initialCheck(preWork):
#    print("This is first test.")

#def test_secondCheck(preWork):
#    print("This is second test.")


#@pytest.fixture (scope="module") # runs ONCE
#def preWork():
    #print("I setup module instance")

#def test_initialCheck(preWork):
    #print("This is first test.")

#def test_secondCheck(preSetupWork):
    #print("This is second test.")


# Return data from Fixture

#@pytest.fixture (scope="module")
#def preWork():
 #   print("I setup preWork instance")

#@pytest.fixture(scope="function")
#def secondPreWork():
#    print("I setup second pre Work instance")
 #   return "Pass" # returns values/results, can be of any data type

#def test_initialCheck(preWork, secondPreWork):
#    print("This is first test.")
#    assert secondPreWork == "Fail" # returned result will not match and the test will fail
#    assert secondPreWork == "Pass"  # returned result will match and the test will pass

#def test_secondCheck(preSetupWork, secondPreWork):
#    print("This is second test.")


# yield keyword (tear down)

#@pytest.fixture(scope="function")
#def secondWork():
#    print("I setup second Work instance")
#    yield
#    print("Tear down validation")

#def test_initialCheck(secondWork):
#    print("This is first test.")

#def test_secondCheck(secondWork):
#    print("This is second test.")


# Running tests through command line and mark & skip pytest commands

@pytest.fixture(scope="function")
def secondWork():
    print("I setup second Work instance")
    yield
    print("Tear down validation")

@pytest.mark.smoke # custom markers should be defined in pytest.ini file in order to prevent warnings
def test_initialCheck(secondWork):
    print("This is first test.")

@pytest.mark.skip
def test_secondCheck(secondWork):
    print("This is second test.")
