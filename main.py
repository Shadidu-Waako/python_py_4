class Customer:
    def __init__(self, name, type_of_customer):
        self.name = name
        self.type_of_customer = type_of_customer
        self.payment = Payment(self, None)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.payment = Payment(self, None)

class Payment:
    def __init__(self, payment_method, customer):
        self.payment_method = payment_method
        self.customer = customer

    def calculate_discount(self, product):
        if self.customer.type_of_customer == 'daily':
            return product_input.price * 0.10
        else:
            return 0

number_of_customers = int(input('Enter the number of customers: '))

for i in range(number_of_customers):
    print(f'\nEnter customer {i + 1} details')
    customer_input = Customer(input('Customer Name: ',), input('Customer type: daily or one-time: '))

    payment_input = Payment(input('Payment method: '), customer_input)

    product_input = Product(input('Product Name: '), int(input('Product price: ')))

    print(f'{customer_input.name} is a {customer_input.type_of_customer} customer and gets a discount of {payment_input.calculate_discount(product_input.name)} on {product_input.name} and payed {product_input.price} in {payment_input.payment_method}\n')

