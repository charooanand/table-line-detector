import cv2
import matplotlib.pyplot as plt
import numpy as np
import statistics

def v_count_pix(image): # input image is b&w and inverted

  v_pix_counts = []

  for x in range(len(image[0])):
    pix_count = 0

    for y in range(len(image)):
      pix_count += image[y][x]

    v_pix_counts.append(pix_count)

  return(v_pix_counts)

def group_list(lst):
    lst.sort()

    diff = [y - x for x, y in zip(*[iter(lst)] * 2)]
    avg = sum(diff) / len(diff)

    grouped_lst = [[lst[0]]]

    for x in lst[1:]:
        if x - grouped_lst[-1][0] < avg:
            grouped_lst[-1].append(x)
        else:
            grouped_lst.append([x])

    return (grouped_lst)

def vline_detector(image):
    # binarize and invert image
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    img_bin = 255 - img_bin

    # use kernel to detect vertical lines
    kernel_len = np.array(img).shape[1] // 100
    ver_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_len))
    vlines = cv2.dilate(cv2.erode(img_bin, ver_kernel, iterations=10), ver_kernel, iterations=10)

    # collapse pixel count vertically
    v_pix_counts = v_count_pix(vlines)

    # create plot
    plot = plt.plot(range(len(v_pix_counts)),
                    v_pix_counts,
                    color='black')

    plt.xlabel("width of image (pixels)")
    plt.ylabel("pixels counted in a detected line")

    # find center of spikes in pixel count
    non_zero = [index for index in range(len(v_pix_counts)) if v_pix_counts[index] > 0]
    coords = list(map(lambda x: statistics.mean(x), group_list(non_zero)))

    return (coords, plot)


def hline_detector(image):

    image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    coords, plot = vline_detector(image)
    plt.xlabel("height of image (pixels)")

    return([coords, plot])
