from abc import ABCMeta, abstractmethod
from datetime import datetime



def compare_format(date, frmt):
    """Check date and format."""
    frmt_signs = (i for i in frmt if not (i.isalpha() or i == '%'))  
    date_signs = (i for i in date if not i.isnumeric())
    
    if not tuple(frmt_signs) == tuple(date_signs):
        return False

    frmt_items = [i for i in frmt if i.isalpha()]
    date_lst = list(date)

    for i, k in enumerate(date_lst):
        if not k.isnumeric():
            date_lst[i] = ' '

    date_items = list(map(int, ''.join(date_lst).split()))

    for i, k in enumerate(date_items):
        if frmt_items[i] == 'Y':
            if k not in range(10**3, 10**4):
                return False
        if frmt_items[i] == 'm':
            if k not in range(1, 13):
                return False
        if frmt_items[i] == 'd':
            if k not in range(1, 31):
                return False
        if frmt_items[i] == 'H':
            if not 23 // k :
                return False
        if frmt_items[i] == 'M':
            if not 59 // k:
                return False
        if frmt_items[i] == 'S':
            if not 59 // k:
                return False
                
    return True


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

    def validate(self, value): # новый метод
        for frmt in self.date_formats:
            if compare_format(value, frmt):
                return True        
        return False

    def validate_old(self, value): # старый метод
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



