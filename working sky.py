from hashlib import new
from mailbox import linesep
import serial.tools.list_ports
import msvcrt
import sys
import os

#list of imports that will be used in the auto file
imports = ["import edu.wpi.first.wpilibj2.command.SequentialCommandGroup;",
           "import frc.robot.Constants.AUTOCONSTANTS;"]

#rfid tags and their corresponding auto command groups
Cynder = ["66AADCA4", "deadline(new Command1(param)),"]
DoubleTrouble = ["F6413CF6", "deadline(new Command2(param)),"]
LegendarySlamBam = ["A48B4C24", "deadline(new Command3()),"]
Bouncer = ["6224FE67", "deadline(new Command4(param1, param2)),"]
Swarm = ["76247EE1", "deadline(new Command5()),"]
ShroomBoom = ["04E82919", "deadline(new Command6(param)),"]




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
firstEmpty = False
filename = "demofile2.txt"
newFileName = ""

while True:
    newFileQuestion = input("is this a new file? (y/n)")
    if newFileQuestion == "y":
        try:
            newFileName = input("input new file name (with file type):")
            filename = newFileName
            f = open(filename, "x")
            break;
        except:
            print("this name is already taken. try again")
    elif newFileQuestion == "n":
        openFileName = input("choose which file to write in: ")
        filename = openFileName
        print("ok, will be writing in " + filename)
        break
    else:
        print("this isnt an input stupid")

print("press any key to exit program")

with open(filename) as friendsfile:
    first = friendsfile.read(1)
    if not first: #empty
        firstEmpty=True



f = open(filename, "a")
key=""
if firstEmpty:
    f.write("// Copyright (c) FIRST and other WPILib contributors. \n// Open Source Software; you can modify and/or share it under the terms of \n// the WPILib BSD license file in the root directory of this project.\n")
    f.write("\npackage frc.robot;\n\n")
    for s in imports:
        f.write(s + "\n")
    f.write("// NOTE:  Consider using this command inline, rather than writing a subclass.  For more \n"
            "// information, see:\n"
            "// https://docs.wpilib.org/en/stable/docs/software/commandbased/convenience-features.html\n"
            "public class " + filename + " extends SequentialCommandGroup {\n"
            "/** Creates a new Swrv. */\n"
            "public " + filename + "() {\n"
            "// Add your commands in the addCommands() call, e.g.\n"
            "// addCommands(new FooCommand(), new BarCommand());\n"
            "addCommands(")
    f.close()
else:
    fd=open(filename,"r")
    d=fd.read()
    fd.close()
    m=d.split("\n")
    s="\n".join(m[:-1])
    fd=open("l","w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        newVal = str(packet.decode('utf')).strip()

        #print(packet.decode('utf'), end = "")
        f = open(filename, "a")
        lineSegment = "".strip()
        if newVal == LegendarySlamBam[0]:
             lineSegment = LegendarySlamBam[1]

        elif newVal == Cynder[0]:
             lineSegment = Cynder[1]

        elif newVal == DoubleTrouble[0]:
             lineSegment =DoubleTrouble[1]

        elif newVal == Bouncer[0]:
             lineSegment =Bouncer[1]

        elif newVal == Swarm[0]:
             lineSegment =Swarm[1]

        elif newVal == ShroomBoom[0]:
             lineSegment =ShroomBoom[1]
        lineWritten = "line written, put on next skylander!"
        
        bool = newVal.strip() == "04E82919"
       
        
        f.write(lineSegment.strip() + "\n")
        #print(packet.split())
        print(str(bool))
        print(lineSegment)
        #print(str(lineWritten))
        f.close() #time delay cuz this is slow lol
    if msvcrt.kbhit():
        f = open(filename, "a")
        f.write("deadline(new Stop()));}}")
        #dont know how to remove last character from file with
        #python, so im just adding a bogus command at the end so
        #it completes with a semicolon
        f.close
        sys.exit()
   