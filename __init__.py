# path shenanigans

import os
import sys

import bpy

from .exporters_factory import operators
from .panel import EmbroideryPanel, ExportSettings

sys.path.insert(0, os.path.dirname(__file__)+"/pyembroidery")


class EmbroideryExportMenu(bpy.types.Menu):
    bl_idname = "TOPBAR_MT_file_export_embroidery"
    bl_label = "Embroidery"

    def draw(self, context):
        layout = self.layout
        if layout is None:
            return

        for op in operators:
            layout.operator_context = 'INVOKE_DEFAULT'
            layout.operator(op.bl_idname, text=op.bl_label or op.__name__)

def menu_func(self: bpy.types.Menu, context):
    layout = self.layout
    if layout is None:
        return

    layout.operator_context = 'INVOKE_DEFAULT'
    layout.menu(EmbroideryExportMenu.bl_idname, text="Embroidery")

classes = (ExportSettings,
           EmbroideryPanel,
           EmbroideryExportMenu,
           *operators)

_register, _unregister = bpy.utils.register_classes_factory(classes)


def register():
    _register()
    bpy.types.TOPBAR_MT_file_export.append(menu_func)  # type: ignore[arg-type]

    bpy.types.WindowManager.emb_settings = bpy.props.PointerProperty(type=ExportSettings)  # type: ignore[attr-defined]
    print("Loaded Blender embroidery")


def unregister():
    bpy.types.TOPBAR_MT_file_export.remove(menu_func)  # type: ignore[arg-type]

    _unregister()
    del bpy.types.WindowManager.emb_settings  # type: ignore[attr-defined]
    print("Unloaded Blender embroidery")
