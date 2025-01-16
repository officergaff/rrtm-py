from vec3 import Vec3
from color import Color

def to_ppm(filename: str, buffer: list[list[float]]):
    width, height = len(buffer[0]), len(buffer)
    with open(f"{filename}.ppm", "w") as file:
        file.write("P3\n")
        file.write(f"{width} {height}\n255\n")
        for row in range(height):
            print(f"scanlines remaining: {height - row}")
            for col in range(width):
                color = Color(col / (width - 1), row / (height - 1), 0)
                file.write(f"{color.to_rgb()}\n")
    return

def main():
    filename = "test"
    width = height = 256
    buffer = [[0.0]*width for _ in range(height)]
    to_ppm(filename, buffer)

if __name__ == "__main__":
    main()
