#function to convert decimal to binary and octal and vice-versa

def convert_number(number, frm, to):
    if 'dec' in frm and 'bin' in to:
        return bin(number)[2:] #to remove 0b in string
    elif 'dec' in frm and 'oct' in to:
        return oct(number)[2:]
    elif 'oct' in frm and 'bin' in to:
        return bin(int(number, 8))[2:] #convert first to decimal , then to binary
    elif 'oct' in frm and 'dec' in to:
        return int(number, 8)
    elif 'bin' in frm and 'dec' in to:
        return int(number, 2)
    else:
        return oct(int(number,2))[2:] #convert to decimal and then octal

number = 42
frm="decimal"
to="binary"

print(convert_number(number, frm, to))