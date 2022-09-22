import shutil
import cv2
import math
from os import listdir
from os.path import isfile, join
import numpy as np


class ImageProps:
    def calc_mean_brightness(self, matrix, type='BGR'):
        if type == 'BGR':
            hsv = cv2.cvtColor(matrix, cv2.COLOR_BGR2HSV)
            return hsv[:,:,2].mean()
        elif type == 'HSV' or type == 'HSL':
            return matrix[:,:,2].mean()
        
    def show_img(self, BGR_matrix):
        cv2.imshow('image',BGR_matrix)
        cv2.waitKey(0)


class ImageAdjust(ImageProps):
    def adjust_brightness(self, val_0_to_255, BGR_matrix):
        hsv = cv2.cvtColor(BGR_matrix, cv2.COLOR_BGR2HSV)
        mean = math.floor(self.calc_mean_brightness(hsv,'HSV'))
        itr = 0
        # while ((mean > val_0_to_255 + 5) or (mean < val_0_to_255 -5)) and itr<10:
        while mean != val_0_to_255 and itr<10:
            adjustment = int(val_0_to_255 - mean)
            
            h,s,v = cv2.split(hsv)
            if adjustment > 0:
                v = np.where(v + adjustment <= 255 , v + adjustment, 255).astype('uint8')
            else:
                v = np.where(v + adjustment >= 0 , v + adjustment, 0).astype('uint8')

            hsv = cv2.merge((h,s,v))
            mean = math.floor(self.calc_mean_brightness(hsv,'HSV'))
            itr += 1

        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    def export(self, BGR_matrix, path):
        cv2.imwrite(path, BGR_matrix)


class BulkImageAdjust(ImageAdjust):
    def __init__(self, path_to_img_dir):
        self.dir_path = path_to_img_dir
        self._load_imgs()

    def _get_file_names(self):
        # only include files, not subdirectories
        return [f for f in listdir(self.dir_path) if isfile(join(self.dir_path, f))]

    def _load_imgs(self):
        self.filenames = self._get_file_names()
        self.imgs = []
        for filename in self.filenames:
            self.imgs.append(cv2.imread(join(self.dir_path, filename)))
    
    def change_brightness_to(self, val_0_to_255):
        for i,img in enumerate(self.imgs):
            try:
                self.imgs[i] = self.adjust_brightness(val_0_to_255,img)
            except Exception as err:
                print(f'An error occured with file at position {i}')
                print(err)
                
    def show_head(self, head_size):
        for i in range(head_size):
            self.show_img(self.imgs[i])

    def export_all(self, path_to_dir):
        for i, img in enumerate(self.imgs):
            self.export(img, join(path_to_dir,self.filenames[i]))

dir_path = './hology_images'

def search_dir(dir_path):
    for f in listdir(dir_path):
        if isfile(join(dir_path,f)):
            shutil.copy(join(dir_path,f),'./imgs/')
        else:
            search_dir(join(dir_path,f))

# search_dir(dir_path)

bulkImgs = BulkImageAdjust('./imgs/in')

bulkImgs.change_brightness_to(20)
# bulkImgs.show_head(10)
bulkImgs.export_all('./imgs/out')

        

