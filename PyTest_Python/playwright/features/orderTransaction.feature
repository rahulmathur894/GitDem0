Feature: Order Transaction
  Tests related to Order Transaction

  #Scenario outline specifies that an input is needed in the scenario
  Scenario Outline: Verify order success message shown in details page

    Given Open the browser, navigate to URL and login with <username> and <password>
    And the user is on landing page

    When I click on Orders menu option
    And Orders page is displayed, select the orderID

    Then Check the order success message is displayed

    Examples:
      | username              | password  |
      | rahulmathur@gmail.com | Rahul@123 |