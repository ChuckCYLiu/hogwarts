from animal import Animal


class Cat(Animal):
    """模拟猫咪的类"""
    def __init__(self, name, color, age, gender, hair):
        super().__init__(name, color, age, gender)
        self.hair = hair

    def catch_mouse(self):
        """猫捉老鼠"""
        print(f'{self.name} caught a mouse!')

    def cry(self):
        """猫咪发出叫声"""
        print(f'{self.name} is mewing.')