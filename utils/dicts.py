def get_val(collection: dict, key, default='git') -> any:
    """
    Возвращает значение по ключу из словаря. Если ключ отсутствует, возвращает значение default
    :param collection: Словарь
    :param key: Ключ словаря
    :param default: Значение при отсутствии ключа. По умолчанию равен 'git'
    :return: Значение по ключу
    """
    if key in collection.keys():
        return collection[key]

    return default
