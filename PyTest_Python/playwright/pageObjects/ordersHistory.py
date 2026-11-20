from pageObjects.orderDetails import *

class OrdersHistoryPage:

    def __init__(self, page):
        self.page = page

    def selectAndViewOrder(self, orderId):
        orderIdRow = self.page.locator("tr").filter(has_text=orderId)  # use the value of order id object
        orderIdRow.get_by_role("button", name="View").click()

        orderDetailsPage = OrderDetailsPage(self.page)
        return orderDetailsPage