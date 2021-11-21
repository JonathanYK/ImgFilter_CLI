from PIL import Image

class OverlayFilter:


    def overlay(self):
        with Image.open('input.jpg') as main_img:
            with Image.open('python.png') as over_img:
                over_img = over_img.convert("RGBA")

                main_img.paste(over_img, (0, 0))


                main_img.save("saved2222.png")


    overlay()