import wpilib
import wpilib.drive
import rev

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.joystick = wpilib.Joystick(0)
        self.left = rev.SparkMax(1, rev.SparkLevel.motorType.kBrushless)
        self.left2 = rev.SparkMax(3, rev.SparkLevel.motorType.kBrushless)
        self.right = rev.SparkMax(2, rev.SparkLevel.motorType.kBrushless)
        self.right2 = rev.SparkMax(4, rev.SparkLevel.motorType.kBrushless)

        self.left2.follow(self.left)
        self.right2.follow(self.right)

    def teleopPeriodic(self):
        self.left.set(0.1)