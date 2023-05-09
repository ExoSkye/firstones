import sys
conversion = {
    # Consonants
    "b": "b",
    "ʧ": "ch",
    "d": "d",
    "dˈh": "dh",
    "f": "f",
    "g": "g",
    "h": "h",
    "ʤ": "j",
    "k": "k",
    "l": "l",
    "m": "m",
    "n": "n",
    "ŋ": "ng",
    "p": "p",
    "ɑː": "r",
    "s": "s",
    "ʃ": "sh",
    "t": "t",
    "ð": "th",
    "v": "v",
    "w": "w",
    "z": "z",
    "ʒ": "zh",
    # Vowels
    "æ": "sad",
    "ɔː": "all",
    "eɪ": "say",
    "ɛ": "pet",
    "iː": "feet",
    "ɪ": "lit",
    "aɪ": "i",
    "ʊ": "good",
    "uː": "too",
    "əʊ": "go",
    "aʊ": "house",
    "ʌ": "fun",
    "ɔɪ": "boy",
    "j": "yes",
    # Fixes
    "ə": "sad"
}

ipa = input("Please enter your IPA string:").strip().split(" ")

for word in ipa:
    start = 0
    while start != len(word):
        symbol = "a"
        end = len(word)
        while end != 0:
            if word[start:end] in conversion.keys():
                symbol = word[start:end]
                print(conversion[word[start:end]], end=" ")
                break
            end -= 1
        start += len(symbol)

    print("")
