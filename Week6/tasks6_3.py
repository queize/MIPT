# Данная задача является продолжением задач № 1 и 2, для ее реализации потребуется класс Player, описанный в задании № 1.

# Работа над игрой идет полным ходом, и пришло время добавить нашим игрокам суперспособности. Ваш гейм-дизайнер после проведенного тщательного анализа заявил, что суперспособности должны быть двух видов: физические и магические.
# Физические суперспособности можно использовать ограниченное число раз, в то время как магические никогда не исчерпываются. При этом каждое использование магической суперспособности добавляет к счету игрока 1 очко.

# Ваша задача — реализовать один базовый класс Power для представления любых суперспособностей и два производных класса PhysicalPower и MagicPower для представления указанных двух разновидностей.

# Класс Power должен определять два атрибута (получив соответствующие параметры в конструктор)

# ●     name (название суперспособности),

# ●     cost (цена).

# Для всех классов должен быть реализован метод use, принимающий в качестве параметра объект Player — игрок, который применяет данную способность (воспользуйтесь классом Player, реализованным в первом задании). Метод use должен вывести на экран сообщение:

# "<имя игрока> used <название суперспособности>", если игрок может использовать данную способность, или

# "<имя игрока> cannot use <название суперспособности>", если она уже израсходована.

# Например, если игрок с именем "Mario" использует способность "teleport", на экран должно быть выведено: "Mario used teleport".

# Вы можете добавить другие атрибуты и методы своим классам, если это нужно для решения задачи, но проверяться будет только работа метода used.

# Конструктор класса PhysicalPower дополнительным аргументом должен принимать количество возможных использований данной способности. Класс PhysicalPower должен дополнительно реализовать подсчет количества использований, а класс MagicPower при каждом использовании увеличивать player.scores на 1.

# Пример работы программы:

# p = Player(1, 'Bilbo')                        ⇒
# t = PhysicalPower('teleport', 10, count=1)    ⇒
# t.use(p)                                      ⇒ Bilbo used teleport
# t.use(p)                                      ⇒ Bilbo cannot use teleport
# print(p.scores)                               ⇒ 0
 
# b = MagicPower('black magic', 200)            ⇒
# b.use(p)                                      ⇒ Bilbo used black magic
# print(p.scores)                               ⇒ 1
# b.use(p)                                      ⇒ Bilbo used black magic
# print(p.scores)                               ⇒ 2

from tasks6_1 import Player
from dataclasses import dataclass
class Power:
    name: str
    cost: int
    player: Player

    def __init__(self, name: str, cost: int) -> None:
        self.name = name
        self.cost = cost

    def use(self, player: Player) -> None:
        pass

@dataclass
class PhysicalPower(Power):
    count: int

    def __init__(self, name: str, cost: int, count: int) -> None:
        super().__init__(name, cost)
        self.count = count

    def use(self, player: Player) -> None:
        if self.count > 0:
            print(f'{player.name} used {self.name}')
            self.count -= 1
        else:
            print(f'{player.name} cannot use {self.name}')

class MagicPower(Power):
    def use(self, player: Player) -> None:
        print(f'{player.name} used {self.name}')
        player.scores += 1

p = Player(1, 'Bilbo')  
t = PhysicalPower('teleport', 10, count=1) 
t.use(p)
t.use(p)
print(p.scores) 

b = MagicPower('black magic', 200)           
b.use(p)                                    
print(p.scores)                              
b.use(p)                                      
print(p.scores)   
