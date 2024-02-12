import string
import random

if __name__ == "__main__":
    #strings
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    #list
    combine = []
    combine.extend(list(s1))
    combine.extend(list(s2))
    combine.extend(list(s3))
    combine.extend(list(s4))

    #randomizing
    random.shuffle(combine)

    #input
    length = int(input("Enter Length of passowrd :"))
    password = "".join(combine[:length]) #method1
    password2 = "".join(random.sample(combine,length))#method2
    print(password2)