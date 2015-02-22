from errors import OutResourcesError, NotFoundError


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Resources ():
    """ Signleton for using of resources """

    _allocated = {}
    _deallocated = []

    __metaclass__ = Singleton

    def init (self, count, name = 'r'):
        self._allocated = {}
        self._deallocated = []
        for i in range(count):
            self._deallocated.append('{0}{1}'.format(name, i))

    def get_list (self, user=None):
        if user:
            return map(lambda a: a[0], filter(lambda a: a[1] == user, self._allocated.items()))
        return {
            'allocated': self._allocated,
            'deallocated': self._deallocated
        }

    def allocate (self, user):
        try:
            resource = self._deallocated.pop(0)
            self._allocated.update({resource: user})
        except IndexError:
            raise OutResourcesError
        else:
            return resource

    def deallocate (self, resource):
        try:
            self._allocated.pop(resource)
        except KeyError:
            raise NotFoundError
        else:
            self._deallocated.append(resource)

    def reset (self):
        while self._allocated:
            self._deallocated.append(self._allocated.popitem()[0])
