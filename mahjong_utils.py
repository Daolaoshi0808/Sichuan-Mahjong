import cv2
import numpy as np

def recognize_tiles(file, peng=0):
    images = []

    for i in range(1, 28):
        if i <= 9:
            filename = f'13promax_char_{i}.png'
        elif 10 <= i <= 18:
            j = i - 9
            filename = f'13promax_bamboo_{j}.png'
        else:
            j = i - 18
            filename = f'13promax_dot_{j}.png'
        
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        images.append(image[2:193, :])
    
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    height, width = image.shape[:2]

    start_x = int((390 + peng * 82) * width / 2778)
    start_y = int(44 * height / 1284)

    tile_width = int(141 * width / 2778)
    tile_height = int(186 * height / 1284)

    number_of_tiles = 13 - 3 * peng

    tiles = []

    for i in range(number_of_tiles):
        top_left_x = start_x + (i * tile_width)
        top_left_y = start_y + tile_height

        tile = image[height - tile_height - start_y:height - start_y, top_left_x:top_left_x + tile_width]
        tiles.append(tile)

    top_left_x = top_left_x + tile_width + int(36 * height / 1284)
    tile = image[height - tile_height - start_y:height - start_y, top_left_x:top_left_x + tile_width]
    tiles.append(tile)

    tiles_nocolor = []

    for i in range(len(tiles)):
        gray = cv2.cvtColor(tiles[i], cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 1)
        median = cv2.medianBlur(blurred, 3)
        edges = cv2.Canny(median, 300, 350)
        _, binary = cv2.threshold(edges, 200, 255, cv2.THRESH_BINARY)
        kernel = np.ones((3, 3), np.uint8)
        dilation = cv2.dilate(binary, kernel)
        tiles_nocolor.append(dilation)

    tiles = []

    for i in range(len(tiles_nocolor)):
        temp_image = tiles_nocolor[i][:, 11:139]
        vals = []

        for j in range(len(images)):
            image_template = images[j][7:193:, 11:139]
            result = cv2.matchTemplate(temp_image, image_template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            vals.append(max_val)

        tiles.append(np.argmax(vals))

    tiles_to_char = {
        0: "char_1",
        1: "char_2",
        2: "char_3",
        3: "char_4",
        4: "char_5",
        5: "char_6",
        6: "char_7",
        7: "char_8",
        8: "char_9",
        9: "bamboo_1",
        10: "bamboo_2",
        11: "bamboo_3",
        12: "bamboo_4",
        13: "bamboo_5",
        14: "bamboo_6",
        15: "bamboo_7",
        16: "bamboo_8",
        17: "bamboo_9",
        18: "dot_1",
        19: "dot_2",
        20: "dot_3",
        21: "dot_4",
        22: "dot_5",
        23: "dot_6",
        24: "dot_7",
        25: "dot_8",
        26: "dot_9",
    }

    converted_list = [tiles_to_char[item] for item in tiles if item in tiles_to_char]

    return converted_list
