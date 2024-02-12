import face_recognition
from PIL import Image,ImageDraw

image = face_recognition.load_image_file('./images/groups/bill-steve.jpg')
bill_face_encoding = face_recognition.face_encodings(image)[0]

image2 = face_recognition.load_image_file('./images/known/Steve Jobs.jpg')
steve_face_encoding = face_recognition.face_encodings(image2)[0]

known_face_encodings = [
    bill_face_encoding,
    steve_face_encoding
]

known_face_names = [
    "bill gates",
    "steve jobs"
]

test_image = face_recognition.load_image_file("./images/groups/bill-steve.jpg")

# find faces in test images
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image,face_locations)

# conver to pil format
pil_images = Image.fromarray(test_image)

# draw
draw = ImageDraw.Draw(pil_images)

#loop through faces in test data
for(top,right, bottom, left), face_encoding in zip(face_locations,face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings,face_encoding)

    name = "Unknown person"

    #if match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # draw the box
    draw.rectangle((left, top, right, bottom), outline=(0, 0, 0))

    #draw label
    bbox = draw.textbbox((left, bottom - 5), name)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]



    draw.rectangle((left, bottom - text_height - 10, right, bottom), fill=(0, 0, 0), outline=(0, 0, 0))
    draw.text((left+6,bottom-text_height-5),name, fill=(255,255,255,255))

del draw
pil_images.show()
pil_images.save("identify.jpg")
