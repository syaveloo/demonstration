from os import listdir
from os.path import isfile, join
import cv2 as cv
import os
import subprocess
from PIL import Image
import json


class MainFolder:
    def __init__(self):
        # make main folder
        try:
            os.mkdir(os.getcwd()+'/take_vtf/')
        except Exception:
            pass

class Img512:
    def __init__(self,path):
        # get files
        files = [f for f in listdir(path) if isfile(join(path, f))]
        for image in files:
            # try to read image
            try:
                img = cv.imread(path+image)
            except Exception:
                print(f"Invalid file:{image}")
            
            # convert to png
            dot = -image[::-1].find(".")-1
            image = image.replace(image[dot:],".png")
            
            # resize to 512x512
            img512 = cv.resize(img,(512,512))
            
            # create a 512images folder
            maindir = '/take_vtf/'
            dirname = "/512images/"
            script_dir = os.getcwd()
            try:
                os.mkdir(script_dir+maindir+dirname)
            except Exception:
                pass
            
            # save image
            cv.imwrite(script_dir+maindir+dirname+image,img512)
            print(f"Saved image: {image} in {script_dir+dirname}")

class ImgTGA:
    def __init__(self,path):
        # get files
        files = [f for f in listdir(path) if isfile(join(path, f))]
        for image in files:
            # try to read image
            try:
                img = Image.open(path+image)
            except Exception:
                print(f"Invalid file:{image}")
            # convert to rgb
            rgb_img = img.convert('RGB')
            
            # change format to tga
            dot = -image[::-1].find(".")-1
            image = image.replace(image[dot:],".tga")
            
            # create a tga folder
            maindir = '/take_vtf/'
            dirname = "/TGAimages/"
            script_dir = os.getcwd()
            try:
                os.mkdir(script_dir+maindir+dirname)
            except Exception:
                pass
            # save file
            rgb_img.save(script_dir+maindir+dirname+image)
            print(f"Saved image: {image} in {script_dir+dirname}")

class ImgVTF:
    def __init__(self,path,vtex,gameinfo):
        # get files
        files = [f for f in listdir(path) if isfile(join(path, f))]
        vtex = os.path.normpath(vtex)
        for image in files:
            os.system(f'""{vtex}" -nopause -outdir "{os.getcwd()}\\take_vtf\\VTFimages" -game "{gameinfo}" -quiet "{os.getcwd()}\\take_vtf\\TGAimages\\{image}""')




if __name__=='__main__':
    with open('config.json','r',encoding='utf-8') as config:
        try:
            cfg = eval(config.read())
        except SyntaxError:
            #stopcode 3
            print('StopCode: 3. Slashes in your path must be a "/" or "\\" or "\\\\"!\nFor example: C:\\\\Program Files (x86)\\\\Steam\\steamapps\\\\common\\\\GarrysMod')
            exit()
    path = cfg['images_path']
    vtex = cfg['gmod_path']+'\\bin\\vtex.exe'
    gameinfo = cfg['gmod_path']+"\\garrysmod"
    print(vtex,'\n',gameinfo)

    #stopcode 1
    if not os.path.isdir(path):
        print("StopCode: 1. Invalid path!")
        exit()
    #stopcode 2
    elif path[-1] not in ['/','\\']:
        path += '\\'
    
    # make main folder
    MainFolder()
    
    # make 512x512 images
    Img512(path=path)
    
    # make 512x512 tga images
    ImgTGA(path=os.getcwd()+'/take_vtf/512images/')
    
    # make vtf files
    ImgVTF(path=os.getcwd()+'/take_vtf/TGAimages/',vtex=vtex,gameinfo=gameinfo)