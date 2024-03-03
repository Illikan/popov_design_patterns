import sys
sys.path.append('c:\\Users\\ze_us\\Documents\\VSProjects\\Shab_proek_2_sem\\gitclone\\popov_design_patterns')

import abc
from Src.settings import settings
from Src.Storage import storage
from Src.exceptions import exception_proxy, operation_exception
from Src.reference import reference
#import json

class reporting(abc.ABC):
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
        
    
    #@abc.abstractclassmethod
    def create(self, typeKey: str) -> str:
        """
        Сформировать отчет

        Args:
            typeKey (str): Ключ тип данных
        """
        exception_proxy.validate(typeKey, str)
        self.__fields = self.build(typeKey, self.__data)
        
        return ""
    
    @staticmethod
    def make_element(attr) -> str:
        """
            Вспомогательная функция для нахождения значения атрибута
        """
        if isinstance(attr, reference):
            return attr.name
        elif attr is None:
            return " "
        elif isinstance(attr, str):
            if len(attr) > 0:
                return attr
        elif isinstance(attr, (int, bool)):
            return str(attr)
    
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
        result = list(filter(lambda x: not x.startswith("_") and not x.startswith("create_") and not x.startswith("is_") and not x == "description", dir(item)))        
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