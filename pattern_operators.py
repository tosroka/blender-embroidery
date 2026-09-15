from typing import Any

import bpy


class PatternElement(bpy.types.PropertyGroup):
    def color_changed(self, context):
        print("Color changed",self, self.color, context)

    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype="COLOR",
        size=4,
        min=0.0,
        max=1.0,
        description="Color for the group",
        update=color_changed,
    )


class EMB_OT_add_curve_to_pattern(bpy.types.Operator):
    """Add selected curves to the pattern, ignores non-curve objects."""
    bl_idname = "emb.add_curve_to_pattern"
    bl_label = "Add selected curves to pattern"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context: return False
        return (context.active_object is not None
                and context.active_object.type == 'CURVE')

    def execute(self, context) -> set[Any]:
        if not context: return {'CANCELLED'}
        if not context.selected_objects:
            return {'CANCELLED'}
        selected_curves = [obj for obj in context.selected_objects if obj.type == 'CURVE']
        if not selected_curves:
            if len(context.selected_objects)>0:
                self.report({'WARNING'}, "Selected objects are not curves.")
            return {'CANCELLED'}

        for curve in selected_curves:
            if curve.name not in context.window_manager.emb_pattern_elements:
                new_element = context.window_manager.emb_pattern_elements.add()
                new_element.name = curve.name

        return {'FINISHED'}

class EMB_OT_remove_curve_from_pattern(bpy.types.Operator):
    """Removes selected curves from the pattern, ignores non-curve objects."""
    bl_idname = "emb.remove_curve_from_pattern"
    bl_label = "Remove curve from pattern"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not context: return False
        return (context.active_object is not None
                and context.active_object.type == 'CURVE'
                and context.active_object.name in context.window_manager.emb_pattern_elements)

    def execute(self, context) -> set[Any]:
        if not context: return {'CANCELLED'}
        if not context.active_object:
            return {'CANCELLED'}

        if not context.selected_objects:
            return {'CANCELLED'}

        for selected in context.selected_objects:
            pattern_elements = context.window_manager.emb_pattern_elements
            index = pattern_elements.find(selected.name)
            if index != -1:
                pattern_elements.remove(index)
            else:
                self.report({'WARNING'}, f"Curve '{selected.name}' not part of the pattern.")

        return {'FINISHED'}