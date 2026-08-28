# path shenanigans

import os
import sys

import bpy

from .panel import ExportSettings, EmbroideryPanel
from .export_operator import ExportEmbroideryTest

sys.path.insert(0, os.path.dirname(__file__)+"/pyembroidery")
import pyembroidery

classes = (ExportSettings,
           EmbroideryPanel,
           ExportEmbroideryTest,)

_register, _unregister = bpy.utils.register_classes_factory(classes)

def register():
    _register()
    export_operator.register()
    bpy.types.WindowManager.emb_settings = bpy.props.PointerProperty(type=ExportSettings)
    print("Loaded Blender embroidery")

def unregister():
    _unregister()
    export_operator.unregister() 
    del bpy.types.WindowManager.emb_settings 
    print("Unloaded Blender embroidery")
