import math
from hittable import Hittable, HitRecord
from ray import Ray
from vec3 import Point, Vec3

class Sphere(Hittable):
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = max(radius, 0)

    def hit(self, r: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> bool:
        oc = self.center - r.origin()
        a = r.direction().length_squared()
        h = Vec3.dot(r.direction(), oc)
        c = oc.length_squared() - self.radius**2
        discriminant = h**2 -  a * c
        if discriminant < 0:
            return False
        sqrtd = math.sqrt(discriminant)
        
        # Find nearest root that lies in the acceptable range
        root = (h - sqrtd) / a
        if root <= ray_tmin or root >= ray_tmax:
            root = (h + sqrtd) / a
            if root <= ray_tmin or root >= ray_tmax:
                return False

        rec.t = root
        rec.p = r.at(rec.t)
        rec.normal = (rec.p-self.center) / self.radius

        return True
