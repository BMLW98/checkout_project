import checkout

def test_add_A_to_basket_and_checkout():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('A', 1)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 50

def test_add_B_to_basket_and_checkout():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('B', 1)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 35

def test_add_C_to_basket_and_checkout():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('C', 1)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 25

def test_add_D_to_basket_and_checkout():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('D', 1)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 12

def test_special_price_A():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('A', 3)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 140

def test_special_price_B():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('B', 2)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 60

def test_A_special_price_when_not_exactly_3():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('A', 4)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 190

def test_B_special_price_when_not_exactly_2():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('B', 3)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 95

def test_invalid_product_code():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('E', 1)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 0

def test_high_multiples_of_special_price():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('A', 60)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 2800

def test_mix_of_products():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('A', 1)
    user_basket.add_to_basket('B', 1)
    user_basket.add_to_basket('C', 1)
    user_basket.add_to_basket('D', 1)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 122

def test_mix_of_products_some_with_special_price():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('A', 3)
    user_basket.add_to_basket('B', 2)
    user_basket.add_to_basket('C', 1)
    user_basket.add_to_basket('D', 1)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 237
    
def test_mix_of_products_added_staggered():
    user_basket = checkout.Basket(checkout.Product_Set(checkout.pricing_dataset1))
    user_basket.add_to_basket('A', 1)
    user_basket.add_to_basket('B', 1)
    user_basket.add_to_basket('A', 2)
    user_basket.checkout()
    result = user_basket.subtotal
    assert result == 175