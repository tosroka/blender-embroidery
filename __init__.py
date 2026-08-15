# path shenanigans

import os
import sys

sys.path.insert(0, os.path.dirname(__file__)+"/pyembroidery")
import pyembroidery

bl_info = {
    "name": "Blender embroidery",
    "blender": (5, 1, 0),
    "category": "Import-Export",
}

def register():
    imported = pyembroidery.read_dst("test/random1-me.dst")
    print("Loaded Blender embroidery")
def unregister():
    print("Unloaded Blender embroidery")