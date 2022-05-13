class Point2D:
    _point_count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point2D._point_count += 1

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    @classmethod
    def get_point_count(cls):
        return cls._point_count


class Point3D(Point2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2) ** 0.5


first_point_2d = Point2D(10, 20)
second_point_2d = Point2D(30, 50)
print(first_point_2d.get_point_count())
print(second_point_2d.get_point_count())
first_point_3d = Point3D(10, 20, 30)
second_point_3d = Point3D(30, 20, 10)
print(first_point_3d.distance(second_point_3d))