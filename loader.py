from threading import Thread
from mayavi import mlab


class LoadObject(Thread):
    def __init__(self, v_file: str, f_file: str):
        Thread.__init__(self)
        self.v_file = v_file
        self.f_file = f_file
        self.x = []
        self.y = []
        self.z = []
        self.triangles = []
        # self.scalars = []

    def run(self):
        v_thread = LoadVertices(self.v_file)
        f_thread = LoadFaces(self.f_file)

        v_thread.start()
        f_thread.start()

        v_thread.join()
        f_thread.join()

        self.x, self.y, self.z = v_thread.get_vertices()
        # self.triangles, self.scalars = f_thread.get_faces_and_scalars()
        self.triangles = f_thread.get_faces_and_scalars()

    def get_object(self):
        # return mlab.triangular_mesh(self.x, self.y, self.z, self.triangles, self.scalars)
        return mlab.triangular_mesh(self.x, self.y, self.z, self.triangles)


class LoadVertices(Thread):
    def __init__(self, v_file: str):
        Thread.__init__(self)
        self.v_file = v_file
        self.x = []
        self.y = []
        self.z = []

    def run(self):
        for line in open(self.v_file):
            split: [float] = line.split()
            self.x.append(float(split[0]))
            self.y.append(float(split[1]))
            self.z.append(float(split[2]))

    def get_vertices(self) -> (list, list, list):
        return self.x, self.y, self.z


class LoadFaces(Thread):
    def __init__(self, f_file: str):
        Thread.__init__(self)
        self.f_file = f_file
        self.triangles = []
        # self.scalars = []

    def run(self):
        for line in open(self.f_file):
            split: [int] = line.split()
            self.triangles.append((int(split[0]) - 1, int(split[1]) - 1, int(split[2]) - 1))

    def get_faces_and_scalars(self) -> (list, list):
        return self.triangles  # , self.scalars
