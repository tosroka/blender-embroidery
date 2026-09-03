# path shenanigans

import os
import sys

import bpy

from .exporters_factory import build_operators
from .panel import EmbroideryPanel, ExportSettings

sys.path.insert(0, os.path.dirname(__file__)+"/pyembroidery")

operators = build_operators()


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


def make_menu_func(menu_id, label):
    def menu_func(self, context):
        layout = self.layout
        if layout is None:
            return

        layout.operator_context = 'INVOKE_DEFAULT'
        layout.menu(menu_id, text=label)
    return menu_func


menu_funcs = []


classes = (ExportSettings,
           EmbroideryPanel,
           EmbroideryExportMenu,
           *operators)

_register, _unregister = bpy.utils.register_classes_factory(classes)


def register():
    _register()
    menu_func = make_menu_func(EmbroideryExportMenu.bl_idname, "Embroidery")
    menu_funcs.append(menu_func)
    bpy.types.TOPBAR_MT_file_export.append(menu_func)  # type: ignore[arg-type]

    bpy.types.WindowManager.emb_settings = bpy.props.PointerProperty(type=ExportSettings)  # type: ignore[attr-defined]
    print("Loaded Blender embroidery")


def unregister():
    for menu_func in reversed(menu_funcs):
        bpy.types.TOPBAR_MT_file_export.remove(menu_func)  # type: ignore[arg-type]
    menu_funcs.clear()

    _unregister()
    del bpy.types.WindowManager.emb_settings  # type: ignore[attr-defined]
    print("Unloaded Blender embroidery")
