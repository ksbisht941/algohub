"use strict";
exports.__esModule = true;
exports.phoneNumberMnemonics = void 0;
function phoneNumberMnemonics(phoneNumber) {
    var mnemonicsFound = [];
    var currentMnemonics = new Array(phoneNumber.length).fill("0");
    phoneNumberMnemonicsHelper(0, phoneNumber, currentMnemonics, mnemonicsFound);
    return mnemonicsFound;
}
exports.phoneNumberMnemonics = phoneNumberMnemonics;
function phoneNumberMnemonicsHelper(idx, phoneNumber, currentMnemonics, result) {
    if (idx == phoneNumber.length) {
        var mnemonic = currentMnemonics.join("");
        result.push(mnemonic);
    }
    else {
        var digit = phoneNumber[idx];
        var letters = DIGIT_LETTERS[digit];
        for (var _i = 0, letters_1 = letters; _i < letters_1.length; _i++) {
            var letter = letters_1[_i];
            currentMnemonics[idx] = letter;
            phoneNumberMnemonicsHelper(idx + 1, phoneNumber, currentMnemonics, result);
        }
    }
}
var DIGIT_LETTERS = {
    "1": ["1"],
    "2": ['a', 'b', 'c'],
    "3": ['d', 'e', 'f'],
    "4": ['g', 'h', 'i'],
    "5": ['j', 'k', 'l'],
    "6": ['m', 'n', 'o'],
    "7": ['p', 'q', 'r', 's'],
    "8": ['t', 'u', 'v'],
    "9": ['w', 'x', 'y', 'z'],
    "0": ["0"]
};
var phoneNumber = "1905";
var output = phoneNumberMnemonics(phoneNumber);
console.log("👋 Output:", output);
