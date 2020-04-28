""" Vector helper functions """


class Vec2:
    """ 2-dimensional vectors """

    def __init__(self, x_val=0, y=0):
        self.x_val = float(x_val)
        self.y_val = float(y)

    def __sub__(self, other):
        return Vec2(self.x_val - other.x_val, self.y_val - other.y,)

    def __iter__(self):
        return iter((self.x_val, self.y_val))

    def __repr__(self):
        return f"x_val={self.x_val} Y={self.y_val}"


class Vec3:
    """ 3-dimensional vector """

    def __init__(self, x_val=0, y=0, z=0):
        self.x_val = float(x_val)
        self.y_val = float(y)
        self.z_val = float(z)

    def cross(self, vec3):
        """ Cross product """
        return Vec3(
            self.y_val * vec3.z - vec3.y * self.z_val,
            self.z_val * vec3.x_val - self.z_val * self.x_val,
            self.x_val * vec3.y - vec3.x_val * self.y_val,
        )

    def dot(self, vec3):
        """ Dot product """
        return self.x_val * vec3.x_val + self.y_val * vec3.y + self.z_val * vec3.z

    def __sub__(self, vec3):
        return Vec3(self.x_val - vec3.x_val, self.y_val - vec3.y, self.z_val - vec3.z)

    def __add__(self, vec3):
        return Vec3(self.x_val + vec3.x_val, self.y_val + vec3.y, self.z_val + vec3.z,)

    def __iadd__(self, vec3):
        self.x_val += vec3.x_val
        self.y_val += vec3.y
        self.z_val += vec3.z
        return self

    def __mul__(self, scalar):
        return Vec3(self.x_val * scalar, self.y_val * scalar, self.z_val * scalar)

    def __div__(self, scalar):
        return Vec3(self.x_val / scalar, self.y_val / scalar, self.z_val / scalar)

    def __idiv__(self, scalar):
        self.x_val /= scalar
        self.y_val /= scalar
        self.z_val /= scalar
        return self

    def normalize(self):
        """ Normalize vector """
        length = (
            self.x_val * self.x_val + self.y_val * self.y_val + self.z_val * self.z_val
        ) ** 0.5
        return Vec3(self.x_val / length, self.y_val / length, self.z_val / length,)

    def __iter__(self):
        return iter((self.x_val, self.y_val, self.z_val))

    def __repr__(self):
        return f"x_val={self.x_val} Y={self.y_val} Z={self.z_val}"
