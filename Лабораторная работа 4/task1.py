if __name__ == "__main__":
    # Write your solution here
    class Spell:
        """Базовый класс заклинаний"""
        def __init__(self, name: str, dmg: int, cost: int, cd: int, modifier: float):
            """

            :param name: название заклиниания
            :param dmg: урон наносимый заклинанием
            :param cost: стоимость произнесения заклинания(количество ресурса, например маны)
            :param cd: время перезарядки заклинания в секундах
            :param modifier: процент(в долях), на который улучшаются все параметры заклинания при его улучшении
            lvl: уровень заклинания, начинается с 1
            все параметры заклинания инкапсулированны для того чтобы подчеркнуть, что вне класса они не меняются
            изменения базовых параметров происходят только при улучшении заклинания
            """
            self._name = name
            self._dmg = dmg
            self._cost = cost
            self._cd = cd
            self._modifier = modifier
            self._lvl = 1
        # Для доступа к базовым параметрам заклинаний используются свойства

        @property
        def name(self):
            return self._name

        @property
        def dmg(self):
            return self._dmg

        @property
        def cost(self):
            return self._cost

        @property
        def cd(self):
            return self._cd

        @property
        def lvl(self):
            return self._lvl
        # для модификатора нет свойства, так как к нему нет обращений вне класса

        def cast(self, target):
            # я предполагаю, что цель заклинания - это тоже будет класс
            # и так как у меня нет подходящего класса, я оставил аннотацию пустой
            """
            Это метод, который применяет заклинание к выбранной цели
            :param target: цель, на которую применяют заклинание
            внутри метода зашиты все модификаторы. которые применяются на параметры заклинания
            (сопротивления цели, бафы, дебафы и т.п.)
            """
            ...

        def upgrade(self):
            """
            Это метод, который улучшает заклинание
            логика работы простая - все параметры заклинания увеличиваются на процент, равный модификатору
            само собой, аттрибут name не изменяется)
            """
            ...

        def __str__(self):
            return f"Заклинание {self.name} {self.lvl} уровня" \
                   f"Урон {self.dmg}" \
                   f"Стоимость {self.cost}" \
                   f"Перезарядка {self.cd}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, level={self.lvl!r}, damage={self.dmg!r}, " \
                   f"cost={self.cost!r}, cooldown={self.cd!r}, modifier={self._modifier!r}"


    class FrostSpell(Spell):
        """
        Класс ледяных заклинаний
        Особенность в том,что они замедляют врагов
        """
        def __init__(self, name: str, dmg: int, cost: int, cd: int, modifier: float, slow: float, duration: int):
            """
            :param slow: процент, на который замедляется цель заклинания
            :param duration: длительность замедления в секундах
            """
            super().__init__(name, dmg, cost, cd, modifier)
            self._slow = slow
            self._duration = duration

        @property
        def slow(self):
            return self._slow

        @property
        def duration(self):
            return self._duration

        def cast(self, target):
            """
            Данный метод перегружается, так как в базовом классе не реализовано наложение дебафа на цель.
            """
            ...

        def __str__(self):
            return f"Заклинание {self.name} {self.lvl} уровня" \
                   f"Урон {self.dmg}" \
                   f"Стоимость {self.cost}" \
                   f"Перезарядка {self.cd}" \
                   f"Описание:" \
                   f"Замедляет передвижение цели на {self.slow * 100} % на {self.duration} секунд"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, level={self.lvl!r}, damage={self.dmg!r}, " \
                   f"cost={self.cost!r}, cooldown={self.cd!r}, modifier={self._modifier!r}, slow={self.slow!r}" \
                   f"duration={self.duration!r}"
    pass
