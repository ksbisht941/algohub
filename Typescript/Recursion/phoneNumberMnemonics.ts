export function phoneNumberMnemonics(phoneNumber: string): string[] {
    const mnemonicsFound: string[] = []
    const currentMnemonics: string[] =  new Array(phoneNumber.length).fill("0");
    phoneNumberMnemonicsHelper(0, phoneNumber, currentMnemonics, mnemonicsFound)
    return mnemonicsFound;
}

function phoneNumberMnemonicsHelper(idx: number, phoneNumber: string, currentMnemonics: string[], result: string[]) {
    if (idx == phoneNumber.length) {
        const mnemonic = currentMnemonics.join("");
        result.push(mnemonic);
    } else {
        const digit = phoneNumber[idx];
        const letters = DIGIT_LETTERS[digit];
        for (const letter of letters) {
            currentMnemonics[idx] = letter;
            phoneNumberMnemonicsHelper(idx + 1, phoneNumber, currentMnemonics, result)
        }
    }
}

const DIGIT_LETTERS: {[digit: string]: string[]} = {
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
}


const phoneNumber = "1905"
const output = phoneNumberMnemonics(phoneNumber)
console.log("👋 Output:", output)