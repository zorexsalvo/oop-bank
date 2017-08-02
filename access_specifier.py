class Car:
    manufacturer = 'Honda'
    _wheels = 4
    __rrn = '5555'

    def __do_private_method(self):
        print('Accessed method')

class Model(Car):
    name = 'Civic'
    def __init__(self):
        print('{} {} has {} wheels'.format(
                self.manufacturer,
                self.name,
                self._wheels,
             )
        )
civic = Model()
