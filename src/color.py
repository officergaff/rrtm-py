from vec3 import Vec3


class Color(Vec3):
    def to_rgb(self):
        ir = int(255.999 * self.x())
        ig = int(255.999 * self.y())
        ib = int(255.999 * self.z())
        return f"{ir} {ig} {ib}"

    @classmethod
    def from_vec3(cls, v: Vec3):
        return cls(v.x(), v.y(), v.z())

    # Need to override the parent methods
    # Using the parent's magic methods will return the parent type
    def __add__(self, other):
        result = super().__mul__(other)
        return Color.from_vec3(result)

    def __sub__(self, other):
        result = super().__mul__(other)
        return Color.from_vec3(result)

    def __mul__(self, other):
        result = super().__mul__(other)
        return Color.from_vec3(result)

    def __rmul__(self, other):
        result = super().__mul__(other)
        return Color.from_vec3(result)
