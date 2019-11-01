def hex2bin(hex_val, num_bits):  # Returns binary string of num_bits length of hex value (pos or neg)

    bit_string = '0' * num_bits
    bin_val = str(bin(int(str(hex_val), 16)))[2:]
    bit_string = bit_string[0: num_bits - len(bin_val)] + bin_val
    return bit_string


'''



# Adjust for negative by performing Two's Complement (tc)  written above the code 
    tc = False
    if '-' in hex_val:
        tc = True
        hex_val = hex_val.replace('-', '')
 # Two's complement if negative hex value  written under the code 
 if tc:
     tsubstring = bit_string[0:bit_string.rfind('1')]
     rsubstring = bit_string[bit_string.rfind('1'):]
     tsubstring = tsubstring.replace('1', 'X')
     tsubstring = tsubstring.replace('0', '1')
     tsubstring = tsubstring.replace('X', '0')
     bit_string = tsubstring + rsubstring

 return bit_stringng[num_bits-1:])
'''
