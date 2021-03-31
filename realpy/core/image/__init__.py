""" Image Resource
    ---
    ```
    from realpy import RsImage
    ```
"""
from typing import List, Tuple, Union

__all__ = ["RsImage"]


class RsImage(object):
    """`RsImage(image_path)`
        ---
        Raw image of a sprite that contains single or multiple images.
    """

    def __init__(self, filepath: Union[str, Tuple[str], List[str]]):
        import os
        import pygame.image as PyImage
        import pygame.rect as PyRect

        self.number: int = -1
        self.raw_data = []
        self.boundbox = PyRect.Rect(0, 0, 0, 0)

        if isinstance(filepath, str):
            filepath = (filepath,)

        self.number = len(filepath)
        FileLoc: str
        for FileLoc in filepath:
            self.raw_data.append(PyImage.load(FileLoc).convert_alpha())
        self.filename = os.path.basename(filepath[0])
        self.boundbox = self.raw_data[0].get_rect()
