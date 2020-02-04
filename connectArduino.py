import serial
import serial.tools.list_ports


#Lancement du programme
#Delai -> début partie 3-2-1 :  LED + Buzzer
#On récupère les informations des arduinos
#On détecte les échanges en fonction

#port = 'COM8'
#bitrate = 9600

def getArduino(port, bitrate):
    return serial.Serial(port, bitrate)


arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description  # may need tweaking to match new arduinos
]
if not arduino_ports:
    raise IOError("No Arduino found")


def main():
    if len(arduino_ports) == 2:
        arduinoRound = getArduino(arduino_ports[0], 9600)
        arduinoSquare = getArduino(arduino_ports[1], 9600)
    else:
        arduinoRound = getArduino(arduino_ports[0], 9600)
        arduinoSquare = ""

    while 1:
        if arduinoRound != "" and arduinoRound.readline() != "":
            print("=======================")
            print(arduinoRound.readline())
        if arduinoSquare != "" and arduinoSquare.readline() != "":
            print("///////////////////////")
            print(arduinoSquare.readline())

main()
