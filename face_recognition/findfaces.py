import face_recognition
from PIL import Image

image = face_recognition.load_image_file('./images/groups/bill-steve.jpg')
face_locations = face_recognition.face_locations(image)

#array of coords of each face
for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    # pil_image.show()
    pil_image.save(f'{top}.jpg')
