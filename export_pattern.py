import os
import sys
from pathlib import Path

import bpy

sys.path.insert(0, os.path.dirname(__file__)+"/pyembroidery")
import pyembroidery

def build_pattern_from_mesh(object: bpy.types.Object, scale) -> pyembroidery.EmbPattern:
    if not isinstance(object.data, bpy.types.Mesh):
        raise TypeError(f"Cannot build pattern from {object.data.__class__}")
    pattern = pyembroidery.EmbPattern()
    pattern.add_command(pyembroidery.JUMP, 
                        object.data.vertices[0].co.x*scale, 
                        object.data.vertices[0].co.y*scale*-1.0)
    for v in object.data.vertices:
        pattern.add_stitch_absolute(pyembroidery.STITCH,
                                    v.co.x*scale,
                                    v.co.y*scale*-1.0)

    return pattern

def export_object(object: bpy.types.Object, scale, writer, filepath: Path):
    # Create EmbPattern from blender curve
    pattern = build_pattern_from_mesh(object, scale)
    match writer:
        case pyembroidery.TxtWriter: # type: ignore[attr-defined]
            with Path(filepath).open("wb") as f:
                writer.write(pattern,f)
        case _:
            with Path(filepath).open("w") as f:
                writer.write(pattern,f)