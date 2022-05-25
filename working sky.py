import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")
newVal = "COM" + str(val)

for x in range(0, len(portList)):
    if portList[x].startswith("Com" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

serialInst.baudrate = 9600
serialInst.port = newVal #"COM4" #portVar dont know why portVar doesnt work
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        newVal = str(packet.decode('utf')).strip('\n')
        print(packet.decode('utf'), end = "")
        f = open("demofile2.txt", "a")
        f.write(newVal)
        lineWritten = "line written, put on next skylander!"
        print(str(lineWritten))
        f.close() #time delay cuz this is slow lol