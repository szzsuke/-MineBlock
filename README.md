# MineBlock

A 3D voxel engine inspired by Minecraft, developed from scratch in Python using ModernGL, Pygame, PyGLM, and Numba.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![OpenGL](https://img.shields.io/badge/OpenGL-3.3%20Core-green)
![ModernGL](https://img.shields.io/badge/ModernGL-5.8%2B-brightgreen)
![Pygame](https://img.shields.io/badge/Pygame-2.5%2B-yellow)

---

## Overview

MineBlock explores the core graphics and performance techniques behind voxel engines:
- **Modern OpenGL Pipeline**: Uses ModernGL to leverage the OpenGL 3.3 Core Profile for hardware-accelerated rendering.
- **Fast Chunk Meshing with Numba**: Utilizes JIT-compiled algorithms with NumPy and Numba to rapidly generate chunk mesh vertices and eliminate hidden faces.
- **GLSL Shaders**: Custom vertex and fragment shaders for world lighting, projection, and voxel rendering.
- **6DoF Player & Camera Controller**: First-person camera system powered by PyGLM vectors and view/projection matrices.

---

## Controls

| Key / Action | Function |
| :--- | :--- |
| **W / A / S / D** | Move Forward / Left / Backward / Right |
| **Q / E** | Move Up / Down |
| **Mouse** | Look around (Yaw & Pitch) |
| **Esc** | Exit Game |

---

## Installation & Setup

1. **Clone the repository:**
   ``bash
   git clone https://github.com/szzsuke/-MineBlock.git
   cd -MineBlock
   ``

2. **Create and activate a virtual environment (optional but recommended):**
   ``bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ``

3. **Install dependencies:**
   ``bash
   pip install -r requirements.txt
   ``

4. **Run the engine:**
   ``bash
   python main.py
   ``

---

## Project Structure

``
MineBlock/
├── assets/             # Textures and static assets
├── meshes/             # Mesh generation and Numba JIT builders
│   ├── base_mesh.py
│   ├── chunk_mesh.py
│   ├── chunk_mesh_builder.py
│   └── quad_mesh.py
├── shaders/            # Custom GLSL vertex and fragment shaders
│   ├── chunk.vert
│   ├── chunk.frag
│   ├── quad.vert
│   └── quad.frag
├── world_objects/      # World and chunk voxel representations
│   └── chunk.py
├── camera.py           # 3D Camera with perspective projection
├── player.py           # Player movement and mouse input handling
├── scene.py            # Scene management and mesh rendering loop
├── settings.py         # Engine settings (resolution, chunk size, FOV)
├── shader_program.py   # Shader compilation and uniform binding
├── main.py             # Main entry point and game loop
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
``

---

## License

This project is licensed under the [MIT License](LICENSE).
