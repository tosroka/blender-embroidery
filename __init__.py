# path shenanigans

import os
import sys

import bpy

from . import panel

sys.path.insert(0, os.path.dirname(__file__)+"/pyembroidery")
import pyembroidery

bl_info = {
    "name": "Blender embroidery",
    "blender": (5, 1, 0),
    "category": "Import-Export",
}

def register():
    bpy.utils.register_class(panel.HelloWorldPanel)
    print("Loaded Blender embroidery")

def unregister():
    bpy.utils.unregister_class(panel.HelloWorldPanel)
    print("Unloaded Blender embroidery")