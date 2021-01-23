from cat import Cat
from animal import Animal

if __name__ == '__main__':
    my_cat = Cat(name='Angel', age='2', color='white', gender='female', hair='short')
    # my_cat = Cat('Angel', 'white', 2, 'female', 'short')
    my_cat.cry()
    my_cat.run()
    my_cat.catch_mouse()
    # my_animal = Animal('Angel', 'white', 2, 'female')
    # my_animal.cry()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
