from data.vertices.main_building_v_x import main_building_v_x
from data.vertices.main_building_v_y import main_building_v_y
from data.vertices.main_building_v_z import main_building_v_z
from data.vertices.other_buildings_v_x import other_buildings_v_x
from data.vertices.other_buildings_v_y import other_buildings_v_y
from data.vertices.other_buildings_v_z import other_buildings_v_z
from data.vertices.terrain_large_v_x import terrain_large_v_x
from data.vertices.terrain_large_v_y import terrain_large_v_y
from data.vertices.terrain_large_v_z import terrain_large_v_z
from data.vertices.terrain_detailed_v_x import terrain_detailed_v_x
from data.vertices.terrain_detailed_v_y import terrain_detailed_v_y
from data.vertices.terrain_detailed_v_z import terrain_detailed_v_z
from data.vertices.wind_rose_v_x import wind_rose_v_x
from data.vertices.wind_rose_v_y import wind_rose_v_y
from data.vertices.wind_rose_v_z import wind_rose_v_z
from data.vertices.water_v_x import water_v_x
from data.vertices.water_v_y import water_v_y
from data.vertices.water_v_z import water_v_z
from data.vertices.cockpit_base_v_x import cockpit_base_v_x
from data.vertices.cockpit_base_v_y import cockpit_base_v_y
from data.vertices.cockpit_base_v_z import cockpit_base_v_z
from data.vertices.cockpit0_v_x import cockpit0_v_x
from data.vertices.cockpit0_v_y import cockpit0_v_y
from data.vertices.cockpit0_v_z import cockpit0_v_z
from data.vertices.cockpit1_v_x import cockpit1_v_x
from data.vertices.cockpit1_v_y import cockpit1_v_y
from data.vertices.cockpit1_v_z import cockpit1_v_z
from data.vertices.cockpit2_v_x import cockpit2_v_x
from data.vertices.cockpit2_v_y import cockpit2_v_y
from data.vertices.cockpit2_v_z import cockpit2_v_z
from data.vertices.cockpit3_v_x import cockpit3_v_x
from data.vertices.cockpit3_v_y import cockpit3_v_y
from data.vertices.cockpit3_v_z import cockpit3_v_z
from data.vertices.cockpit4_v_x import cockpit4_v_x
from data.vertices.cockpit4_v_y import cockpit4_v_y
from data.vertices.cockpit4_v_z import cockpit4_v_z
from data.vertices.cockpit5_v_x import cockpit5_v_x
from data.vertices.cockpit5_v_y import cockpit5_v_y
from data.vertices.cockpit5_v_z import cockpit5_v_z
from data.vertices.cockpit6_v_x import cockpit6_v_x
from data.vertices.cockpit6_v_y import cockpit6_v_y
from data.vertices.cockpit6_v_z import cockpit6_v_z

from data.faces.main_building_f import main_building_f
from data.faces.other_buildings_f import other_buildings_f
from data.faces.terrain_detailed_f import terrain_detailed_f
from data.faces.terrain_large_f import terrain_large_f
from data.faces.wind_rose_f import wind_rose_f
from data.faces.water_f import water_f
from data.faces.cockpit_base_f import cockpit_base_f
from data.faces.cockpit0_f import cockpit0_f
from data.faces.cockpit1_f import cockpit1_f
from data.faces.cockpit2_f import cockpit2_f
from data.faces.cockpit3_f import cockpit3_f
from data.faces.cockpit4_f import cockpit4_f
from data.faces.cockpit5_f import cockpit5_f
from data.faces.cockpit6_f import cockpit6_f

from mayavi import mlab
import numpy as np


def create_main_building():
    return mlab.triangular_mesh(main_building_v_x, main_building_v_y, main_building_v_z, main_building_f,
                                color=(0.9922, 0.2471, 0.5725))


def create_other_buildings():
    return mlab.triangular_mesh(other_buildings_v_x, other_buildings_v_y, other_buildings_v_z, other_buildings_f,
                                color=(1, 1, 1))


def create_terrain_detailed():
    return mlab.triangular_mesh(terrain_detailed_v_x, terrain_detailed_v_y, terrain_detailed_v_z, terrain_detailed_f,
                                colormap='gist_earth')  # (0.5843, 0.6471, 0.5843)


def create_terrain_large():
    return mlab.triangular_mesh(terrain_large_v_x, terrain_large_v_y, terrain_large_v_z, terrain_large_f,
                                colormap='gist_earth')  # (0.0353, 0.3216, 0.1569)


def create_wind_rose():
    return mlab.triangular_mesh(wind_rose_v_x, wind_rose_v_y, wind_rose_v_z, wind_rose_f, color=(1, 0.8431, 0))


def create_water():
    return mlab.triangular_mesh(water_v_x, water_v_y, water_v_z, water_f, color=(0.1098, 0.1569, 0.2588))


def create_line():
    data = np.genfromtxt("data/csv/data.csv", delimiter=";")
    data = np.transpose(data)
    x, y, z, I, u, delta_u, U_prime = data
    return mlab.plot3d(x, y, z, I, tube_radius=9, tube_sides=30, opacity=0.45), y, I

# def create_line():
#     data = np.genfromtxt("data/csv/data.csv", delimiter=";")
#     data = np.transpose(data)
#     x, y, z, I, u, delta_u, U_prime = data
#     return mlab.plot3d(x, y, z, delta_u, tube_radius=9, tube_sides=30, opacity=0.45), y, delta_u


def create_cockpit():
    return mlab.triangular_mesh(cockpit_base_v_x, cockpit_base_v_y, cockpit_base_v_z, cockpit_base_f,
                                color=(0.86098, 0.90196, 0.9647)), \
           mlab.triangular_mesh(cockpit0_v_x, cockpit0_v_y, cockpit0_v_z, cockpit0_f,
                                color=(0.4, 0.4549, 0.5333)), \
           mlab.triangular_mesh(cockpit1_v_x, cockpit1_v_y, cockpit1_v_z, cockpit1_f, color=(0.4666, 0.5176, 0.5647)), \
           mlab.triangular_mesh(cockpit2_v_x, cockpit2_v_y, cockpit2_v_z, cockpit2_f, color=(0.6157, 0.6118, 0.6275)), \
           mlab.triangular_mesh(cockpit3_v_x, cockpit3_v_y, cockpit3_v_z, cockpit3_f, color=(0.3255, 0.3451, 0.3725)), \
           mlab.triangular_mesh(cockpit4_v_x, cockpit4_v_y, cockpit4_v_z, cockpit4_f, color=(0.2196, 0.2314, 0.2627)), \
           mlab.triangular_mesh(cockpit5_v_x, cockpit5_v_y, cockpit5_v_z, cockpit5_f, color=(0.2353, 0.2588, 0.2941)), \
           mlab.triangular_mesh(cockpit6_v_x, cockpit6_v_y, cockpit6_v_z, cockpit6_f, color=(0.1686, 0.1765, 0.1961))


def process_obj_file_v(original: str, new_file: str, type: str, obj_name: str):
    with open(original) as original:
        out_x = open(new_file + '_x' + f'{type}', 'w')
        out_x.write(f'{obj_name}_x = [')
        out_y = open(new_file + '_y' + f'{type}', 'w')
        out_y.write(f'{obj_name}_y = [')
        out_z = open(new_file + '_z' + f'{type}', 'w')
        out_z.write(f'{obj_name}_z = [')

        new_line_counter = 0
        for line in original:
            if line == '\n':
                continue
            split = line.split()
            if split[0] == 'v':
                new_line_counter += 1
                out_x.write(f'{float(split[1])/55}, ')
                out_y.write(f'{float(split[2])/55}, ')
                out_z.write(f'{float(split[3])/55}, ')
                if new_line_counter % 5 == 0:
                    out_x.write('\n     ')
                    out_y.write('\n     ')
                    out_z.write('\n     ')

        out_x.write(']\n')
        out_y.write(']\n')
        out_z.write(']\n')


def process_obj_file_f(original: str, new_file: str, type: str, obj_name: str):
    with open(original) as in_file:
        with open(new_file + type, 'w') as out_file:
            out_file.write(obj_name + ' = [\n')

            for line in in_file:
                if line == '\n':
                    continue
                split = line.split()
                if split[0] == 'f':
                    out_file.write('    (')
                    for i in range(1, 4):
                        split_slash = split[i].split('/')
                        out_file.write(f'{int(split_slash[0]) - 1}')
                        if i < 3:
                            out_file.write(', ')
                    out_file.write('),\n')

            out_file.write(']\n')

# def main():
# process_obj_file_v('data/obj/wind_rose.obj', 'data/vertices/wind_rose_v', '.py', 'wind_rose_v')
# process_obj_file_v('data/obj/terrain_detailed.obj', 'data/vertices/terrain_detailed_v', '.py', 'terrain_detailed_v')
# process_obj_file_v('data/obj/terrain_large.obj', 'data/vertices/terrain_large_v', '.py', 'terrain_large_v')
# process_obj_file_v('data/obj/other_buildings.obj', 'data/vertices/other_buildings_v', '.py', 'other_buildings_v')
# process_obj_file_v('data/obj/main_building.obj', 'data/vertices/main_building_v', '.py', 'main_building_v')
# process_obj_file_v('data/obj/water.obj', 'data/vertices/water_v', '.py', 'water_v')
#     process_obj_file_v('data/obj/cockpit_base.obj', 'data/vertices/cockpit_base_v', '.py', 'cockpit_base_v')
#     process_obj_file_v('data/obj/cockpit0.obj', 'data/vertices/cockpit0_v', '.py', 'cockpit0_v')
#     process_obj_file_v('data/obj/cockpit1.obj', 'data/vertices/cockpit1_v', '.py', 'cockpit1_v')
#     process_obj_file_v('data/obj/cockpit2.obj', 'data/vertices/cockpit2_v', '.py', 'cockpit2_v')
#     process_obj_file_v('data/obj/cockpit3.obj', 'data/vertices/cockpit3_v', '.py', 'cockpit3_v')
#     process_obj_file_v('data/obj/cockpit4.obj', 'data/vertices/cockpit4_v', '.py', 'cockpit4_v')
#     process_obj_file_v('data/obj/cockpit5.obj', 'data/vertices/cockpit5_v', '.py', 'cockpit5_v')
#     process_obj_file_v('data/obj/cockpit6.obj', 'data/vertices/cockpit6_v', '.py', 'cockpit6_v')

# process_obj_file_f('data/obj/wind_rose.obj', 'data/faces/wind_rose_f', '.py', 'wind_rose_f')
# process_obj_file_f('data/obj/terrain_detailed.obj', 'data/faces/terrain_detailed_f', '.py', 'terrain_detailed_f')
# process_obj_file_f('data/obj/terrain_large.obj', 'data/faces/terrain_large_f', '.py', 'terrain_large_f')
# process_obj_file_f('data/obj/other_buildings.obj', 'data/faces/other_buildings_f', '.py', 'other_buildings_f')
# process_obj_file_f('data/obj/main_building.obj', 'data/faces/main_building_f', '.py', 'main_building_f')
# process_obj_file_f('data/obj/water.obj', 'data/faces/water_f', '.py', 'water_f')
#     process_obj_file_f('data/obj/cockpit_base.obj', 'data/faces/cockpit_base_f', '.py', 'cockpit_base_f')
#     process_obj_file_f('data/obj/cockpit0.obj', 'data/faces/cockpit0_f', '.py', 'cockpit0_f')
#     process_obj_file_f('data/obj/cockpit1.obj', 'data/faces/cockpit1_f', '.py', 'cockpit1_f')
#     process_obj_file_f('data/obj/cockpit2.obj', 'data/faces/cockpit2_f', '.py', 'cockpit2_f')
#     process_obj_file_f('data/obj/cockpit3.obj', 'data/faces/cockpit3_f', '.py', 'cockpit3_f')
#     process_obj_file_f('data/obj/cockpit4.obj', 'data/faces/cockpit4_f', '.py', 'cockpit4_f')
#     process_obj_file_f('data/obj/cockpit5.obj', 'data/faces/cockpit5_f', '.py', 'cockpit5_f')
#     process_obj_file_f('data/obj/cockpit6.obj', 'data/faces/cockpit6_f', '.py', 'cockpit6_f')
#
#
# main()
