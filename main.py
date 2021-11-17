from mayavi import mlab
import numpy as np

from helper import create_wind_rose, create_main_building, create_other_buildings, create_terrain_large, \
    create_terrain_detailed, create_line, create_water

dt = .016
delay = int(dt * 1000)


water = create_water()
wind_rose = create_wind_rose()
main_building = create_main_building()
other_buildings = create_other_buildings()
terrain_large = create_terrain_large()
terrain_detailed = create_terrain_detailed()
line = create_line()


@mlab.animate(delay=delay)
def anim():
    line_start = (322.5, 482, 59.1)
    line_flatten = (322.5, -302.7, 18.0)
    line_end = (322.5, -518.0, 18.0)
    cam_start = (322.5, 1000, line_start[2] + np.tan(np.deg2rad(3)) * (1000 - line_start[1]))
    mlab.view(azimuth=90, elevation=87, distance=.1, focalpoint=cam_start)

    current_fig = mlab.gcf()
    scene = current_fig.scene
    cam = current_fig.scene.camera

    v = 44  # 160 km/p - Approx. landing speed of DHC-8 300
    v_dt = v * dt
    t = 0
    d = 0
    prev_i_move = (0, 0)

    pitch_start = line_flatten[1] - 10
    pitch_end = line_flatten[1] + 10
    pitch_delta = 3. / ((pitch_end - pitch_start) / (v * dt))

    while True:
        if t > 3.:
            if cam.position[1] <= line_start[1]:
                mlab.move(right=-prev_i_move[0], up=-prev_i_move[1])
                mlab.move(v_dt)
                d += v_dt
            else:
                mlab.move(v_dt)

            if pitch_start < cam.position[1] < pitch_end:
                cam.pitch(pitch_delta)

            if cam.position[1] <= line_end[1]:
                break

        scene.render()
        t += dt
        yield


anim()
# mlab.show_pipeline()
mlab.show()
