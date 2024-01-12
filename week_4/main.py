class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def distance_to(self, Point):
        return ((Point.x - self.x) ** 2 + (Point.y - self.y) ** 2 + (Point.z - self.z) ** 2) ** 0.5

class Segment3D:
    def __init__(self, P1: Point3D, P2: Point3D):
        self.P1 = P1
        self.P2 = P2
    def length(self):
        return ((self.P1.x - self.P2.x) ** 2 + (self.P1.y - self.P2.y) ** 2 + (self.P1.z - self.P2.z) ** 2) ** 0.5
    def middle(self):
        return Point3D((self.P1.x + self.P2.x)/2, (self.P1.y + self.P2.y)/2, (self.P1.z + self.P2.z)/2,)




p1 = Point3D(1, 2, 3)

p2 = Point3D(2.5, 1, -2)

s = Segment3D(p1, p2)

print(s.length())

