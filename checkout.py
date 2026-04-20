pricing_dataset1 = {
    'A': {'unit_price': 50, 'spec': (3, 140)},
    'B': {'unit_price': 35, 'spec': (2, 60)},
    'C': {'unit_price': 25, 'spec': None},
    'D': {'unit_price': 12, 'spec': None}
}

class Product:
    def __init__(self, item_code: str, unit_price: float, special_price: tuple):
        '''Create a Product class that accepts an item code, unit price and special price/discount.'''
        self.item_code = item_code
        self.unit_price = unit_price
        self.special_price = special_price

class Product_Set:
    def __init__(self, pricing_dataset: dict):
        '''Create a Product Set class that populates sets of products based on a data set. includes tracking of basketed items and basket subtotal'''
        self.products = []
        for i in pricing_dataset.keys():
            self.products.append(Product(i, pricing_dataset[i]['unit_price'], pricing_dataset[i]['spec']))

    def __str__(self):
        '''Create string representation to check the contents of the product set object.'''
        string_rep = ''
        for i in self.products:
            string_rep += i.item_code + ' ' + str(i.unit_price) + ' ' + str(i.special_price) + '\n'
        return str(string_rep)

class Basket:
    def __init__(self, product_set: Product_Set):
        self.basketed_items = {}
        self.subtotal = 0
        self.product_set = product_set
        self.basket_string = ''

    def add_to_basket(self, item_code: str, unit_num: int):
        '''Adds a product to basket list - iterates through a Product Set's item codes.
        Adds it to the basket if it matches item code argument.'''
        # check if product code is valid
        correct_code = False
        if unit_num < 0:
            print('Choose a quantity!')
            return
        for i in self.product_set.products:
            if i.item_code == item_code:
                correct_code = True
        if not correct_code:
            print('Invalid product code!')
            return
        for i in self.product_set.products:
            if i.item_code == item_code:
                if item_code not in self.basketed_items.keys():
                    self.basketed_items[item_code] = unit_num
                else:
                    self.basketed_items[item_code] += unit_num

    def checkout(self):
        '''Iterates through the basketed items and calculates the subtotal. If a product has a special price, it calculates how many deals can be applied and how many units are
        left at the normal price, then adds these together to get the total for that product.'''
        for i in self.basketed_items.keys():
            for j in self.product_set.products:
                if j.item_code == i:
                    self.basket_string += f'Product {i} x {self.basketed_items[i]}\n'
                    if j.special_price is None:
                        self.subtotal += j.unit_price * self.basketed_items[i]
                    else:
                        deals = (self.basketed_items[i] // j.special_price[0])
                        non_discounted_units = self.basketed_items[i] % j.special_price[0]
                        self.subtotal += (deals * j.special_price[1]) + (non_discounted_units * j.unit_price)

        return f'Your basket contains:\n{self.basket_string}\nSubtotal: £{self.subtotal:.2f}'
    
