import datetime
class Time_control:
    # def __init__(self, skript):
    #     self.skript = skript
    def __enter__(self):
        self.start_time = datetime.datetime.now()
        print('Начало работы кода', self.start_time.strftime("%X"))
        return self.start_time

    def __exit__(self, exception_type, exception_val, trace):
        self.end_time = datetime.datetime.now()
        deference = self.end_time - self.start_time
        print('Конец работы кода', self.end_time.strftime("%X"))
        print('Код работал: ', deference, 'минут')
        return self.end_time


with Time_control() as start_time:
   a = input('подожди и введи число: ')


