from magicbot.state_machine import AutonomousStateMachine, state
import wpilib
from wpilib.drive import DifferentialDrive
from ntcore import NetworkTableInstance


class Center1(AutonomousStateMachine):

    MODE_NAME = "Center 1"
    DEFAULT = True

    nt: NetworkTableInstance
    drive: DifferentialDrive

    @state(first=True)
    def gettx(self):
        tid = self.nt.getEntry("/limelight/tid").getDouble(-1)
        offset = self.nt.getEntry("/limelight/tx").getDouble(0)
        pose = self.nt.getEntry("/limelight/targetpose_robotspace").getDoubleArray(
            [0, 0, 0, 0, 0, 0]
        )
        rot = 0
        speed = 0
        if tid != -1:
            if not -2 < offset < 2:
                rot = 0.16 if offset < 0 else -0.16

            if not 1.3 < pose[2] < 1.5:
                speed = 0.3 if pose[2] > 1.5 else -0.3

        print("----")
        print(tid)
        print(pose[2], offset)
        print(-speed, rot)
        self.drive.arcadeDrive(-speed, rot)
