'''
Library of useful functions for working with images.
'''
import requests 
import ctypes

def main():
    image_data = download_image('https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jepg')
    result = save_image_file(image_data, r'C\temp\kitty.jpg')
    return

def download_image(image_url):
    """Downloads an image from a specified URL.

    DOES NOT SAVE THE IMAGE FILE TO DISK.

    Args:
        image_url (str): URL of image

    Returns:
        bytes: Binary image data, if successful. None, if unsuccessful.
    """
     