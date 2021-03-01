class File:

    def __init__(self, name):
        self._name = name # имя нашего файла

    def get_name(self):
        """Геттер имени файла"""
        name = self._name.split('.', 1)[0]
        return name
    
    def get_frmt(self):
        """Возвращает формат файла."""
        frmt = self._name.split('.', 1)[1]
        return frmt

    def set_format(self, frmt):
        """Сеттер формата. Возвращает новый объект File."""
        file_old = self._name.split('.', 1)
        file_old[1] = frmt
        file_new = ''.join(file_old)
        return File(file_new)

    def read_params(self, frmt):
        """Функция открывает объект в нужном формате, считывает данные с нашего объекта."""
        a = self.set_format(frmt)
        with open(a) as f:
            #считали данные, параметры
            params = {}
        return params #вернули параметры

    def write_params(self, frmt, params):
        """Функция открывает объект в нужном формате, записывает данные, возвращает объект File в прежнем формате."""
        old_frmt = self.get_frmt() # запомнили формат
        a = self.set_format(frmt)
        with open(a, 'w') as f:
            f.write(params)  # записали параметры

        self.set_format(old_frmt) # вернули прежний формат  


