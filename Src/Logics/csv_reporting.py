import sys
sys.path.append('c:\\Users\\ze_us\\Documents\\VSProjects\\Shab_proek_2_sem\\gitclone\\popov_design_patterns')
from Src.Logics.reporting import reporting

class csv_reporting(reporting):
        
    def create(self, typeKey: str):

        super().create(typeKey)
        result = ""
        list = []
        #Исходные данные
        items = self.data[ typeKey ]
        
        
        #Список
        for field in self.fields:
            result += f"{field};"
            
        result = result[:-1] + '\n'
        
        for item in items:
            for field in self.fields:
                attr = getattr(item, field)
                found_attr = reporting.make_element(attr)
                list.append(found_attr)
            result += ";".join(list) + "\n"

        #Результат csv
        return result
    