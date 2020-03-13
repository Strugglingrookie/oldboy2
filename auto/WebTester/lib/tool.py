import os
from lib.path import WEBPICTUREPATH


class Tool(object):
    def __init__(self):
        self.filelist = os.listdir(WEBPICTUREPATH)

    def error_picture(self):
        picture = []
        for item in self.filelist:
            if item.endswith('.jpg'):
                picture.append((item,))
        return picture

    def clear_picture(self):
        list(map(os.remove, map(lambda file: WEBPICTUREPATH + file, self.filelist)))
