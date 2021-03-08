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
        date_signs = [i for i in value if not i.isalnum()]
        fit_frmt = ''
            
        for frmt in self.date_formats:
            print(frmt)
            frmt_signs = (i for i in frmt if not (i.isalpha() or i == '%'))      
            if tuple(date_signs) == tuple(frmt_signs):
                fit_frmt = frmt   

        print(fit_frmt, date_signs)
        try:
                datetime.strptime(value, fit_frmt)
                return True
        except ValueError:
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

