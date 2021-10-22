#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyvista as pv
import panel as pn
import param
import os




class ResultsViewer(param.Parameterized):
    result_type = param.ObjectSelector(default='stress', objects=['stress',
                                                                  'strain',])

    result_dir = param.ObjectSelector(default='magnitude', objects=['magnitude',
                                                                    'XX',
                                                                    'XY',
                                                                    'XZ',
                                                                    'YY',
                                                                    'YZ',
                                                                    'ZZ'])


    def __init__(self):
        super().__init__()

    @param.depends('result_type', 'result_dir')
    def vtk(self):
        here = os.path.dirname(os.path.abspath(__file__))
        file = os.path.join(here, 'V7.vtk')
        mesh = pv.read(file)

        if self.result_dir == 'magnitude':
            scalars_val = mesh[self.result_type]
        else:
            if self.result_dir == 'XX':
                scalars_val = mesh[self.result_type][:,0]
            elif self.result_dir == 'YY':
                scalars_val = mesh[self.result_type][:,1]
            elif self.result_dir == 'ZZ':
                scalars_val = mesh[self.result_type][:,2]
            elif self.result_dir == 'XY':
                scalars_val = mesh[self.result_type][:,3]
            elif self.result_dir == 'YZ':
                scalars_val = mesh[self.result_type][:,4]
            elif self.result_dir == 'XZ':
                scalars_val = mesh[self.result_type][:,5]

        pl = pv.Plotter(notebook=True)
        pl.add_mesh(mesh,
                    scalars = scalars_val,
                    show_edges=True,
                    cmap =  'jet',
                    smooth_shading=True)
        pan = pn.panel(pl.ren_win, height = 650, width = 1000, orientation_widget=True)
        pan.construct_colorbars()
        return pn.Column(pan, pan.construct_colorbars())

    def panel(self):
        return pn.Row(self.param , self.vtk)


if __name__ == '__main__':
    pn.extension()
    explorer = ResultsViewer()
    exp = explorer.panel()

    server = pn.serve(
                      exp, \
                      websocket_max_message_size = 10485760000,\
                      max_buffer_size = 10485760000,\
                      max_body_size = 10485760000,\
                      max_header_size = 10485760000,\
                      verbose = True,\
                      threaded = False\
                     )


