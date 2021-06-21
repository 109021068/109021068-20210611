import sys
from PIL import Image, ImageFilter

def resizeImg (imgName) :
    try:
        img = Image.open (imgName)
        print ("Current size (width, height)", img.size)
        newWidth = int (input ("new width: "))
        ratio = float (newWidth) /img.size [0]
        newHeight = int (img.size [1] * ratio)
        resizedImg = img.resize( (newWidth, newHeight), Image.BILINEAR )
        print ("new image size: ", resizedImg.size)
        dotIndex = imgName.index (".")
        newImgName = imgName [:dotIndex] + "_resized" + imgName [dotIndex:]
        resizedImg.save (newImgName) 
        print("Resized img is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print (fnfe)

def rotateImg (imgName) :
    try:
        img = Image.open (imgName)
        print("選擇選項: ")
        print ("1. 左右翻轉")
        print ("2. 上下翻轉")
        print ("3. 旋轉 90 度")
        print ("4. 旋轉 180 度")
        print ("5. 旋轉 270 度")
        opl = input("您要進行的操作: ")
        if opl == "1":
            newIm = img.transpose (Image.FLIP_LEFT_RIGHT)
            strl = "_flip_LR"
        elif opl == "2":
            newIm = img.transpose (Image.FLIP_TOP_BOTTOM)
            strl = "_flip_TB"
        elif opl == "3":
            newIm = img.transpose (Image.ROTATE_90)
            strl = "rotate_90"
        elif opl == "4":
            newIm = img.transpose (Image.ROTATE_180)
            strl = "_rotate_180"
        elif opl == "5":
            newIm = img.transpose (Image.ROTATE_270)
            strl = "_rotate_270"
        elif opl == "6":
            rotDegree = float (input ("Rotate degree: "))
            newIm = img.rotate(rotDegree)
            strl = "_rotate_" + str(rotDegree)
        dotIndex = imgName.index (".")
        newImgName = imgName [:dotIndex] + "_rotate" + imgName [dotIndex:]
        newIm.save (newImgName) 
        print("Rotated image is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print (fnfe)

def genThumbnail (imgName) :
    try:
        img = Image.open (imgName)
        print ("Current size (width, height)", img.size)
        newWidth, newHeight = map (int, input ("請輸入縮圖尺寸: ").split())
        img.thumbnail ((newWidth, newHeight))
        dotIndex = imgName.index (".")
        newImgName = imgName [:dotIndex] + "_thumbnail" + imgName [dotIndex:]
        img.save (newImgName) 
        print("Thumbnail image is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print (fnfe)

def applyFilter (imgName) :
    try:
        im = Image.open (imgName)
        print("濾鏡選項: ")
        print ("1. 模糊 (BLUR)")
        print ("2. 輪廓 (CONTOUR)")
        print ("3. 細節增強 (DETAIL)")
        print ("4. 邊緣增強 (EDGE ENHANCE) ") 
        print ("5. 深度邊緣增強 (EDGE ENHANCE_MORE)") 
        print ("6. 浮雕效果 (EMBOSS)")
        print ("7. 邊緣訊息 (FIND_EDGES")
        print ("8. 平滑效果 (SMOOTH")
        print ("9. 深度平滑效果 (SMOOTH_MORE")
        print ("A. 銳利化效果 (SHARPEN)")
        opl=input("選擇要套用的濾鏡: ")
        if opl == "1":
            newImg = im.filter (ImageFilter.BLUR)
            strl = "_BLUR"
        elif opl == "2":
            newImg = im.filter (ImageFilter.CONTOUR)
            strl = "_CONTOUR"
        elif opl == "3":
            newImg = im.filter (ImageFilter. DETAIL)
            strl = "_ DETAIL"
        elif opl == "4":
            newImg = im.filter (ImageFilter.EDGE_ENHANCE)
            strl = "_EDGE_ENHANCE"
        elif opl == "5":
            newImg = im.filter (ImageFilter.EDGE_ENHANCE_MORE)
            strl = "EDGE_ENHANCE_MORE"
        elif opl == "6":
            newImg = im. filter (ImageFilter.EMBOSS)
            strl = "_EMBOSS"
        elif opl == "7":
            newImg = im.filter (ImageFilter. FIND_EDGES)
            strl = "_FIND_EDGES"
        elif opl == "8":
            newImg = im.filter (ImageFilter.SMOOTH)
            strl = "_SMOOTH"
        elif opl == "9":
            newImg = im.filter (ImageFilter.SMOOTH_MORE)
            strl="_SMOOTH_MORE"
        elif opl == "A":
            newImg = im.filter (ImageFilter.SHARPEN)
            strl = "_SHARPEN"
        dotIndex = imgName.index (".")
        newImgName = imgName [:dotIndex] + strl + imgName [dotIndex:]
        newImg.save (newImgName) 
        print("Filter image is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print (fnfe)


def showMenu () :
    print("============================")
    print("1: 等比例縮放")
    print("2: 圖片旋轉")
    print("3: 產生縮圖")
    print("4: 套用濾鏡")
    print("0: 結束")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        showMenu()
        op = input ("選擇功能: ")
        if op == "1":
            resizeImg(sys.argv[1])
        if op == "2":
            rotateImg(sys.argv[1])
        if op == "3":
            genThumbnail(sys.argv[1])
        if op == "4":
            applyFilter(sys.argv[1])
    else:
        print ("argument error")