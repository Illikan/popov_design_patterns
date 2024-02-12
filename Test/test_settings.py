from settings import settings
from settings_manager import  settings_manager
import unittest

#filepath = r"C:\Users\ze_us\Documents\VSProjects\Shab_proek_2_sem\settings.json"
filepath = "setings.json"
class test_settings(unittest.TestCase):
    
    def test_check_create_manager(self):
        # Подготовка
        manager1 = settings_manager()
        manager2 = settings_manager()
        
        # Действие
        
        # Проверки
        print(str(manager1.number))
        print(str(manager2.number))
    
        assert manager1.number == manager2.number
    
    #
    # Провеиить корректность заполнения поля first_name
    #
    def test_check_first_name(self):
        # Подготовка
        item = settings()
        
        # Действие
        item.first_name = "a  "
        
        # Проверка
        assert item.first_name == "a"
        
    def test_check_manager_convert(self):
        # Подготовка
        manager = settings_manager()
        manager.open(filepath)
         
        # Действие
        manager.convert()       
        
        # Проверка    
        
    def test_check_open_settings(self):
        # Подготовка
        manager = settings_manager()
        
        # Действие
        result = manager.open(filepath)
        
        # Проверка
        print(manager.data)
        assert result == True
        
                
        
        