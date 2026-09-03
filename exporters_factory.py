import sys
import os
from typing import Any
import bpy

sys.path.insert(0, os.path.dirname(__file__)+"/pyembroidery")
import pyembroidery

from .export_pattern import export_object


def execute(self, context: bpy.types.Context | None)-> set[Any]:
    if not context:
        return {'CANCELLED'}
    if context.active_object:
        settings = bpy.context.window_manager.emb_settings
        export_object(context.active_object, settings.scale_float, self.writer, self.filepath)
        return {'PASS_THROUGH'}
    else:
        return {'CANCELLED'}

def invoke(self, context: bpy.types.Context | None, event)-> set[Any]:
    if not context:
        return {'CANCELLED'}
    context.window_manager.fileselect_add(self)

    print("Invoke")
    return {'RUNNING_MODAL'}

def poll(cls, context):
    return (context.active_object is not None
            and context.active_object.type == 'MESH')


class ExportTemplate(bpy.types.Operator):
    """Export embroidery test"""
    bl_idname = "emb.export_test"
    bl_label = "Export Embroidery - Test"

def build_operator_class(ext, description, writer):
    annotations = {
        "filepath": bpy.props.StringProperty(
            name="File Path",
            description="Path to the file",
            subtype='FILE_PATH'
        )
    }

    class_attributes = {
        "bl_idname": f"emb.export_{ext}",
        "bl_label": f"{description} (.{ext})",
        "execute": execute,
        "poll": classmethod(poll),
        "invoke": invoke,
        "writer": writer,
        "__annotations__": annotations,
        "__doc__": f"Export pattern to {ext.upper()} file"
    }
    class_name = f"EMB_OT_{ext}"
    return type(class_name, (bpy.types.Operator,), class_attributes)


def build_operators():
    to_register = []
    for format in pyembroidery.supported_formats():
        operator_class = build_operator_class(format['extension'], format["description"], format.get('writer', None))
        to_register.append(operator_class)
    return to_register