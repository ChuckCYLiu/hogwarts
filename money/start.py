from send_money import send_money
from select_money import select_money


if __name__ == '__main__':
    print('原有存款：', select_money())
    send_money(1000)
    print('发工资后存款：', select_money())
