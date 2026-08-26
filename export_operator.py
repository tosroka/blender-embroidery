from typing import Any

import bpy

from .export_pattern import ExportFormat, export_object


class ExportEmbroideryTest(bpy.types.Operator):
    """Export embroidery test"""
    bl_idname = "emb.export_test"
    bl_label = "Export Embroidery - Test"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context: bpy.types.Context | None)-> set[Any]:
        if not context:
            return {'CANCELLED'}
        if context.active_object:
            export_object(self.filepath, ExportFormat.JSON, context.active_object)
            return {'PASS_THROUGH'}
        else:
            return {'CANCELLED'}

    def invoke(self, context: bpy.types.Context | None, event)-> set[Any]:
        if not context:
            return {'CANCELLED'}
        context.window_manager.fileselect_add(self)

        print("Invoke")
        return {'RUNNING_MODAL'}


# Only needed if you want to add into a dynamic menu.
def menu_func(self):
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator(ExportEmbroideryTest.bl_idname, text="Text Export Operator")


# Register and add to the file selector (required to also use F3 search "Text Export Operator" for quick access).
def register():
    bpy.utils.register_class(ExportEmbroideryTest)
    bpy.types.TOPBAR_MT_file_export.append(menu_func)

def unregister():
    bpy.utils.unregister_class(ExportEmbroideryTest)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func)