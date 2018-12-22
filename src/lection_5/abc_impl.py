from abc import ABC, abstractmethod

class Unit(ABC):
    @property
    @abstractmethod
    def health(self):
        pass


class Soldier(Unit):
    @property
    def health(self):
        return self.health

    @health.setter
    def health(self, damage):
        self.health -= damage


class Vehicle(Unit):
    @property
    def health(self):
        return self.health


