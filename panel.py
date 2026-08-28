import bpy

class ExportSettings(bpy.types.PropertyGroup):
    scale_float: bpy.props.FloatProperty(
        name="Scale",
        description = "Pattern scale, \n 1m * 10000 = 1m in pattern",
        default=10000,    
    )
    format_list: bpy.props.EnumProperty(
        name="Format",
        items=[
            ('txt', ".txt", "txt Format, Text File"),
            ('json', ".json", "Json Export"),
            ('gcode', ".gcode", "gcode Format, Text File"),
        ],
    )

class EmbroideryPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D' # this will be in 3D view panel
    bl_region_type = "UI" # 'N' panel
    bl_context = "objectmode" # only in object mode
    bl_category = "Embroidery" # tab name
    bl_idname = "OBJECT_PT_embroidery"
    bl_label = "Embroidery Export"
    
    
    def draw(self, context):

        layout = self.layout
        split_size = 0.5

        col = layout.column()
        row = col.row(align=True)
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Format', translate=False)
        row = split.row(align=True)
        row.prop(context.window_manager.emb_settings, 
                'format_list', expand=False, text="", translate=False)

        row = col.row()
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Scale', translate=False)
        row = split.row(align=True)
        row.prop(context.window_manager.emb_settings, 
                 'scale_float', text="", slider=True)

        row = col.row()
        row = col.row(align=True)
        row = col.row(align=True)
        row = col.row(align=True)
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Export', translate=False)
        row = split.row(align=True)
        row.operator('emb.export_test', 
                     emboss=True, text="", icon='EXPORT', translate=False) 
