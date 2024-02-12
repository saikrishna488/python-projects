import face_recognition

image = face_recognition.load_image_file('./images/known/Bill Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image)[0]

image2 = face_recognition.load_image_file('./images/unknown/mark.jpg')
image2_face_encoding = face_recognition.face_encodings(image2)[0]

result = face_recognition.compare_faces([bill_face_encoding],image2_face_encoding)

if result[0]:
    print("faces matched")
else:
    print("faces not matched")