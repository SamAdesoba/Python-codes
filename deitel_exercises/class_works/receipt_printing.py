total_products_bought = int(input("Enter the number of items bought: "))
product = []
for i in range(0, total_products_bought):
    product += [[(str(input("Enter the product: "))), (int(input("Enter the quantity: "))), (float(input("Enter the price per unit product"))), ((int(input("Enter the quantity: ")))*(float(input("Enter the price per unit product"))))]]
    print()
print("------------------------------------------------------------------------------------------------")
for i in product:
    print(i)
