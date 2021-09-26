"use strict";
exports.__esModule = true;
exports.makeArrayFromMaximumFrequency = exports.updateMaximumFrequency = exports.countCharacterFrequency = exports.minimumCharactersForWords = void 0;
// O(n * l) time | O(c) space - where n is the number of words,
// l is the length of the longest word, and c is the number of
// unique characters across all words
function minimumCharactersForWords(words) {
    var maximumCharctersFrequency = {};
    for (var _i = 0, words_1 = words; _i < words_1.length; _i++) {
        var word = words_1[_i];
        var characterFrequency = countCharacterFrequency(word);
        updateMaximumFrequency(characterFrequency, maximumCharctersFrequency);
    }
    return makeArrayFromMaximumFrequency(maximumCharctersFrequency);
}
exports.minimumCharactersForWords = minimumCharactersForWords;
function countCharacterFrequency(word) {
    var frequency = {};
    for (var _i = 0, word_1 = word; _i < word_1.length; _i++) {
        var character = word_1[_i];
        if (!(character in frequency)) {
            frequency[character] = 0;
        }
        frequency[character] += 1;
    }
    return frequency;
}
exports.countCharacterFrequency = countCharacterFrequency;
function updateMaximumFrequency(characterFrequency, maximumCharctersFrequency) {
    for (var character in characterFrequency) {
        var frequency = characterFrequency[character];
        if (character in maximumCharctersFrequency) {
            maximumCharctersFrequency[character] = Math.max(frequency, maximumCharctersFrequency[character]);
        }
        else {
            maximumCharctersFrequency[character] = frequency;
        }
    }
}
exports.updateMaximumFrequency = updateMaximumFrequency;
function makeArrayFromMaximumFrequency(maximumCharctersFrequency) {
    var characters = [];
    for (var character in maximumCharctersFrequency) {
        var frequency = maximumCharctersFrequency[character];
        for (var idx = 0; idx < frequency; idx++) {
            characters.push(character);
        }
    }
    return characters;
}
exports.makeArrayFromMaximumFrequency = makeArrayFromMaximumFrequency;
var words = ["this", "that", "did", "deed", "them!", "a"];
var output = minimumCharactersForWords(words);
console.log("👋 Output", output);
// 👋 Output ['t', 't', 'h', 'i', 's', 'a', 'd', 'd', 'e', 'e', 'm', '!']
