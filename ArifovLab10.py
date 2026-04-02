'''
-----------------------------------------------------------------------------
Solution: Lab 10
-----------------------------------------------------------------------------
Developer: < Akmal Arifov >
Course: Intro to Programming & Logic CITC-1301
Creation Date: < 12/1/2022 >
Last Mod Date: < 12/2/2022 >
E-mail Address: <Asarifov@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - <Vehicle Class Test Program>
-----------------------------------------------------------------------------
Description of input:
<No inputs>
Description of output:
<Car accerrates and decerelates 5 times>
-----------------------------------------------------------------------------

'''

class Vehicle:

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def decelerate(self):
        if self.speed > 0:
            self.speed -= 5

    def __str__(self):
        return f"The {self.year} {self.make} {self.model} vehicle is traveling at {self.speed} MPH"

def main():

    car1 = Vehicle('2015', 'Chevy', 'Spark')
    
    print('Vehicle Class Test Program')

    print('\nAccerlerating...')
    for i in range(5):
        car1.accelerate()
        print(f'Current Speed: {car1.speed}')

    print('\nBraking...')
    for i in range(5):
        car1.decelerate()
        print(car1.__str__())


if __name__ == "__main__":
    main()