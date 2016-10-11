import numpy as np


class Value(WithUnit):
    """ A floating-point value with associated units. """
    pass


class Complex(WithUnit):
    """ A complex value with associated units. """
    pass


class ValueArray(WithUnit):
    """ A numpy array with associated units. """
    def __setitem__(WithUnit self, key, val):
        cdef WithUnit right = _in_WithUnit(val)
        if self.base_units != right.base_units:
            raise UnitMismatchError("Item's units don't match array's units.")
        cdef conversion conv = conversion_div(right.conv, self.conv)
        self.value[key] = right.value * conversion_to_double(conv)

    def __copy__(WithUnit self):
        return self.__with_value(copy.copy(self.value))

    def __deepcopy__(WithUnit self, memo):
        return self.__with_value(copy.deepcopy(self.value))

    def __iter__(WithUnit self):
        for e in self.value:
            yield self.__with_value(e)

    def __len__(WithUnit self):
        return len(self.value)

    @property
    def dtype(WithUnit self):
        return self.value.dtype

    @property
    def ndim(WithUnit self):
        return self.value.ndim

    @property
    def shape(WithUnit self):
        return self.value.shape

    def allclose(WithUnit self, other, *args, **kw):
        return np.allclose(self.value, other[self.unit], *args, **kw)


class UnitMismatchError(TypeError):
    """ Incompatible units. """
    pass
