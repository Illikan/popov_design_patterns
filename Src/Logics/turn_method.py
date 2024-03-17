
def turn_method(transactions_list: list):
    # Словарь, где ключ - кортеж из номенклатуры, единицы измерения, склада и типа операции
    turn_dict = {}
    # Перебор всех транзакций в списке и передача данных в словарь
    for transaction in transactions_list:
        if (transaction.nomenclature, transaction.unit, transaction.storage, transaction.operation_type) in turn_dict.keys():
            turn_dict[(transaction.nomenclature, transaction.unit, transaction.storage, transaction.operation_type)] += transaction.quantity
        else:
            turn_dict[(transaction.nomenclature, transaction.unit, transaction.storage, transaction.operation_type)] = transaction.quantity
    # Результат
    return turn_dict
    
