interface CharacterFrequencies {
    [character: string]: number;
}

// O(n * l) time | O(c) space - where n is the number of words,
// l is the length of the longest word, and c is the number of
// unique characters across all words
export function minimumCharactersForWords(words: string[]) {
    const maximumCharctersFrequency: CharacterFrequencies = {};

    for (const word of words) {
        const characterFrequency = countCharacterFrequency(word);
        updateMaximumFrequency(characterFrequency, maximumCharctersFrequency);
    }

    return makeArrayFromMaximumFrequency(maximumCharctersFrequency)
}

export function countCharacterFrequency(word: string) {
    const frequency = {};

    for (const character of word) {
        if (!(character in frequency)) {
            frequency[character] = 0
        }

        frequency[character] += 1
    }

    return frequency;
}

export function updateMaximumFrequency(characterFrequency: CharacterFrequencies, maximumCharctersFrequency: CharacterFrequencies) {
    for (const character in characterFrequency) {
        const frequency = characterFrequency[character];

        if (character in maximumCharctersFrequency) {
            maximumCharctersFrequency[character] = Math.max(frequency, maximumCharctersFrequency[character]);
        }
        else {
            maximumCharctersFrequency[character] = frequency;
        }
    }
}

export function makeArrayFromMaximumFrequency(maximumCharctersFrequency: CharacterFrequencies) {
    const characters: string[] = [];

    for (const character in maximumCharctersFrequency) {
       const frequency = maximumCharctersFrequency[character];

       for (let idx = 0; idx < frequency; idx++) {
           characters.push(character);
       }
    }

    return characters;
}

const words = ["this", "that", "did", "deed", "them!", "a"]
const output = minimumCharactersForWords(words)
console.log("👋 Output", output)
// 👋 Output ['t', 't', 'h', 'i', 's', 'a', 'd', 'd', 'e', 'e', 'm', '!']