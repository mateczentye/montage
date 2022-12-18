import numpy as np


def format_check(
    file: str,
    supported_list: list = ['.jpeg', '.jpg', '.png', '.tiff', '.gif']    
):
    """Function to check if the file is a supported format."""
    check = None
    for ext in supported_list:        
        if ext in file:
            return True
        else:
            check = False

    if check is False:
        return False


def loop_check(
    name_array: list
):
    """Function loops through the list of given strings
    and filters out all the ones that are not supported
    by replacing them with blank space on the mosaic"""
    new_array = []
    shape = np.shape(name_array)
    for pic in np.asarray(name_array).flatten():
        if format_check(pic):
            new_array.append(pic)
        else:
            new_array.append('.')

    return np.asarray(new_array).reshape(shape)