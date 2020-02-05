import time
import datetime
import keyboard

ROUND = 'ROUND'
SQUARE = 'SQUARE'
TOUCH_NUMBER = 0
IS_RUNNING = True


def main(data):
    anterior = data[0]
    if keyboard.read_key() == "q" and anterior != ROUND:
        print("Ball hit round side, anterior:" + anterior)
        temp_date = datetime.datetime.now()
        if (temp_date - data[3]).total_seconds() < get_delta_time(data[2]):
            anterior = ROUND
            data[2] = data[2] + 1
            data[3] = temp_date
        else:
            data[1] = send_game_over()
    elif keyboard.read_key() == "d" and anterior != SQUARE:
        print("Ball hit square side, anterior:" + anterior)
        temp_date = datetime.datetime.now()
        if (temp_date - data[3]).total_seconds() < get_delta_time(data[2]):
            anterior = SQUARE
            data[2] = data[2] + 1
            data[3] = temp_date
        else:
            data[1] = send_game_over()
    else:
        data[1] = send_game_over()
    data[0] = anterior
    return data


def get_delta_time(touch_number):
    if touch_number == 0:
        return 10
    if touch_number < 40:
        return - touch_number / 10+5
    return 1


def send_game_over():
    print('Game Over !')
    return False


print("Game Start !")
data = ['', IS_RUNNING, TOUCH_NUMBER, datetime.datetime.now()]
while IS_RUNNING:
    data = main(data)
    IS_RUNNING = data[1]
    time.sleep(.200)
