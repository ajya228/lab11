#Добавьте в созданный класс Restaurant атрибут, задающий начальный рейтинг ресторана и метод, который получает на вход новое значение рейтинга и обновляет
# его.
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type, rating=5):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
    def describe_restaurant (self):
        print(f"Название ресторана: {self.restaurant_name}\n"
              f"Тип кухни:    {self.cuisine_type}\n"
              f"Рейтинг ресторана: {self.rating}")
    def open_restaurant (self):
        print (f"Ресторан {self.restaurant_name} открыт!")
    def update_rating (self, updated_rating):
        if 0<= updated_rating <= 5:
            self.rating = updated_rating
            print(f"Рейтинг ресторана {self.restaurant_name} теперь: {self.rating}\n")
        else:
            print("Рейтинг вне диапазона")

restaurant_1 = Restaurant('Slurp Ramen', 'Японская кухня', 4.7)
restaurant_2 = Restaurant('Хачапури и Вино', 'Грузинская кухня', 4.6)
restaurant_3 = Restaurant('Теремок', 'Русская кухня', 4.5)

restaurant_3.update_rating (4.4)
restaurant_1.update_rating(4.9)
restaurant_2.update_rating(4.5)

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()