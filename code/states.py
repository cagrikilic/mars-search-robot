"""Module for rover states."""

__author__ = 'Salman Hashmi'
__license__ = 'BSD License'


import numpy as np


class FindWall():
    """Create a class to represent FindWall state."""

    def __init__(self):
        """Initialize a FindWall instance."""
        self.name = 'Find Wall'

    def execute(self, Rover):
        """Execute the FindWall state action."""
        Rover.throttle = 0
        Rover.brake = 0
        Rover.steer = 15


class FollowWall():
    """Create a class to represent FollowWall state."""

    def __init__(self):
        """Initialize a FollowWall instance."""
        self.throttle_setting = 0.8
        self.wall_angle_offset = 9.2
        self.name = 'Follow Wall'

    def execute(self, Rover):
        """Execute the FollowWall state action."""
        if Rover.vel < Rover.max_vel:
            Rover.throttle = self.throttle_setting
        else:
            Rover.throttle = 0

        Rover.brake = 0
        Rover.steer = np.clip(
            np.mean(Rover.nav_angles_left * 180 / np.pi),
            -15, 15) - self.wall_angle_offset


class TurnToWall():
    """Create a class to represent TurnToWall state."""

    def __init__(self):
        """Initialize a TurnToWall instance."""
        self.brake_setting = 10
        self.name = 'Turn To Wall'

    def execute(self, Rover):
        """Execute the TurnToWall state action."""
        # Stop before turning
        if Rover.vel > 0.2:
            Rover.throttle = 0
            Rover.brake = self.brake_setting
            Rover.steer = 0

        elif Rover.vel <= 0.2:
            Rover.throttle = 0
            Rover.brake = 0
            Rover.steer = 15


class AvoidWall():
    """Create a class to represent AvoidWall state."""

    def __init__(self):
        """Initialize a AvoidWall instance."""
        self.name = 'Avoid Wall'

    def execute(self, Rover):
        """Execute the AvoidWall state action."""
        pass


class AvoidObstacles():
    """Create a class to represent AvoidObstacles state."""

    def __init__(self):
        """Initialize a AvoidObstacles instance."""
        self.name = 'Avoid Obstacles'

    def execute(self, Rover):
        """Execute the AvoidObstacles state action."""
        pass


class GoToSample():
    """Create a class to represent GoToSample state."""

    def __init__(self):
        """Initialize a GoToSample instance."""
        self.name = 'Go to Sample'

    def execute(self, Rover):
        """Execute the GoToSample state action."""
        pass


class InitiatePickup():
    """Create a class to represent InitiatePickup state."""

    def __init__(self):
        """Initialize a InitiatePickup instance."""
        self.name = 'Initiate Pickup'

    def execute(self, Rover):
        """Execute the InitiatePickup state action."""
        pass


class WaitForPickupInitiate():
    """Create a class to represent WaitForPickupInitiate state."""

    def __init__(self):
        """Initialize a WaitForPickupInitiate instance."""
        self.name = 'Wait..'

    def execute(self, Rover):
        """Execute the WaitForPickupInitiate state action."""
        pass


class WaitForPickupFinish():
    """Create a class to represent WaitForPickupFinish state."""

    def __init__(self):
        """Initialize a WaitForPickupFinish instance."""
        self.name = 'Pickup Sample.'

    def execute(self, Rover):
        """Execute the WaitForPickupFinish state action."""
        pass


class ReturnHome():
    """Create a class to represent ReturnHome state."""

    def __init__(self):
        """Initialize a ReturnHome instance."""
        self.name = 'Return Home'

    def execute(self, Rover):
        """Execute the ReturnHome state action."""
        pass


class Stop():
    """Create a class to represent Stop state."""

    def __init__(self):
        """Initialize a Stop instance."""
        self.name = 'Stop'

    def execute(self, Rover):
        """Execute the Stop state action."""
        pass


class FullStop():
    """Create a class to represent FullStop state."""

    def __init__(self):
        """Initialize a FullStop instance."""
        self.name = 'Full Stop'

    def execute(self, Rover):
        """Execute the FullStop state action."""
        pass
