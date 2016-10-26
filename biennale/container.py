from biennale.creature import Creature

class Container(object):
    """
    A Container object stores the movable elements -- i.e., Creature()
    objects -- of the projection and provides an interface to perform
    basic operations on these Creatures.
    """

    def __init__(self, timeout=60):
        """
        timeout (in seconds)
            a creature will be removed if it receives no updates in the
            duration specified by timeout.
        """

        raise NotImplementedError

    def add(self, request):
        """
        request
            the request made by the client

        Container.add() adds a creature to the container. If the request
        is coming from a pre-existing client, no creature is added, else
        a new creature is created and added to the container.
        """
        raise NotImplementedError

    def remove(self, request):
        """
        request
            the request made by the client

        Removes the creature corresponding to the request's client from 
        the container. Raises a KeyError if the requested client is not
        present in the container.
        """
        raise NotImplementedError

    def get_json(self):
        """
        returns the container and all its elements as a json thing.
        """
        raise NotImplementedError

    def move_creature(self, request):
        """
        request
            the request made by the client

        extracts the move made by the client through `request` and adds
        it to the correponding creature.
        """
        raise NotImplementedError

    def update(self):
        """
        Updates the container and kills the creatures that have not been
        updated recently.
        """
        raise NotImplementedError

    def get_elements(self):
        """
        Returns a list of elements in the current container.
        """
        raise NotImplementedError

    def get_timeout(self):
        """
        Returns the timeout of the current container.
        """
        raise NotImplementedError
