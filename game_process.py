import time
import keyboard

ROUND = 'ROUND'
SQUARE = 'SQUARE'
IS_RUNNING = True


def main(data):
    anterior = data[0]
    if keyboard.read_key() == "q" and anterior != ROUND:
        print("Ball hit round side, anterior:" + anterior)
        anterior = ROUND
    elif keyboard.read_key() == "d" and anterior != SQUARE:
        print("Ball hit square side, anterior:" + anterior)
        anterior = SQUARE
    else:
        data[1] = send_game_over()
    data[0] = anterior
    return data


def send_game_over():
    print('Game Over !')
    return False


print("Game Start !")
data = ['', IS_RUNNING]
while IS_RUNNING:
    data = main(data)
    IS_RUNNING = data[1]
    time.sleep(.200)
