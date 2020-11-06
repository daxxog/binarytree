from numbers import Real, Number
from functools import total_ordering


@total_ordering
#class Character(object):
class Character(Real):
#class Character(Integral):
    def __init__(self, _char_value):
        self._char_value = ord(_char_value)

    def __repr__(self):
        return chr(self._char_value)

    def __abs__(self):
        return Character(self._char_value.__abs__())

    def __add__(self, other):
        return Character(self._char_value.__add__(other))

    def __and__(self, other):
        return Character(self._char_value.__and__(other))

    def __ceil__(self):
        return Character(self._char_value.__ceil__())

    def __eq__(self, other):
        if isinstance(other, Character):
            return self._char_value.__eq__(other._char_value)
        else:
            return self._char_value.__eq__(other)

    def __float__(self):
        return Character(self._char_value.__float__())

    def __floor__(self):
        return Character(self._char_value.__floor__())

    def __floordiv__(self, other):
        return Character(self._char_value.__floordiv__(other))

    def __int__(self):
        return Character(self._char_value.__int__())

    def __invert__(self):
        return Character(self._char_value.__invert__())

    def __lshift__(self, other):
        return Character(self._char_value.__lshift__(other))

    def __le__(self, other):
        if isinstance(other, Character):
            return self._char_value.__le__(other._char_value)
        else:
            return self._char_value <= other

    def __lt__(self, other):
        if isinstance(other, Character):
            return self._char_value.__lt__(other._char_value)
        else:
            return self._char_value < other

    def __mod__(self, other):
        return Character(self._char_value.__mod__(other))

    def __mul__(self, other):
        return Character(self._char_value.__mul__(other))

    def __neg__(self):
        return Character(self._char_value.__neg__())

    def __or__(self, other):
        return Character(self._char_value.__or__(other))

    def __pos__(self):
        return Character(self._char_value.__pos__())

    def __pow__(self, other, *args):
        if len(args) == 1:
            return Character(self._char_value.__pow__(other, args[0]))
        else:
            return Character(self._char_value.__pow__(other))

    def __radd__(self, other):
        return Character(self._char_value.__radd__(other))

    def __rand__(self, other):
        return Character(self._char_value.__rand__(other))

    def __rfloordiv__(self, other):
        return Character(self._char_value.__rfloordiv__(other))

    def __rlshift__(self, other):
        return Character(self._char_value.__rlshift__(other))

    def __rmod__(self, other):
        return Character(self._char_value.__rmod__(other))

    def __rmul__(self, other):
        return Character(self._char_value.__rmul__(other))

    def __ror__(self, other):
        return Character(self._char_value.__ror__(other))

    def __round__(self, *args):
        if len(args) == 1:
            return Character(self._char_value.__round__(args[0]))
        else:
            return Character(self._char_value.__round__())

    def __rpow__(self, other, *args):
        if len(args) == 1:
            return Character(self._char_value.__rpow__(other, args[0]))
        else:
            return Character(self._char_value.__rpow__(other))

    def __rrshift__(self, other):
        return Character(self._char_value.__rrshift__(other))

    def __rshift__(self, other):
        return Character(self._char_value.__rshift__(other))

    def __rtruediv__(self, other):
        return Character(self._char_value.__rtruediv__(other))

    def __rxor__(self, other):
        return Character(self._char_value.__rxor__(other))

    def __truediv__(self, other):
        return Character(self._char_value.__truediv__(other))

    def __trunc__(self):
        return Character(self._char_value.__trunc__())

    def __xor__(self, other):
        return Character(self._char_value.__xor__(other))
