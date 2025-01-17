from vec3 import Point, Vec3
from ray import Ray
from color import Color

def ray_color(r: Ray) -> Color:
    unit_direction = Vec3.unit_vector(r.direction())
    print(unit_direction.y())
    alpha = 0.5 * (unit_direction.y() + 1.0)
    return (1-alpha) * Color(1, 1, 1) + alpha * Color(0.5, 0.7, 1)

class Camera:
    def __init__(self, image_width: int, aspect_ratio: float, viewport_height: float, focal_length: float, camera_center: Point):
        # Image
        self.image_width = image_width
        image_height = int(image_width / aspect_ratio)
        self.image_height = image_height if image_height > 1 else 1

        # Camera
        self.focal_length = focal_length
        self.viewport_height = viewport_height
        self.viewport_width = viewport_height * (float(image_width) / self.image_height)

        self.camera_center = camera_center

        # Unit vectors to navigate across the viewport
        self.viewport_u = Vec3(self.viewport_width, 0, 0)
        self.viewport_v = Vec3(0, -self.viewport_height, 0)

        # Delta vectors from pixel to pixel
        self.pixel_delta_u = self.viewport_u / self.image_width
        self.pixel_delta_v = self.viewport_v / self.image_height

        # Calculate location of the upper-left of the viewport in real-space
        viewport_upper_left = self.camera_center - Vec3(0,0,focal_length) - self.viewport_u/2 - self.viewport_v/2
        # Calculate location of the upper-left pixel in the image
        # We made the decision to place the pixel with a 0.5 pixel_delta distance margin horizontally and vertically
        self.pixel00_loc = viewport_upper_left + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)

    def render(self) -> list[list[Color]]:
        image = []
        for row in range(self.image_height):
            pixel_row = []
            for col in range(self.image_width):
                pixel_center = self.pixel00_loc + (col * self.pixel_delta_u) + (row * self.pixel_delta_v)
                ray_direction = pixel_center - self.camera_center
                r = Ray(self.camera_center, ray_direction)

                pixel_color = ray_color(r)
                pixel_row.append(pixel_color)
            image.append(pixel_row)
        return image
