import sys
sys.path.append('c:\\Users\\ze_us\\Documents\\VSProjects\\Shab_proek_2_sem\\gitclone\\popov_design_patterns')

import unittest
from Src.Logics.reporting import reporting
from Src.Models.unit_model import unit_model
from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Storage.storage import storage
from Src.Logics.csv_reporting import csv_reporting
from Src.settings_manager import settings_manager

class reporting_test(unittest.TestCase):
    
    
    #
    #Проверить статический метод build класса reporting
    #
    def test_check_reporting_build(self):
        #Подготовка
        data = {}
        list = []
        item = unit_model.create_gram()
        list.append(item)
        data[ storage.unit_key() ] = list
        #Действие
        result = reporting.build( storage.unit_key(), data)
        
        #Проверки
        assert result is not None
        assert len(result) > 0
    def test_check_csv_create(self):
        #Подготовка
        data_unit = {}
        data_group = {}
        data_nomenclature = {}
        
        list_unit = []
        list_group = []
        list_nomenclature = []
        
        group = group_model("test group")
        unit = unit_model("test unit")
        
        item_unit = unit_model.create_gram()
        item_group = group_model.create_group()
        item_nomenclature = nomenclature_model("test")
        
        item_nomenclature.group = group
        item_nomenclature.unit = unit
        
        list_unit.append(item_unit)
        list_group.append(item_group)
        list_nomenclature.append(item_nomenclature)
       
        data_unit[ storage.unit_key() ] = list_unit
        data_group[ storage.group_key() ] = list_group
        data_nomenclature[ storage.nomenclature_key() ] = list_nomenclature
        
        manager = settings_manager()
        
        report_unit = csv_reporting( manager.settings, data_unit)
        report_group = csv_reporting( manager.settings, data_group)
        report_nomenclature = csv_reporting( manager.settings, data_nomenclature)
        
        #Действие
        result_unit = report_unit.create( storage.unit_key() )
        result_group = report_group.create( storage.group_key() )
        result_nomenclature = report_nomenclature.create( storage.nomenclature_key() )

        print(result_unit)
        print(result_group)
        print(result_nomenclature)
        
        #Проверки
        assert result_unit is not None
        assert len(result_unit) > 0
        assert len(result_unit.split(';')) == 7
        
        assert result_group is not None
        assert len(result_group) > 0   
        assert len(result_group.split(';')) == 3
        
        assert result_nomenclature is not None
        assert len(result_nomenclature) > 0
        assert len(result_nomenclature.split(';')) == 7