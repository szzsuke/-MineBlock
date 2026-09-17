from dataclasses import dataclass
from typing import Dict, Tuple, Optional


@dataclass(frozen=True)
class Material:
    id: int
    name: str
    is_transparent: bool = False
    is_solid: bool = True
    hardness: float = 1.0
    light_level: int = 0
    # Texture indices for faces: (top, bottom, side)
    texture_top: int = 0
    texture_bottom: int = 0
    texture_side: int = 0

    def get_texture_id(self, face_id: int) -> int:
        """
        Returns texture index based on face_id:
        0: Top (+Y)
        1: Bottom (-Y)
        2, 3, 4, 5: Sides (North, South, East, West)
        """
        if face_id == 0:
            return self.texture_top
        elif face_id == 1:
            return self.texture_bottom
        return self.texture_side


# Standard Material / Block Definitions for MineBlock
AIR = Material(
    id=0,
    name="Air",
    is_transparent=True,
    is_solid=False,
    hardness=0.0
)

GRASS = Material(
    id=1,
    name="Grass",
    is_transparent=False,
    is_solid=True,
    hardness=0.6,
    texture_top=0,
    texture_bottom=2,
    texture_side=1
)

DIRT = Material(
    id=2,
    name="Dirt",
    is_transparent=False,
    is_solid=True,
    hardness=0.5,
    texture_top=2,
    texture_bottom=2,
    texture_side=2
)

STONE = Material(
    id=3,
    name="Stone",
    is_transparent=False,
    is_solid=True,
    hardness=1.5,
    texture_top=3,
    texture_bottom=3,
    texture_side=3
)

SAND = Material(
    id=4,
    name="Sand",
    is_transparent=False,
    is_solid=True,
    hardness=0.5,
    texture_top=4,
    texture_bottom=4,
    texture_side=4
)

WOOD = Material(
    id=5,
    name="Wood",
    is_transparent=False,
    is_solid=True,
    hardness=2.0,
    texture_top=6,
    texture_bottom=6,
    texture_side=5
)

LEAVES = Material(
    id=6,
    name="Leaves",
    is_transparent=True,
    is_solid=True,
    hardness=0.2,
    texture_top=7,
    texture_bottom=7,
    texture_side=7
)

WATER = Material(
    id=7,
    name="Water",
    is_transparent=True,
    is_solid=False,
    hardness=100.0,
    texture_top=8,
    texture_bottom=8,
    texture_side=8
)

BEDROCK = Material(
    id=8,
    name="Bedrock",
    is_transparent=False,
    is_solid=True,
    hardness=-1.0,  # Unbreakable
    texture_top=9,
    texture_bottom=9,
    texture_side=9
)

GLASS = Material(
    id=9,
    name="Glass",
    is_transparent=True,
    is_solid=True,
    hardness=0.3,
    texture_top=10,
    texture_bottom=10,
    texture_side=10
)

COBBLESTONE = Material(
    id=10,
    name="Cobblestone",
    is_transparent=False,
    is_solid=True,
    hardness=2.0,
    texture_top=11,
    texture_bottom=11,
    texture_side=11
)

PLANKS = Material(
    id=11,
    name="Planks",
    is_transparent=False,
    is_solid=True,
    hardness=2.0,
    texture_top=12,
    texture_bottom=12,
    texture_side=12
)


# Registry mapping ID -> Material
MATERIALS: Dict[int, Material] = {
    AIR.id: AIR,
    GRASS.id: GRASS,
    DIRT.id: DIRT,
    STONE.id: STONE,
    SAND.id: SAND,
    WOOD.id: WOOD,
    LEAVES.id: LEAVES,
    WATER.id: WATER,
    BEDROCK.id: BEDROCK,
    GLASS.id: GLASS,
    COBBLESTONE.id: COBBLESTONE,
    PLANKS.id: PLANKS,
}


def get_material(material_id: int) -> Material:
    """Retrieve material by voxel ID, default to AIR if not found."""
    return MATERIALS.get(material_id, AIR)


def is_block_solid(material_id: int) -> bool:
    """Check if the given block is solid for collision detection."""
    mat = get_material(material_id)
    return mat.is_solid


def is_block_transparent(material_id: int) -> bool:
    """Check if the given block is transparent for mesh culling."""
    mat = get_material(material_id)
    return mat.is_transparent
