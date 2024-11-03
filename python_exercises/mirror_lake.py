"""
File: mirror_lake.py
Name:
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:
    :return:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    b_img = SimpleImage.blank(original_mt.width, original_mt.height * 2)
    for x in range(original_mt.width):
        for y in range(original_mt.height):
            original_mt_p = original_mt.get_pixel(x, y)
            blank_p1 = b_img.get_pixel(x, y)
            blank_p2 = b_img.get_pixel(x, b_img.height - 1 - y)
            blank_p1.red = original_mt_p.red
            blank_p2.red = original_mt_p.red
            blank_p1.green = original_mt_p.green
            blank_p2.green = original_mt_p.green
            blank_p1.blue = original_mt_p.blue
            blank_p2.blue = original_mt_p.blue
    return b_img


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
