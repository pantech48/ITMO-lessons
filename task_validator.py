from abc import ABCMeta, abstractmethod
from datetime import datetime


class Validator(metaclass=ABCMeta):

    @abstractmethod
    def validate(self, value):
        """Метод принимает валидируемое значение"""


class EMailValidator(Validator):
    def __init__(self):
        pass

    def validate(self, value):

        if not 0 < value.count('@') < 2:
            return False

        if value.startswith('@') or value.endswith('@'):
            return False
        
        return True

        
class DateTimeValidator(Validator):
    
    def __init__(self, date_formats=[
                                        '%Y-%m-%d',
                                        '%Y-%m-%d %H:%M',
                                        '%Y-%m-%d %H:%M:%S',
                                        '%d.%m.%Y',
                                        '%d.%m.%Y %H:%M',
                                        '%d.%m.%Y %H:%M:%S',
                                        '%d/%m/%Y',
                                        '%d/%m/%Y %H:%M',
                                        '%d/%m/%Y %H:%M:%S',
                                    ]
    ):
        self.date_formats = date_formats

    def validate(self, value):

        for frmt in self.date_formats:
            try:
                datetime.strptime(value, frmt)
                return True
            except ValueError:
                continue
        return False


class ChainValidator(Validator):
    
    def __init__(self, validators):
        self.validators = validators

    def validate(self, value):

        for validator in self.validators:
            if validator.validate(value):
                continue
            return False

        return True
