import bpy # type: ignore

class HelloWorldPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_embroidery"
    bl_label = "Embroidery"
    bl_space_type = 'VIEW_3D' # this will be in 3D view panel
    bl_region_type = "UI" # 'N' panel
    bl_context = "objectmode" # only in object mode
    bl_category = "Embroidery" # tab name

    def draw(self, context):
        self.layout.label(text="Embroidery")
