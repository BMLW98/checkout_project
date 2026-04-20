# Checkout System
Simple Python checkout system which consumes a product set and generates Product Set objects containing Product objects. 

## How it works
Consumes a dataset for products by iterating through a dictionary, converting keys into product codes and tuples containing special unit/price to instantiate product and product_set objects that follow business logic. 

Discount prices are applied based on multiples of the second value in the product tuple, and remaining products not covered in a discount deal are calculated with a modulo operator.

### Set-up/Tests
```bash
git clone (github url)
cd checkout_project
pip install -r requirements.txt
pytest checkout_test.py
```

### Command examples
A basket and Product Set can be instantiated in the same command:

```
basket = Basket(Product_Set(pricing_dataset1))
```
This creates a basket instance, sets up a Product Set object and also instantiates the individual Product objects. From here, you can add products to the basket via inputting the product code and quantity:
```
basket.add_to_basket('A', 1)
```
The checkout() method returns the contents and subtotal of the basket:
```
basket.checkout()
# Your basket contains:
# Product A x 3
# Product B x 2
# Product C x 1
# Product D x 1

# Subtotal: £237.00
```

### Error Handling
If an incorrect product code is input when adding to basket, the program will print 'Invalid product code!' and end. A quantity of 1 or more is needed when adding products to the basket - otherwise 'Choose a quantity!' will be printed and the program will end.

Tests in checkout_test.py run through different variations of adding and checking out products, including special prices, special prices at high quantity, quantities that aren't an exact multiple of the discount quantity etc.

### Design decisions
Went via an Object-based approach instead of separate functions for better separation of concerns. Made some changes to the structure of the code in terms of the amount of classes. Originally had the checkout and basket elements of the program within the Product Set class, but added a separate basket class to allow for fresh instances each session. The totting up of the subtotal and return of the basket's contents were originally within the add_to_basket method, however this had flawed logic wherein adding products in a staggered way wouldn't calculate the discounts if staggered additions added up to a discounted quantity, so added this process to the checkout method instead.

Instantiation of the products set is limited as it requires inputting data into a dictionary - could be modified in future by using a library or framework to parse a separate database storing the product data, e.g. SQLite. 