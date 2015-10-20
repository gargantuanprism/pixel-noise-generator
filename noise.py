#!/usr/bin/env python2

import argparse
import random
import time

from PIL import Image, ImageDraw

def random_rgb():
    """
    Generates a random RGB tuple.

    Returns:
        tuple: random RGB tuple
    """

    return (
            random.randrange(255),
            random.randrange(255),
            random.randrange(255),
            )

def block_random(image, block_size):
    """
    Fills in an image with rectangles of block size, randomly filled.

    Args:
        image: PIL Image object
        block_size: size of rect in pixels
    """

    d = ImageDraw.Draw(image)

    x_blocks = image.size[0] / block_size
    y_blocks = image.size[1] / block_size
    pos = [0, 0]

    for xb in range(x_blocks):
        for yb in range(y_blocks):
            d.rectangle(
                    [pos[0], pos[1], pos[0] + block_size, pos[1] + block_size],
                    fill=random_rgb()
                    )

            pos[0] += block_size

        pos[0] = 0
        pos[1] += block_size

def full_random(image):
    """
    Draws a random color on each pixel of an image.

    Args:
        image: PIL Image object
    """

    d = ImageDraw.Draw(image)

    for x in range(args.x):
        for y in range(args.y):
            d.point((x, y), random_rgb())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('x', type=int)
    parser.add_argument('y', type=int)
    parser.add_argument('--block-size', type=int)

    args = parser.parse_args()

    image = Image.new('RGB', (args.x, args.y))

    if args.block_size is None:
        full_random(image)
    else:
        block_random(image, args.block_size)

    filename = 'noise-%d.png' % int(time.time())

    # Save image with timestamp and print filename
    image.save(filename)
    print filename


