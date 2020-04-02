'''Imaging module for generators'''
import time
from uuid import uuid4
from PIL import Image

import generate


def frame2monoimage(frame):
    '''Produce a monocolor image from a frame''' 

    img = Image.new(
        'RGB', (generate.FRAME_SIZE, generate.FRAME_SIZE), (0, 0, 0)
    )

    for x in range(generate.FRAME_SIZE):
        for y in range(generate.FRAME_SIZE):
            intensity = int(255 * frame.density_norm[x, y])
            img.putpixel((y, x), (intensity, intensity, intensity))
    
    return img


def frame2image(red_frame, green_frame, blue_frame):
    '''Produce a color image from three channel frames'''

    assert len(red_frame) == len(green_frame) == len(blue_frame)

    img = Image.new(
        'RGB', (generate.FRAME_SIZE, generate.FRAME_SIZE), (0, 0, 0)
    )

    for x in range(generate.FRAME_SIZE):
        for y in range(generate.FRAME_SIZE):
            red_intensity = int(255 * red_frame.density_norm[x, y])
            green_intensity = int(255 * green_frame.density_norm[x, y])
            blue_intensity = int(255 * blue_frame.density_norm[x, y])

            img.putpixel((y, x), (red_intensity, green_intensity, blue_intensity))
    
    return img


# def color_images(r_gen, g_gen, b_gen):
#     '''Produce color images using the red, green, and blue frames'''
#     image_id = uuid4()
#     print(f"imag {str(image_id)[:6]} ", end='', flush=True)

#     assert len(r_gen.frames) == len(g_gen.frames) == len(b_gen.frames)

#     time_str = time.strftime("%Y%m%d%H%M%S")
#     name = f"{image_id}_{time_str}"

#     for i in range(len(r_gen.frames)):
#         img = Image.new(
#             'RGB', (generate.FRAME_SIZE, generate.FRAME_SIZE), (0, 0, 0)
#         )

#         for x in range(generate.FRAME_SIZE):
#             for y in range(generate.FRAME_SIZE):
#                 r = int(255 * r_gen.frames[i].density_norm[x, y])
#                 g = int(255 * g_gen.frames[i].density_norm[x, y])
#                 b = int(255 * b_gen.frames[i].density_norm[x, y])

#                 img.putpixel((y, x), (r, g, b))

#         img.save(f"./media/frames/{name}_frame{i}.png")

#         print(f"{i + 1} ", end='', flush=True)