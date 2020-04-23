from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size, title):
        self.size = size
        self.title = title

    @abstractmethod
    def tex_cons(self):
        pass

    def __add__(self, other):
        return self.tex_cons + other.tex_cons


class Coat(Clothes):

    def __init__(self, size, title):
        super().__init__(size, title)

    @property
    def tex_cons(self):
        return float(f"{self.size / 6.5 + 0.5:.4f}")


class Suit(Clothes):

    def __init__(self, size, title):
        super().__init__(size, title)

    @property
    def tex_cons(self):
        return float(f"{2 * self.size + 0.3:.4f}")


my_coat = Coat(52, "Red coat")
a = my_coat.tex_cons
print(my_coat.tex_cons)

my_suit = Suit(1.85, "Casual suit")
b = my_suit.tex_cons
print(my_suit.tex_cons)

print(my_coat + my_suit)
