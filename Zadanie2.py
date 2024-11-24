#На основе ранее созданного класса Restaurant из задания 11.1 создайте три разных экземпляра (три ресторана), вызовите для каждого экземпляра метод
# describe_restaurant().
from Zadanie1 import Restaurant

restaurant_1 = Restaurant('Slurp Ramen', 'Японская кухня')
restaurant_2 = Restaurant('Хачапури и Вино', 'Грузинская кухня')
restaurant_3 = Restaurant('Теремок', 'Русская кухня')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

print(restaurant_1, restaurant_2, restaurant_3)