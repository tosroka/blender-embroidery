# path shenanigans

import os
import sys

import bpy

from . import export_operator, panel

sys.path.insert(0, os.path.dirname(__file__)+"/pyembroidery")
import pyembroidery


def register():
    bpy.utils.register_class(panel.HelloWorldPanel)
    export_operator.register()
    print("Loaded Blender embroidery")

def unregister():
    export_operator.unregister()
    bpy.utils.unregister_class(panel.HelloWorldPanel)
    print("Unloaded Blender embroidery")