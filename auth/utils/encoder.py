

payloads = "qwertyuiopasdfghjklñzxcvbnm 0123456789.QWERTYUIOPZXCVBNMLKJHGFDSA-"
key = "01m2n3b4v5c6x7z8a9sdf.ghjklñpoiuytr ewqASDFGHJKLÑPOIUYTREWQMNBV-CXZ"


def decode(messege:str) -> (str):
    
    messegeDecode = ''

    for char in messege[::-1]:
        messegeDecode += payloads[key.find(char)]

    return messegeDecode


def encode(messege:str) -> (str):
    messege = messege[::-1]
    encodeMessege = ''

    for char in messege:
        encodeMessege += key[payloads.find(char)]


    return encodeMessege



