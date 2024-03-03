from Src.exceptions import exception_proxy, argument_exception

#
# Класс для описания настроек
#
class settings():
    __inn = ""
    __bank_account = ""
    __bic = ""
    __corresp_account = ""
    __prop_type = ""
    __short_name = ""
    __first_start = True
    __report_format = ""
    
    def restricted_len(value: str, restriction: int) -> None:
        if (len(value) > restriction):
            raise argument_exception("Не соблюдается ограничение длины аргумента")
    
    @property
    def inn(self) -> str:
        """
        ИНН организации, ограничение в 12 символов

        Returns:
            str:
        """
        return self.__inn
    
    @inn.setter
    def inn(self, value: str):
        exception_proxy.validate(value, str)
        settings.restricted_len(value, 12)
        self.__inn = value

    @property
    def bic(self) -> str:
        """
        БИК организации, ограничение 9 символов

        Returns:
            str: 
        """
        return self.__bic
    
    @bic.setter
    def bic(self, value: str):
        exception_proxy.validate(value, str)
        settings.restricted_len(value, 9)
        self.__bic = value
    
    @property
    def bank_account(self) -> str:
        """
        Банковский счет организации, ограничение 11 символов

        Returns:
            str: 
        """
        return self.__bank_account
    
    @bank_account.setter
    def bank_account(self, value: str):
        exception_proxy.validate(value, str)
        settings.restricted_len(value, 11)
        self.__bank_account = value
    
    @property
    def corresp_account(self) -> str:
        """
        Корреспондентский счет организации, ограничение 11 символов

        Returns:
            str: 
        """
        return self.__corresp_account
    
    @corresp_account.setter
    def corresp_account(self, value: str):
        exception_proxy.validate(value, str)
        settings.restricted_len(value, 11)
        self.__corresp_account = value
    
    @property
    def prop_type(self) -> str:
        """
        Тип собственности организации, ограничение 5 символов

        Returns:
            str: 
        """
        return self.__prop_type
    
    @prop_type.setter
    def prop_type(self, value: str):
        exception_proxy.validate(value, str)
        settings.restricted_len(value, 5)
        self.__prop_type = value
    
    @property     
    def short_name(self):
        """
            Короткое наименование организации
        Returns:
            str:
        """
        return self.__short_name
    
    @short_name.setter
    def short_name(self, value:str):
        exception_proxy.validate(value, str)
        self.__short_name = value
        
        
    @property    
    def is_first_start(self):
        """
           Флаг Первый старт
        """
        return self.__first_start    
            
    @is_first_start.setter        
    def is_first_start(self, value: bool):
        self.__first_start = value
    
    @property
    def report_format(self) -> str:
        """
        Формат отчета, CSV, Markdown или Json

        Returns:
            str:
        """
        return self.__report_format
    
    @report_format.setter
    def report_format(self, value: str):
        exception_proxy.validate(value, str)
        accepted = ["csv", "Markdown", "Json"]
        if value in accepted: 
            self.__report_format = value
        else:
            raise argument_exception("Неподдерживаемый формат отчета")