import bpy

from .exporters_factory import operators


class ExportSettings(bpy.types.PropertyGroup):
    scale_float: bpy.props.FloatProperty(
        name="Scale",
        description = "Pattern scale, \n 1m * 10000 = 1m in pattern",
        default=10000,    
    )
    format_list: bpy.props.EnumProperty(
        name="Format",
        items=[ (o.filename_ext, o.filename_ext, o.bl_label, 'NONE', idx) for idx, o in enumerate(operators)], # type: ignore
    )

class EmbroideryPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D' # this will be in 3D view panel
    bl_region_type = "UI" # 'N' panel
    bl_context = "objectmode" # only in object mode
    bl_category = "Embroidery" # tab name
    bl_idname = "OBJECT_PT_embroidery"
    bl_label = "Embroidery Export"

    def draw_object_stack(self, layout: bpy.types.UILayout):
        layout.label(text='Pattern stack')
        box = layout.box()

        pattern_elements : bpy.types.CollectionProperty = bpy.context.window_manager.emb_pattern_elements

        for obj in pattern_elements:
            row = box.row(align=True)
            row.label(text=obj.name)
            row.prop(obj, 'color', text="")

        row = layout.row()
        row.operator("emb.add_curve_to_pattern", emboss=True, text="Add object", icon="ADD")
        row.operator("emb.remove_curve_from_pattern", emboss=True, text="Remove object", icon="REMOVE")

    def draw_export(self, layout: bpy.types.UILayout, types_enum_prop: bpy.types.PropertyGroup):
        # format selector and export button
        split_size = 0.5

        col = layout.column()
        if not col: return 
        row = col.row(align=True)
        if not row: return
        split = row.split(align=True, factor=split_size)
        if not split: return
        row = split.row(align=True)
        if not row: return
        row.label(text='File format', translate=False)
        row = split.row(align=True)
        if not row: return
        row.prop(types_enum_prop, 
                'format_list', expand=False, text="", translate=False)

        # row = col.row()
        # split = row.split(align=True, factor=split_size)
        # row = split.row(align=True)
        # row.label(text='Scale', translate=False)
        # row = split.row(align=True)
        # row.prop(context.window_manager.emb_settings, 
        #          'scale_float', text="", slider=True)

        operator_index = types_enum_prop.get("format_list", 0)
        current_export_operator = operators[operator_index].bl_idname
    
        row.operator(current_export_operator, emboss=True, text="", icon='EXPORT', translate=False)

    
    
    def draw(self, context):
        layout = self.layout
        if not layout or not context:
            return

        settings = context.window_manager.emb_settings

        self.draw_object_stack(layout)
        self.draw_export(layout, settings)

        
