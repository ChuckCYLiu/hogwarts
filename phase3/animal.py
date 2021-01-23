class Animal:
    """模拟动物的类"""
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def cry(self):
        """发出叫声"""
        print(f'{self.name} is crying.')

    def run(self):
        """跑动"""
        print(f'{self.name} started running.')
