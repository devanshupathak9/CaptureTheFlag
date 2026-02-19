## decrypt flag
def decrypt(encrypted_flag):
    c = ''
    for i in range(len(encrypted_flag)):
        ch = encrypted_flag[i]
        if not ch.isalpha():
            ech = ch
        else:
            ech = 'x'
        c += ech
    return c

with open('output.txt', 'r') as f:
    data = f.read()
    print(decrypt(data.split("\n")[1]))


