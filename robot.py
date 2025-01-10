import wpilib
import wpilib.drive
from magicbot import MagicRobot
import rev

class Robot(MagicRobot):
    def createObjects(self):
        self.controller =  wpilib.XboxController(0)
        
        self.left1 = rev.SparkMax(21, rev.SparkLowLevel.MotorType.kBrushless)
        self.left2 = rev.SparkMax(24, rev.SparkLowLevel.MotorType.kBrushless)
        self.right1 = rev.SparkMax(22, rev.SparkLowLevel.MotorType.kBrushless)
        self.right2 = rev.SparkMax(23, rev.SparkLowLevel.MotorType.kBrushless)

        self.left = wpilib.MotorControllerGroup(self.left1, self.left2)
        self.left.setInverted(True)
        self.right = wpilib.MotorControllerGroup(self.right1, self.right2)
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

    def teleopPeriodic(self):
        self.drive.arcadeDrive(self.controller.getRawAxis(1) * .5, self.controller.getRawAxis(2) * .5)