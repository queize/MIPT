from Point3D import *

A = Point3D(0, 2, 3)
B = Point3D(1, 1, 1)

AB = Segment3D(A, B)
BA = Segment3D(B, A)

print(
    f"dist(A, B) = {A.distance_to(B)}",
    f"dist(B, A) = {B.distance_to(A)}",
    f"middle(AB) = {AB.middle()}",
    f"cos(A, B) = {AB.cos_to(BA)}",
    sep='\n'
    )