from playwright.async_api import Page, Playwright

# Declared global variable of Request Payload for createorder
orderPayload = {"orders":[{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]}

class APIUtils:

    def getToken(self, playwright:Playwright, user_credentials):

        user_email = user_credentials['userEmail']
        user_password = user_credentials['userPassword']

        getRequestToken = {"userEmail": user_email, "userPassword": user_password}

        apiRequest_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = apiRequest_context.post("/api/ecom/auth/login",
                                           data = getRequestToken,
                                           headers = {"Content-Type": "application/json"})

        # check if the response code is 200 OK
        assert response.ok
        print(response.json())

        # get token data in the variable and return the same
        token = response.json()["token"]
        return token



    def createOrder(self, playwright:Playwright, user_credentials):

        # calling getToken function to get token variable value
        token = self.getToken(playwright, user_credentials)

        # call the URL found in the Headers > Request URL field in Network tab after placing an order
        apiRequest_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")

        # POST method used as mentioned in Request method field in Network tab
        response = apiRequest_context.post("/api/ecom/order/create-order",  # other part of the URL, to get to resources
                                           data = orderPayload, # sending payload as data
                                           headers = {"Content-Type": "application/json", # parse in JSON
                                                      "Authorization": token # Sending autorization token found as response of Login
                                                     })

        print(response.json())
        orderId = response.json()["orders"][0]
        return orderId

