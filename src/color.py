from vec3 import Vec3

class Color(Vec3):
    def to_rgb(self):
        ir = int(255.999 * self.x())
        ig = int(255.999 * self.y())
        ib = int(255.999 * self.z())
        return f"{ir} {ig} {ib}"
