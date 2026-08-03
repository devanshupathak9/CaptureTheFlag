import base64

def decode_string(miwen):
    rot_13 =""
    for ch in miwen:
        if ch.isalpha():
            val = ord(ch)
            if val >=65 and val<=90:
                if val - 13 >=65:
                    rot_13 += chr(val-13)
                else:
                    rot_13 += chr(90 - (12-(val-65)))
            elif val >=97 and val<=122:
                if val - 13 >=97:
                    rot_13 += chr(val-13)
                else:
                    rot_13 += chr(122 - (12-(val-97)))
        else:
            rot_13 += ch
    revstr = rot_13[::-1]
    fstr = base64.b64decode(revstr).decode()
    flag = ""
    for ch in fstr:
        flag += chr(ord(ch) - 1)
    return flag[::-1]

print(decode_string("a1zLbgQsCESEIqRLwuQAyMwLyq2L5VwBxqGA3RQAyumZ0tmMvSGM2ZwB4tws"))