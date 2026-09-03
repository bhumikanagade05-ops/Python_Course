# # 25. Shopping Cart Module

# cart = []


# def add_product(name, price, quantity):
#     product = {
#         "name": name,
#         "price": price,
#         "quantity": quantity
#     }

#     cart.append(product)


# def remove_product(name):

#     for product in cart:

#         if product["name"].lower() == name.lower():
#             cart.remove(product)
#             print("Product removed.")
#             return

#     print("Product not found.")


# def calculate_total():

#     total = 0

#     for product in cart:
#         total += product["price"] * product["quantity"]

#     return total


# def display_cart():

#     if len(cart) == 0:
#         print("Cart is empty.")
#         return

#     print("\n----- CART -----")

#     for product in cart:

#         subtotal = product["price"] * product["quantity"]

#         print(
#             product["name"],
#             "- ₹", product["price"],
#             "x", product["quantity"],
#             "= ₹", subtotal
#         )

#     print("Total = ₹", calculate_total())



# OUTPUT:
# ----- SHOPPING CART -----
# 1. Add Product
# 2. Remove Product
# 3. Display Cart
# 4. Calculate Total
# 5. Exit
# Enter choice: 1
# Enter product name: beauty products
# Enter price: 2000
# Enter quantity: 2
# Product added.
