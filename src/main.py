from camera import Camera
from color import Color
from vec3 import Point, Vec3

def to_ppm(filename: str, image: list[list[Color]]):
    width, height = len(image[0]), len(image)
    with open(f"{filename}.ppm", "w") as file:
        file.write("P3\n")
        file.write(f"{width} {height}\n255\n")

        for row in range(height):
            for col in range(width):
                color = image[row][col]
                file.write(f"{color.to_rgb()}\n")
    return

def main():
    filename = "test"
    camera = Camera(400, 16.0/9.0, 2.0, 1.0, Point(0,0,0))
    image = camera.render()
    to_ppm(filename, image)

if __name__ == "__main__":
    main()
