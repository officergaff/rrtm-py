from abc import ABC, abstractmethod
from ray import Ray
from vec3 import Point, Vec3


class HitRecord:
    def __init__(self, p: Point, normal: Vec3, t: float) -> None:
        self.p = p
        self.normal = normal
        self.t = t


class Hittable(ABC):
    @abstractmethod
    def hit(self, r: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> bool:
        pass
