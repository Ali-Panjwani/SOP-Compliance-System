from imutils import paths
import face_recognition
import pickle
import cv2
import os
import smtplib, ssl

# get paths of each file in folder named Images
# Images here contains my data(folders of various persons)
imagePaths = list(paths.list_images('Images'))

knownEncodings = []
knownNames = []
rollNumber = []

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    # extract the person name from the image path
    ex = imagePath.split(os.path.sep)[-1]
    name = ex.split(".")[0]
    rn = ex.split(".")[1]
    # load the input image and convert it from BGR (OpenCV ordering)
    # to dlib ordering (RGB)
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Use Face_recognition to locate faces
    boxes = face_recognition.face_locations(rgb, model='hog')
    # compute the facial embedding for the face
    encodings = face_recognition.face_encodings(rgb, boxes)
    # loop over the encodings
    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)
        rollNumber.append(rn)
# save encodings along with their names in dictionary data
data = {"encodings": knownEncodings, "names": knownNames}
# use pickle to save data into a file for later use
f = open("face_enc", "wb")
f.write(pickle.dumps(data))
f.close()

# find path of xml file containing haarcascade file
cascPathface = "haarcascade_frontalface_default.xml"
# load the harcaascade in the cascade classifier
faceCascade = cv2.CascadeClassifier(cascPathface)
# load the known faces and embeddings saved in last file
data = pickle.loads(open('face_enc', "rb").read())

print("Streaming started")
video_capture = cv2.VideoCapture(0)
# loop over frames from the video file stream
count = 0
while True:
    # grab the frame from the threaded video stream
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(60, 60),
                                         flags=cv2.CASCADE_SCALE_IMAGE)

    # convert the input frame from BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # the facial embeddings for face in input
    encodings = face_recognition.face_encodings(rgb)
    names = []
    # loop over the facial embeddings incase
    # we have multiple embeddings for multiple faces
    for encoding in encodings:
        # Compare encodings with encodings in data["encodings"]
        # Matches contain array with boolean values and True for the embeddings it matches closely
        # and False for rest
        matches = face_recognition.compare_faces(data["encodings"],
                                                 encoding)
        # set name =inknown if no encoding matches
        name = "Unknown"
        # check to see if we have found a match
        if True in matches:
            # Find positions at which we get True and store them
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                # Check the names at respective indexes we stored in matchedIdxs
                name = data["names"][i]
                # increase count for the name we got
                counts[name] = counts.get(name, 0) + 1
            # set name which has highest count
            name = max(counts, key=counts.get)

        # update the list of names
        names.append(name)
        # loop over the recognized faces
        for ((x, y, w, h), name) in zip(faces, names):
            # rescale the face coordinates
            # draw the predicted face name on the image
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.75, (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    count = count + 1
    print(count)
    if cv2.waitKey(1) & 0xFF == ord('q') or count == 20:
        video_capture.release()
        cv2.destroyAllWindows()
        break

if name == "Unknown" :
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "" #Email which will be used to mail the Administartion
    receiver_email = "" #Administration's Email
    password = "" #Password of sender_email
    message = "A Unknown person in your surrounding is not wearing a mask"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

else:
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "" #Email which will be used to mail the Administartion
    receiver_email = "" #Administration's Email
    password = "" #Password of sender_email
    message = name + " ,Roll Number " + rollNumber[knownNames.index(name)] + ", is not wearing a mask"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


    sender_email = "" #Email which will be used to mail the Administartion
    receiver_email = rollNumber[knownNames.index(name)] + '@nu.edu.pk' #SOP violator's email
    password = "" #Password of sender_email
    message = "You're requested to please wear a mask"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

exec(open('Final.py').read())
