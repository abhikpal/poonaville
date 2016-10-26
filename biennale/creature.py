import random
import time

class Creature(object):
    """Defines a creature on the projection."""
    def __init__(self, uid):
        """
        Creatures a new creature with the given unique identifier (uid).
        """
        raise NotImplementedError

    def get_location(self):
        """
        returns a tuple (x, y) with the location of the creature.
        """
        raise NotImplementedError

    def update_position(self, position):
        """
        position
            tuple of the form (x, y) with x and y derivates.

        Updates the coordinates of the creature. The new position is the
        sum of the current coordinate set and the derivatives given in
        position. The method also chnages the last modification time.

        """
        raise NotImplementedError

    def get_inactivity_duration(self):
        """
        Returns the time (in secods) elapsed between the last time the
        Creature was updated to the current time.
        """
        raise NotImplementedError

    def get_dict_repr(self):
        """
        Returns a dictionary representation of the Creature.
            {
                "id": <str: uid>,
                "x": <float: x location>,
                "y": <float: y location>,
                "created": <timestamp: creation timestamp>,
                "modifed": <timestamp: last modification timestamp>
            }
        """
        raise NotImplementedError
