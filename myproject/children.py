""" Children creates children objects """


class Children:
    """ Children creates children object """

    def __init__(self):
        self.list = []
        self.map = {}

    def add(self, child):
        """ Adds an object to children """
        name = child.name.lower()
        self.list.append(child)
        if name in self.map:
            if isinstance(self.map[name], list):
                self.map[name].append(child)
            else:
                self.map[name] = [self.map[name], child]
        else:
            self.map[name] = child

    def __iter__(self):
        return iter(self.list)

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.map[key]
        return self.list[key]

    def __getattr__(self, name):
        return self.map[name]
