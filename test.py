from imutils import paths
import face_recognition
import pickle
import cv2
import os

# get paths of each file in folder named Images
# Images here contains my data(folders of various persons)
#imagePaths = list(paths.list_images('Imagess/'))
imagePaths = list(paths.list_images("Images"))
print(imagePaths)

knownNames = []
RollNumber = []
for (i, imagePath) in enumerate(imagePaths):
    # extract the person name from the image path
    ex = imagePath.split(os.path.sep)[-1]
    name = ex.split(".")[0]
    rn = ex.split(".")[1]
    knownNames.append(name)
    RollNumber.append(rn)
print(knownNames)
print(RollNumber)

name = "Ali Panjwani"
index = RollNumber[knownNames.index(name)]
print(index)