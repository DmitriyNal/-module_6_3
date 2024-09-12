class Horse:
    def __init__(self):
        super().__init__()
        self.x_distance = 0  # пройденный путь
        self.sound = 'Frrr'  # звук лошади


    def run(self, dx):  # метод изменяющий дистанцию
        self.x_distance += dx
        return self.x_distance  # возвращает пройденный путь


class Eagle:
    def __init__(self):
        super().__init__()
        self.y_distance = 0  # высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # звук передаваемый орлом

    def fly(self, dy):
        self.y_distance += dy  # метод изменяющий высоту
        return self.y_distance  # возвращает высоту полета


class Pegasus(Horse, Eagle):# класс наследуется от класса лошади и орла
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)


    def move(self, dx, dy):## метод изменяющий полет объекта
        return self.run(dx),self.fly(dy)




    def get_pos(self):## метод возвращающий позицию объекта
            return self.x_distance, self.y_distance

    def voice(self):## метод возвращающий звук объекта
        print(self.sound)



p1 = Pegasus() # создание объекта класса Pegasus
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
print(Pegasus.mro())
