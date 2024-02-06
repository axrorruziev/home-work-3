all_product = {"весь склад": {}}
while True:
    admin = input(" что хотите сделать?(добавить//продукты/продукты в корзине/добавить в корзину/выход)")
    if admin == "добавить":
        product_name = input("введите названия продукта:")
        product_count = input("введите количевство продуктов:")
        all_product["весь склад"][product_name] = int(product_count)
        print(f"продукт {product_name} успешно добавлен ")

    elif admin =="продукты":
       print("список продуктов и их количевство")
       for product,count in all_product["весь склад"].items():
         print(f"{product}:{count}")

    elif admin == "продукты в корзине":
      print("список продуктов и их количевство в корзине")
      for product, count in all_product["весь склад"].items():
         print(f"{product}:{count} /в корзине/")

    elif admin == "добавить в корзину":
        product_name = input("введите названия продукта:")
        product_count = input("введите количевство продуктов:")
        all_product["весь склад"][product_name] = int(product_count)
        print(f"продукт {product_name} успешно добавлен  в корзину")

