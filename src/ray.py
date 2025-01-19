from vec3 import Point, Vec3


class Ray:
    def __init__(self, origin: Point = Point(), direction: Vec3 = Vec3()):
        self.orig = origin
        self.dir = direction

    def origin(self):
        return self.orig

    def direction(self):
        return self.dir

    def at(self, t) -> Point:
        return self.orig + self.dir * t

    def __repr__(self):
        """Return a string representation of the ray."""
        return f"Ray(origin={self.orig}, direction={self.dir})"
