from abc import ABCMeta, abstractmethod
import json
import pickle
import os


class ParamHandlerException(Exception):
    pass


class ParamHandler(metaclass=ABCMeta):
    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_param(self, key):
        return self.params.get(key)

    def get_all_params(self):
        return self.params

    def remove_param(self, key):
        self.params.pop(key)

    def remove_all_params(self):
        self.params.clear()


    @abstractmethod
    def read(self):
        """Read parametres from file."""

    @abstractmethod
    def write(self):
        """Write parametres on file."""


class JsonParamHandler(ParamHandler):
    def read(self):
        with open(self.source) as f:
            self.params = json.load(f)

    def write(self):
        with open(self.source, 'w') as f:
            json.dump(self.params, f)


class PickleParamHandler(ParamHandler):
    def read(self):
        with open(self.source, 'rb') as f:
           self.params = pickle.load(f)

    def write(self):
        with open(self.source, 'wb') as f:
            pickle.dump(self.params, f)


class ParamHandlerFactory:
    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name.')
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(f'Class "{klass}" is not ParamHandler.')

        cls.types[name] = klass

    @classmethod
    def create(cls, source):
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')

        klass = cls.types.get(ext)

        if klass is None:
            raise ParamHandlerException(f'Type "{ext}" not found.')

        return klass(source) 


ParamHandlerFactory.add_type('pickle', PickleParamHandler)
ParamHandlerFactory.add_type('json', JsonParamHandler)







