from mayavi import mlab
import numpy as np
from typing import Tuple

from helper import create_wind_rose, create_main_building, create_other_buildings, create_terrain_large, \
    create_terrain_detailed, create_line, create_water, create_cockpit

Custom = (2426, 1365)
mlab.figure(bgcolor=(0.1255, 0.5176, 0.8157), size=Custom)

dt = 0.016
delay = int(dt * 1000)

water = create_water()
line, i_y, intensity = create_line()
wind_rose = create_wind_rose()
main_building = create_main_building()
other_buildings = create_other_buildings()
terrain_large = create_terrain_large()
terrain_detailed = create_terrain_detailed()
use_cockpit = False
if use_cockpit:
    cockpit = create_cockpit()
    for obj in cockpit:
        obj.actor.actor.rotate_z(180)
        obj.actor.actor.rotate_x(90)
else:
    cockpit = None


# scene = mlab.get_engine().scenes[0]
# scene.scene.movie_maker.record = True

def get_intensity(index: int, d: float) -> Tuple[float, float, int]:
    current_intensity = intensity[index]
    factor = 60
    right = 0.001 * np.sin(d * 2) * current_intensity * 0.01 * factor
    up = -current_intensity * 0.01 * factor
    up += 4.86 * 0.01 * factor  # To stay at center of tube (avoid sudden drop when tube is entered)

    distance_to_next = np.sqrt(np.square(i_y[index - 1] - i_y[len(i_y) - 1]))
    if distance_to_next <= d:
        index -= 1

    return right, up, index

    # TODO change origin


@mlab.animate(delay=delay)
def anim():
    line_start = (322.5, 482, 59.1)
    line_flatten = (322.5, -302.7, 18.0)
    line_end = (322.5, -518.0, 18.0)
    cam_start = (322.5, 1000, line_start[2] + np.tan(np.deg2rad(3)) * (1000 - line_start[1]))

    if use_cockpit:
        for obj in cockpit:
            obj.actor.actor.position = (cam_start[0], cam_start[1] - 6, cam_start[2]-0.8)
    mlab.view(azimuth=90, elevation=87, distance=.1, focalpoint=cam_start)

    current_fig = mlab.gcf()
    scene = current_fig.scene
    cam = current_fig.scene.camera

    v = 44  # 160 km/p - Approx. landing speed of DHC-8 300
    v_dt = v * dt
    t = 0
    d = 0
    plane_angle = 3
    index = len(intensity) - 1
    prev_i_move = (0, 0)
    add_y = True

    pitch_start = line_flatten[1] - 10
    pitch_end = line_flatten[1] + 10
    pitch_delta = 3 / ((pitch_end - pitch_start) / v_dt)


    while True:
    #     if t > 3.:
    #         if cam.position[1] <= line_start[1]:
    #             mlab.move(right=-prev_i_move[0], up=-prev_i_move[1])
    #             if use_cockpit:
    #                 pos1 = cockpit[0].actor.actor.position
    #                 for obj in cockpit:
    #                     obj.actor.actor.position = (pos1[0] - prev_i_move[0], pos1[1], pos1[2] - prev_i_move[1])
    #                     # obj.actor.actor.position = (pos1[0], pos1[1], pos1[2])
    #
    #             right, up, index = get_intensity(index, d)
    #             mlab.move(v_dt)
    #             mlab.move(right=right, up=up)
    #
    #             if use_cockpit:
    #                 for obj in cockpit:
    #                     pos2 = obj.actor.actor.position
    #                     obj.actor.actor.position = (pos2[0]+right, pos2[1]-v_dt + (.0022 if add_y else 0.), pos2[2]-(np.tan(np.deg2rad(plane_angle)) * v_dt)+up)
    #                     # obj.actor.actor.position = (pos2[0], pos2[1] - v_dt + (.0022 if add_y else 0.), pos2[2] - np.tan(np.deg2rad(plane_angle)) * v_dt)
    #
    #             prev_i_move = (right, up)
    #             d += v_dt
    #
    #         else:
    #             mlab.move(v_dt)
    #             if use_cockpit:
    #                 for obj in cockpit:
    #                     p = obj.actor.actor.position
    #                     obj.actor.actor.position = (p[0], p[1] - v_dt + .0022, p[2] - np.tan(np.deg2rad(plane_angle)) * v_dt)
    #
    #
    #
    #         if pitch_start < cam.position[1] < pitch_end:
    #             add_y = False
    #             cam.pitch(pitch_delta)
    #             mlab.move(up=-.012)
    #             if use_cockpit:
    #                 for obj in cockpit:
    #                     obj.actor.actor.rotate_x(-pitch_delta)
    #             plane_angle -= pitch_delta
    #
    #         if cam.position[1] <= line_end[1]:
    #             break
    #
        scene.render()
        t += dt
        yield



anim()
# mlab.show_pipeline()
mlab.show()
