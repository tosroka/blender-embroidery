# path shenanigans

import os
import sys

import bpy # type: ignore

from . import export_operator, panel

sys.path.insert(0, os.path.dirname(__file__)+"/pyembroidery")
import pyembroidery

classes = (panel.HelloWorldPanel,
           export_operator.ExportEmbroideryTest,)

_register, _unregister = bpy.utils.register_classes_factory(classes)

def register():
    _register()
    export_operator.register()
    print("Loaded Blender embroidery")

def unregister():
    _unregister()
    export_operator.unregister()  
    print("Unloaded Blender embroidery")
