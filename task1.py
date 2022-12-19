from typing import Union
import doctest


class Battery:
    def __init__(self, capacity: int, current_capacity: Union[int, float]):
        """
        Инициализация объекта "Батарея"

        :param capacity: Максимальная ёмкость батареи в Ач. Обычно указывается целым числом
        :param current_capacity: Текущее значение ёмкости в Ач. Может быть дробным.

        Пример:
        >>> laptop_battery = Battery(28, 0.05) # инициализация экземпляра
        """
        if not isinstance(capacity, int):
            raise TypeError("Значение ёмкости должно быть целым числом")
        if capacity <= 0:
            raise ValueError("Значение ёмкости должно быть положительным")
        self.capacity = capacity
        if not isinstance(current_capacity, (int, float)):
            raise TypeError("Значение текущей ёмкости должно быть int или float")
        if current_capacity <= 0:
            raise ValueError("Значение текущей ёмкости не может быть меньше нуля")
        if current_capacity > capacity:
            raise ValueError("Значение текущей ёмкости не может превышать ёмкость батареи")
        self.current_capacity = current_capacity

    def charge_discharge(self, charging_current: Union[int, float], time: int) -> None:
        """
        Функция заряжающая или разряжающая батарею.
        Зарядка идет постоянным током в течении некоторого времени.

        :param charging_current: ток зарядки, если >0 или разрядки, елси <0 в мА
        :param time: время зарядки/разрядки в секундах
        :raise ValueError: если происходит перезаряд/переразряд
        Пример:
        >>> battery1 = Battery(20, 10)
        >>> battery1.charge_discharge(60, 1800)
        """
        if not isinstance(charging_current, (int, float)):
            raise TypeError("Значение тока должно быть int или float")
        if charging_current == 0:
            raise ValueError("Значение тока  не может быть нулем")
        if not isinstance(time, int):
            raise TypeError("Значение времени должно быть целым")
        if time < 0:
            raise ValueError("Значение времени не может быть меньше нуля")
        ...

    def state_of_charge(self) -> float:
        """
        функция возвращает текущий заряд в процентах от максимального
        :return: Текущий процент заряда в виде доли
        Пример
        >>> battery1 = Battery
        >>> battery1.state_of_charge()
        """
        ...


class Engine:
    def __init__(self, max_speed: int, torgue: int):
        """
        Инициализация обьекта "Двигатель"
        :param max_speed: максимальная скорость двигателя в об/мин (rpm)
        :param torgue: крутящий момент двигателя в Нм
        Пример
        >>> motor1 = Engine(3000, 20)
        """
        if not isinstance(max_speed, int):
            raise TypeError("Значение максимальной скорости должно быть целым числом")
        if max_speed <= 0:
            raise ValueError("Значение максимальной скорости должно быть положительным")
        self.max_speed = max_speed
        if not isinstance(torgue, int):
            raise TypeError("Значение крутящего момента должно быть целым числом")
        if torgue <= 0:
            raise ValueError("Значение крутящего момента должно быть положительным")
        self.torque = torgue

    def start_engine(self) -> None:
        """
        Функция запускает двигатель
        :raise ValueError если двигатель уже запущен

        Пример
        >>> motor1 = Engine(3000, 20)
        >>> motor1.start_engine()
        """
        ...

    def calculate_power(self) -> int:
        """
        Функция расчитываетмощность двигателя
        :return: значение мощности в ваттах
        Пример
        >>> motor1 = Engine(3000, 20)
        >>> power = motor1.calculate_power()
        """
        ...


class Transmission:
    def __init__(self, stages_number: int, current_stage: int, gear_ratio: Union[int, float]):
        """
        Инициализация объекта "Коробка передач"
        :param stages_number:число ступеней в коробке
        :param current_stage: текущая ступень. 0 соответвует нейтральному положению
        :param gear_ratio: передаточное отношение между ступенями. Будем считать, что оно постоянное между ступенями
        Пример
        >>> speed_box = Transmission(5, 1, 1.5)
        """
        if not isinstance(stages_number, int):
            raise TypeError("Значение числа передач должно быть целым числом")
        if stages_number <= 0:
            raise ValueError("Значение числа передач должно быть положительным")
        self.stages_number = stages_number
        if not isinstance(current_stage, int):
            raise TypeError("Номер текущей передачи должен быть целым числом")
        if current_stage < 0:
            raise ValueError("Номер текущей передачи не должен быть отрицательным")
        if current_stage > stages_number:
            raise ValueError("Номер текущей передачи не должен превышать число ступеней")
        self.current_stage = current_stage
        if not isinstance(gear_ratio, (int, float)):
            raise TypeError("Передаточное отношение должно быть int или float")
        if gear_ratio <= 0:
            raise ValueError("Передаточное отношение должно быть положительным")

    def change_stage(self, increment: int) -> None:
        """
        Функция переключает коробку на заданное число ступеней
        :param increment: число переключаемых ступеней.
        Если >0 - повышение, если <0 - понижение
        :raise ValueError: если при переключении уйдем за пределы существующих передач
        Пример
        >>> speed_box = Transmission(5, 1, 1.5)
        >>> speed_box.change_stage(3)
        """
        if not isinstance(increment, int):
            raise TypeError("Можно переключить только целое число пердач")
        ...

    def calculate_current_gear_ratio(self) -> Union[int, float]:
        """
        функция вычисляет текущее передаточное число
        :return: возвращает передаточное число на текущей ступени
        Пример
        >>> speed_box = Transmission(5, 1, 1.5)
        >>>> reduction = speed_box.calculate_current_gear_ratio()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
