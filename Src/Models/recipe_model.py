from Src.Models.group_model import group_model
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.settings import settings
from Src.Storage.storage import storage
from Src.exceptions import exception_proxy

class recipe_model:
    
    __recipe_name = None
    __comments = None
    __cooking_time = None
    __weight_before = None
    __weight_after = None
    
    
    