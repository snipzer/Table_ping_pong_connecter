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
        if data[2] != 0 and data[2] % 2 != 0:
            if (temp_date - data[3]).total_seconds() < data[4]:
                anterior = ROUND
                data[2] = data[2] + 1
                data[3] = temp_date
                data[4] = get_delta_time(data[2])+2
                ## RESET DES DIODES ICI
                print("Temp pour l'echange: " + str(data[4]))
            else:
                data[1] = send_game_over()
        else:
            anterior = ROUND
            data[2] = data[2] + 1
    elif keyboard.read_key() == "d" and anterior != SQUARE:
        print("Ball hit square side, anterior:" + anterior)
        temp_date = datetime.datetime.now()
        if data[2] != 0 and data[2] % 2 != 0:
            if (temp_date - data[3]).total_seconds() < data[4]:
                anterior = SQUARE
                data[2] = data[2] + 1
                data[3] = temp_date
                data[4] = get_delta_time(data[2])+2
                ## RESET DES DIODES ICI
                print("Temp pour l'echange: " + str(data[4]))
            else:
                data[1] = send_game_over()
        else:
            anterior = SQUARE
            data[2] = data[2] + 1
    else:
        data[1] = send_game_over()
    data[0] = anterior
    return data


def get_delta_time(touch_number):
    if touch_number == 0:
        return 5
    if touch_number < 40:
        return - touch_number / 10+5
    return 1


def send_game_over():
    print('Game Over !')
    return False


print("Game Start !")
data = ['', IS_RUNNING, TOUCH_NUMBER, datetime.datetime.now(), get_delta_time(TOUCH_NUMBER)]
print("Temp pour faire l'échange :" + str(data[4]))
while IS_RUNNING:
    data = main(data)
    IS_RUNNING = data[1]
    time.sleep(.200)
