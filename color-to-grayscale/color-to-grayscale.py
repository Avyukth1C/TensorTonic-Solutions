def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    result = []
    for i in range(len(image)):
        row = []
        for j in range(len(image[i])):
            row.append(0.299 * image[i][j][0] + 0.587 * image[i][j][1] + 0.114 * image[i][j][2])
        result.append(row)

    return result
             
