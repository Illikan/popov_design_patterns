from abc import ABC
from Src.settings import settings
from Src.exceptions import exception_proxy, operation_exception
class reporting(ABC):
    # Настройки
    __settings: settings = None
    # Набор данных
    __data = {}
    # Поля
    __fields = []
    def __init__(self, _setting: settings, _data):
        """

        Args:
            _setting (settings): Настройки
            _data (_type_): Словарь с данными
        """
        exception_proxy.validate(_setting, settings)
        exception_proxy.validate(_data, dict)
        
        self.__data = _data
        self.__settings = _setting
    
    #@ABC.__abstractmethods__
    def create(self, typeKey: str):
        """
        Сформировать отчет

        Args:
            typeKey (str): Ключ тип данных
        """
        exception_proxy.validate(typeKey, str)
        self.__fields = self.build(typeKey, self.data)
        pass
    
    @staticmethod
    def build(typeKey: str, data: dict) -> list:
        """
        Предобработка. Получить набор полей

        Args:
            typeKey (str): ключ в словаре
            data (dict): _description_

        Raises:
            operation_exception: _description_
            operation_exception: _description_

        Returns:
            list: _description_
        """
        exception_proxy.validate(typeKey, str)
        if data is None:
            raise operation_exception("Набор данных не определен")
        if len(data) == 0:
            raise operation_exception("Набор данных пуст!")
        
        item = data[typeKey][0]
        result = list(filter(lambda x: x.startswith("_") and not x.startswith("__"), dir(item)))        

        return result
    
    def _build(self, typeKey: str) -> list:
                
        """
        Предобработка данных. Возвращает нбор полей класса typeKey

        Returns:
            _type_: _description_
        """
        return reporting.build(typeKey, self.__data)
    
    @property
    def fields(self) -> list:
        """
        Набор полей от исходного объекта на основании которого формируем отчет

        Returns:
            _type_: _description_
        """
        return self.__fields
    
    @property
    def data(self) -> dict:
        """
        Набор данных

        Returns:
            dict: _description_
        """
        return self.__data