from PIL import ImageFilter

class BlackAndWhiteFilter:
    def apply_filter(self, image):
        # Convert the image to grayscale
        baw_image = image.convert("L")
        # Convert the grayscale image to black and white
        black_white_image = baw_image.convert("1")
        return black_white_image

class GrayscaleFilter:
    def apply_filter(self, image):
        # Convert the image to grayscale
        grayscale_image = image.convert("L")
        return grayscale_image

class EdgesFilter:
    def apply_filter(self, image):
        # Convert the image to grayscale
        grayscale_image = image.convert("L")
        cartoon_image = grayscale_image.filter(ImageFilter.FIND_EDGES)
        return cartoon_image