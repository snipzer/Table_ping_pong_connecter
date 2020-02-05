import time
import serial.tools.list_ports
import serial

ROUND = 'ROUND'
SQUARE = 'SQUARE'
IS_RUNNING = True
data = {
    "error": '100'
}

def getArduino(port, bitrate):
    return serial.Serial(port, bitrate)


arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description  # may need tweaking to match new arduinos
]
if not arduino_ports:
    raise IOError("No Arduino found")


if len(arduino_ports) == 2:
    arduinoRound = getArduino(arduino_ports[0], 9600)
    arduinoSquare = getArduino(arduino_ports[1], 9600)
elif len(arduino_ports) > 0 and len(arduino_ports) != 2:
    arduinoRound = getArduino(arduino_ports[0], 9600)
    arduinoSquare = ""
else:
    exit(1)


def main(data):
    anterior = data[0]
    if arduinoRound.readline() != "" and anterior != ROUND:
        print("Ball hit round side, anterior:" + anterior)
        anterior = ROUND
    elif arduinoSquare.readline() != "" and anterior != SQUARE:
        print("Ball hit square side, anterior:" + anterior)
        anterior = SQUARE
    else:
        data[1] = send_game_over()
    data[0] = anterior
    return data


def send_game_over():
    print('Game Over !')
    arduinoRound.write(data['error'].encode())
    return False


print("Game Start !")
data = ['', IS_RUNNING]
while IS_RUNNING:
    data = main(data)
    IS_RUNNING = data[1]
    time.sleep(.200)
