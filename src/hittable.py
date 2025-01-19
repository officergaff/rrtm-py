from vec3 import Point, Vec3


class HitRecord:
    def __init__(self, p: Point, normal: Vec3, t: float) -> None:
        self.p = p
        self.normal = normal
        self.t = t
