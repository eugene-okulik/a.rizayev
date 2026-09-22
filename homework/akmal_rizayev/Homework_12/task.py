class Flower:
    def __init__(self, life_time, freshness, color, length, price):
        self.life_time = life_time
        self.freshness = freshness
        self.color = color
        self.length = length
        self.price = price

    def __str__(self):
        return (f'Цветок живет {self.life_time} дней, свежесть: {self.freshness},'
                f' цвет: {self.color}, длина: {self.length}, цена: {self.price}')


class Rose(Flower):
    def __init__(self, life_time, freshness, color, length, price, country):
        super().__init__(life_time, freshness, color, length, price)
        self.country = country


class Magnolia(Flower):
    def __init__(self, life_time, freshness, color, length, price, size):
        super().__init__(life_time, freshness, color, length, price)
        self.size = size


class Dandelion(Flower):
    def __init__(self, life_time, freshness, color, length, price, stage):
        super().__init__(life_time, freshness, color, length, price)
        self.stage = stage


class Bouquet:
    def __init__(self, flowers_list):
        self.flowers = list(flowers_list)
        self.__full_price = sum((obj.price for obj in flowers_list))

    def get_price(self):
        return self.__full_price

    def get_avg_lifetime(self):
        return sum((flower.life_time for flower in self.flowers)) / len(self.flowers)

    def sort_by(self, param):
        self.flowers.sort(key=lambda x: getattr(x, param))

    def find_flower(self, param, value):
        for flower in self.flowers:
            if getattr(flower, param) == value:
                return f'Найден: {str(flower)}'
        else:
            return 'Не найден'

    def __str__(self):
        result = ''
        index = 1
        for flower in self.flowers:
            result += f'{index}: {str(flower)}\n'
            index += 1
        return result


flower_1 = Rose(2, 10, 'white', 50, 5.5, 'Russia')
flower_2 = Dandelion(5, 8, 'yellow', 48, 3.5, 2)
flower_3 = Magnolia(3, 6, 'purple', 30, 4.5, 'big')

bouquet_1 = Bouquet([flower_1, flower_2, flower_3])

bouquet_1.sort_by('life_time')

print(bouquet_1)

print(bouquet_1.find_flower('freshness', 6))
