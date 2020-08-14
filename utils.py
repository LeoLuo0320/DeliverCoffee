import inspect


def get_subclass_set(cls, base_cls):
    subcls_set = {}
    for subclass_name in dir(cls):
        attr = getattr(cls, subclass_name)
        if inspect.isclass(attr) and issubclass(attr, base_cls):
            subcls_set[subclass_name] = attr
    return subcls_set


def subclass_set(base_cls, property_name):
    class MetaClass(type):
        def __init__(cls, name, bases, dct):
            super().__init__(name, bases, dct)
            setattr(cls, property_name, get_subclass_set(cls, base_cls))

    return MetaClass


def encode(x, l):
    return [y == x for y in l]


def one_hot(i, l):
    assert i < l, (i, l)
    res = [0.] * l
    res[i] = 1.
    return res


def pad(x, l):
    if x is None:
        return [0.] * l
    assert len(x) <= l, (len(x), l, x)
    return x + ([0.] * (l - len(x)))
