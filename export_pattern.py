import os
import sys
from enum import Enum
from pathlib import Path

import bpy

sys.path.insert(0, os.path.dirname(__file__)+"/pyembroidery")
import pyembroidery

class ExportFormat(Enum):
    TXT = "txt"
    JSON = "json"

def build_pattern_from_mesh(object: bpy.types.Object) -> pyembroidery.EmbPattern:
    if not isinstance(object.data, bpy.types.Mesh):
        raise TypeError(f"Cannot build pattern from {object.data.__class__}")
    pat = pyembroidery.EmbPattern()
    pat.add_command(pyembroidery.JUMP, object.data.vertices[0].co.x, object.data.vertices[0].co.y)
    for v in object.data.vertices:
        pat.add_stitch_absolute(pyembroidery.STITCH,v.co.x,v.co.y)

    return pat

def export_object(filepath: Path, format, object: bpy.types.Object):
    # Create EmbPattern from blender curve

    pat = build_pattern_from_mesh(object)
    match format:
        case ExportFormat.TXT:
            with Path(filepath).open("wb") as f:
                pyembroidery.write_txt(pat,f)
        case ExportFormat.JSON:
            with Path(filepath).open("w") as f:
                pyembroidery.write_json(pat,f)
    