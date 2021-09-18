"use strict";
exports.__esModule = true;
exports.validIPAddresses = void 0;
function validIPAddresses(string) {
    var ipAddressesFound = [];
    for (var idx = 0; idx < Math.min(string.length, 4); idx++) {
        var currentIPAddressParts = ['', '', '', ''];
        currentIPAddressParts[0] = string.slice(0, idx);
        if (!(isValidPart(currentIPAddressParts[0])))
            continue;
        for (var jdx = idx + 1; jdx < idx + Math.min(string.length - idx, 4); jdx++) {
            currentIPAddressParts[1] = string.slice(idx, jdx);
            if (!(isValidPart(currentIPAddressParts[1])))
                continue;
            for (var kdx = jdx + 1; kdx < jdx + Math.min(string.length - jdx, 4); kdx++) {
                currentIPAddressParts[2] = string.slice(jdx, kdx);
                currentIPAddressParts[3] = string.slice(kdx);
                if (isValidPart(currentIPAddressParts[2]) &&
                    isValidPart(currentIPAddressParts[3])) {
                    ipAddressesFound.push(currentIPAddressParts.join("."));
                }
            }
        }
    }
    return ipAddressesFound;
}
exports.validIPAddresses = validIPAddresses;
function isValidPart(string) {
    var stringAsInt = parseInt(string);
    if (stringAsInt > 255) {
        return false;
    }
    return string.length === stringAsInt.toString().length;
}
//   Call the function
var string = '1921680';
var output = validIPAddresses(string);
console.log('👋 Output:', output);
// ['1.9.216.80', '1.92.16.80', '1.92.168.0', '19.2.16.80', '19.2.168.0', '19.21.6.80', '19.21.68.0', '19.216.8.0', '192.1.6.80', '192.1.68.0', '192.16.8.0']
