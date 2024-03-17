from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.Logics.report_factory import report_factory
from Src.Logics.process_factory import process_factory
import unittest

#
# Набор автотестов для проверки работы фабричного метода
# 
class factory_test(unittest.TestCase):

    # 
    # Проверить метод storage_keys в хранилище
    #
    def test_check_method_storage_keys(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory( manager.settings )
        start.create()
        
        # Действия
        result = start.storage.storage_keys( start.storage  )
        
        # Проверки
        assert result is not None
        assert len(result) > 0
     
    #
    # Проверка работы фабрики для построения отчетности
    #
    def test_check_report_factory_create(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory( manager.settings )
        start.create()
        factory = report_factory()
        key = storage.unit_key()

        # Действие
        report = factory.create( 
                                manager.settings.report_mode, 
                                start.storage.data)
        
        # Проверки
        assert report is not None
        print ( report.create(key) )
 
    #
    # Проверка создания начальных рецептов
    #    
    def test_check_create_receipts(self):
        # Подготовка
        items = start_factory.create_receipts()
        
        # Действие
        
        # Проверки
        assert len(items) > 0     
        
    # 
    # Проверка создание начальной номенклатуры
    #    
    def test_check_create_nomenclatures(self):
        # Подготовка
        items = start_factory.create_nomenclatures()
        
        # действие
        
        # Прверки
        assert len(items) > 0 
        
        
    #
    # Проверка создание списка единиц измерения
    #    
    def test_check_create_units(self):
        # Подготовка
        items = start_factory.create_units()
        
        # Действие
        
        # Проверки
        assert len(items) > 0    
     
    #
    # Проверка создания списка групп
    # 
    def test_check_create_groups(self):
        # Подготовка
        items = start_factory.create_groups()
        
        # Действие
        
        # Проверки    
        assert len(items) > 0
        
        
    #      
    # Проверка работы класса start_factory. Метод create
    #
    def test_check_factory_create(self):
        # Подготовка
        manager = settings_manager()
        factory = start_factory( manager.settings )
        
        
        # Действие
        result = factory.create()
        
        
        # Проверка
        if manager.settings.is_first_start == True:
            assert result == True
            assert not factory.storage is None
            assert storage.nomenclature_key() in factory.storage.data
            assert storage.receipt_key() in factory.storage.data
            assert storage.group_key() in factory.storage.data
            assert storage.unit_key() in factory.storage.data
        else:
            assert result == False    
    def test_check_transactions_create(self):
        manager = settings_manager()
        factory = start_factory( manager.settings )
        
        
        # Действие
        result = factory.create_transaction()
        
        print(result)
        
        assert result != None
        assert len(result) == 20
        assert result[12].nomenclature.unit != None
        print(result)             
    
    def test_check_turn_calculation(self):
        manager = settings_manager()
        factory = start_factory( manager.settings )
        
        
        # Действие
        transactions_list = factory.create_transaction()
        result = process_factory.process_storage_turn(transactions_list)
        for item in result:
            print(item.quantity, item.nomenclature.name, item.storage.name)
        assert result != None
        assert len(result) <= 20
        assert len(result) > 0
        
       
