#Here is your solutuion
# Solution 1
def validIPAddress(string):
    ipAddressFound = []

    for idx in range(1, min(len(string), 4)):
        currentIPAddressParts = ['', '', '', '']

        currentIPAddressParts[0] = string[:idx]

        if not isValidPart(currentIPAddressParts[0]):
            continue

        for jdx in range(idx + 1, idx + min(len(string) - idx, 4)):
            currentIPAddressParts[1] = string[idx:jdx]

            if not isValidPart(currentIPAddressParts[1]):
                continue

            for kdx in range(jdx + 1, jdx + min(len(string) - jdx, 4)):
                currentIPAddressParts[2] = string[jdx:kdx]
                currentIPAddressParts[3] = string[kdx:]

                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    ipAddressFound.append('.'.join(currentIPAddressParts))
            
    return ipAddressFound

def isValidPart(string):
    stringAsInt = int(string)

    if stringAsInt > 255:
        return False
    
    # check leading 0
    return len(string) == len(str(stringAsInt))


# Call the function
string = '1921680'
output = validIPAddress(string)
print('👋 Output:', output)
# ['1.9.216.80', '1.92.16.80', '1.92.168.0', '19.2.16.80', '19.2.168.0', '19.21.6.80', '19.21.68.0', '19.216.8.0', '192.1.6.80', '192.1.68.0', '192.16.8.0']