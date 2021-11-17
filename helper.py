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

from data.faces.main_building_f import main_building_f
from data.faces.other_buildings_f import other_buildings_f
from data.faces.terrain_detailed_f import terrain_detailed_f
from data.faces.terrain_large_f import terrain_large_f
from data.faces.wind_rose_f import wind_rose_f
from data.faces.water_f import water_f

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
                                colormap='gist_earth') #(0.5843, 0.6471, 0.5843)


def create_terrain_large():
    return mlab.triangular_mesh(terrain_large_v_x, terrain_large_v_y, terrain_large_v_z, terrain_large_f,
                                colormap='gist_earth')  #(0.0353, 0.3216, 0.1569)


def create_wind_rose():
    return mlab.triangular_mesh(wind_rose_v_x, wind_rose_v_y, wind_rose_v_z, wind_rose_f, color=(1, 0.8431, 0))


def create_water():
    return mlab.triangular_mesh(water_v_x, water_v_y, water_v_z, water_f, color=(0.1098, 0.1569, 0.2588))


def create_line():
    data = np.genfromtxt("data/csv/data.csv", delimiter=";")
    data = np.transpose(data)
    x, y, z, I, u, delta_u, U_prime = data
    return mlab.plot3d(x, y, z, I, tube_radius=9, tube_sides=30, opacity=0.45), y, I


def process_obj_file_v(original: str, new_file: str, type: str, obj_name: str):
    with open(original) as original:
        out_x = open(new_file + '_x' + f'.{type}', 'w')
        out_x.write(f'{obj_name}_x = [')
        out_y = open(new_file + '_y' + f'.{type}', 'w')
        out_y.write(f'{obj_name}_y = [')
        out_z = open(new_file + '_z' + f'.{type}', 'w')
        out_z.write(f'{obj_name}_z = [')

        new_line_counter = 0
        for line in original:
            split = line.split()
            if split[0] == 'v':
                new_line_counter += 1
                out_x.write(f'{float(split[1])}, ')
                out_y.write(f'{float(split[2])}, ')
                out_z.write(f'{float(split[3])}, ')
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
    #
    # process_obj_file_f('data/obj/wind_rose.obj', 'data/faces/wind_rose_f', '.py', 'wind_rose_f')
    # process_obj_file_f('data/obj/terrain_detailed.obj', 'data/faces/terrain_detailed_f', '.py', 'terrain_detailed_f')
    # process_obj_file_f('data/obj/terrain_large.obj', 'data/faces/terrain_large_f', '.py', 'terrain_large_f')
    # process_obj_file_f('data/obj/other_buildings.obj', 'data/faces/other_buildings_f', '.py', 'other_buildings_f')
    # process_obj_file_f('data/obj/main_building.obj', 'data/faces/main_building_f', '.py', 'main_building_f')
    # process_obj_file_f('data/obj/water.obj', 'data/faces/water_f', '.py', 'water_f')


# main()