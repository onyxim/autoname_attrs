from sqlalchemy.ext.declarative import DeclarativeMeta

from . import AutoNamedClassAttrs


class AutoNamedModelAttrs(AutoNamedClassAttrs, DeclarativeMeta):

    def __init__(cls, classname, bases, dict_):
        type.__init__(cls, classname, bases, dict_)

    def __setattr__(cls, key, value):
        type.__setattr__(cls, key, value)
