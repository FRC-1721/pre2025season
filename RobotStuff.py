import wpilib
import wpilib.drive
from rev import CANSparkMax

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.joystick = wpilib.Joystick(0)
        self.motor = CANSparkMax(12, CANSparkLevel.motorType.kBrushless)

    def teleopPeriodic(self):
        self.motor.set(self.joystick.getY())