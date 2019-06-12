import random


class Gen:
    uid = 0
    adaptation = 0

    def __init__(self, uid):
        self.uid = uid
        self.adaptation = random.randint(1, 10000)

    def __repr__(self):
        return '(id:{}, adapt:{})'.format(self.uid, self.adaptation)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.get_uid() == other.get_uid() and self.get_adaptation() == other.get_adaptation()
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.get_uid() != other.get_uid() and self.get_adaptation() != other.get_adaptation()
        return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.get_adaptation() < other.get_adaptation()
        return False

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.get_adaptation() <= other.get_adaptation()
        return False

    def __qt__(self, other):
        if isinstance(other, self.__class__):
            return self.get_adaptation() > other.get_adaptation()
        return False

    def __qe__(self, other):
        if isinstance(other, self.__class__):
            return self.get_adaptation() >= other.get_adaptation()
        return False

    def mutation(self, other):
        if isinstance(other, self.__class__):
            return (self.get_adaptation() + other.get_adaptation()) // 2
        return False

    def get_adaptation(self):
        return self.adaptation

    def get_uid(self):
        return self.id

    def set_adaptation(self, adaptation):
        self.adaptation = adaptation
