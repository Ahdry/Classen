class Store:
    def __init__(self, name, address):
        self.name = name  # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Ассортимент товаров (словарь: товар -> цена)

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Возвращает цену товара по его названию."""
        return self.items.get(item_name, None)  # Возвращает None, если товар отсутствует

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def __str__(self):
        """Возвращает строковое представление магазина."""
        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {self.items}"


# Создаем несколько магазинов
store1 = Store("Продуктовый рай", "ул. Ленина, 10")
store2 = Store("ТехноМир", "пр. Мира, 25")
store3 = Store("Модный стиль", "ул. Пушкина, 5")

# Добавляем товары в магазины
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store1.add_item("молоко", 1.2)

store2.add_item("ноутбук", 50000)
store2.add_item("смартфон", 30000)

store3.add_item("платье", 2500)
store3.add_item("джинсы", 1800)

# Тестируем методы на одном из магазинов
print(store1)  # Выводим информацию о магазине

# Добавляем новый товар
store1.add_item("хлеб", 0.8)
print("После добавления хлеба:", store1.items)

# Обновляем цену товара
store1.update_price("яблоки", 0.6)
print("После обновления цены яблок:", store1.items)

# Удаляем товар
store1.remove_item("бананы")
print("После удаления бананов:", store1.items)

# Получаем цену товара
price = store1.get_price("молоко")
print(f"Цена молока: {price}")

# Пытаемся получить цену отсутствующего товара
price = store1.get_price("апельсины")
print(f"Цена апельсинов: {price}")