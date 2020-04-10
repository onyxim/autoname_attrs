class AutoNamedClassAttrs(type):

    def __new__(mcs, name, bases, dict_):
        attrs_dict = {}
        for key, value in dict_.items():
            if key.startswith('__') or callable(value):
                continue
            attrs_dict[key] = key
        return type.__new__(mcs, name, (), attrs_dict)