class Restaurant():
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_table(self, table_number):
        self.book_table.append(table_number)

    def customer_order(self, table_number, order):
        order_details = {'tab'}            