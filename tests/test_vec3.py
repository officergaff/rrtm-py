import math
from src.vec3 import Vec3

v1 = Vec3(1,1,1)
v2 = Vec3(2,2,2)

def test_add():
    v3 = v1 + v2
    assert v3.x() == 3 and v3.y() == 3 and v3.z() == 3

def test_subtract():
    assert v2 - v1 == Vec3(1,1,1)

def test_scalar_mul():
    assert v2 * 5 == Vec3(10,10,10)

def test_vec_mul():
    assert v1 * v2 == Vec3(2,2,2)

def test_truediv():
    assert v2 / 4 == Vec3(0.5, 0.5, 0.5)

def test_length_squared():
    assert v2.length_squared() == 12

def test_length():
    assert v2.length() == math.sqrt(12)

def test_unit_vector():
    u = Vec3.unit_vector(v2)
    v = v2 / math.sqrt(12)
    assert u == v

def test_dot():
    assert Vec3.dot(v1, v2) == 6

def test_cross():
    assert Vec3.cross(v1, v2) == Vec3(0,0,0)
