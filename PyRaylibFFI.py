import ctypes
import numpy as np

# Load Raylib shared library (.dylib on macOS)
raylib = ctypes.CDLL('CLib/Raylib/lib/libraylib.dylib')  # Adjust path if necessary

# Define constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define Raylib's Color structure (r, g, b, a)
class Color(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_ubyte),  # Red component (0-255)
        ("g", ctypes.c_ubyte),  # Green component (0-255)
        ("b", ctypes.c_ubyte),  # Blue component (0-255)
        ("a", ctypes.c_ubyte),  # Alpha component (0-255)
    ]

# Define test colors
RED = Color(255, 0, 0, 255)
BLUE = Color(0, 121, 241, 255)
GREEN = Color(0, 255, 0, 255)
RAYLIB_WHITE= Color(245, 245, 245, 255)

# Function signatures for Raylib
raylib.InitWindow.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
raylib.InitWindow.restype = None
raylib.SetTargetFPS.argtypes = [ctypes.c_int]
raylib.SetTargetFPS.restype = None
raylib.BeginDrawing.restype = None
raylib.EndDrawing.restype = None
raylib.ClearBackground.argtypes = [Color]
raylib.ClearBackground.restype = None
raylib.DrawRectangle.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, Color]
raylib.DrawRectangle.restype = None
raylib.WindowShouldClose.restype = ctypes.c_bool
raylib.CloseWindow.restype = None

# Initialize the window
raylib.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, b"Scatter Plot Example with Rectangles")
raylib.SetTargetFPS(60)

# Number of rectangles to draw
num_rectangles = 100
# Generate random scatter plot data
data_points = np.random.rand(num_rectangles, 2)  # 100 random points in [0, 1] range
rectangle_size = 10  # Size of the rectangles

# Main loop
while not raylib.WindowShouldClose():
    # Start drawing
    raylib.BeginDrawing()

    # Clear the background with RED color
    raylib.ClearBackground(RAYLIB_WHITE)

    # Draw random rectangles
    for point in data_points:
        x = int(point[0] * SCREEN_WIDTH)  # Map point's x-coordinate to screen width
        y = int(point[1] * SCREEN_HEIGHT)  # Map point's y-coordinate to screen height
        # Draw a small rectangle
        raylib.DrawRectangle(x, y, rectangle_size, rectangle_size, BLUE)

    # End drawing
    raylib.EndDrawing()

# Close window when done
raylib.CloseWindow()
