def decode(encode)
    new_password = ''
    for number in encode:
        if number == '2':
            new_password += '9'
        if number == '1':
            new_password += '8'
        if number == '0':
            new_password += '7'
        else:
            new_password += str(int(number)-3)
    return new_password