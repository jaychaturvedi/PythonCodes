from PIL import Image
import os

def get_h_repeat(im, column):
    dst = Image.new('RGB', (im.width * column, im.height))
    for x in range(column):
        dst.paste(im, (x * im.width, 0))
    return dst

def get_v_repeat(im, row):
    dst = Image.new('RGB', (im.width, im.height * row))
    for y in range(row):
        dst.paste(im, (0, y * im.height))
    return dst

def get_tile_image(im, row, column):
    dst_h = get_h_repeat(im, column)
    return get_v_repeat(dst_h, row)

filename = input("enter image file path : ")
im1 = Image.open(filename)
savedir = input("enter folder path or name : ")
column = int(input("number of column tiles : "))
row = int(input("number of row tiles : "))
save_to = os.path.join(savedir,"result.jpg")
im_s = im1.resize((im1.width // 2, im1.height // 2))
get_tile_image(im_s, row, column).save(save_to)
