import itertools


def is_passphrase(line):
    words = line.split(" ")
    s_words = set(words)
    return len(words) == len(s_words)


def chk_passphrases(file):
    count = 0
    with open(file, 'r') as f:
        for line in f:
            if is_passphrase(line.strip()):
                count += 1
    return count


def is_not_anagram(line):
    words = line.split(" ")

    for p in range(len(words)):
        rev_p = words[p][::-1]
        for pp in range(p + 1, len(words)):
            if rev_p in set(map(lambda s: "".join(s), list(itertools.permutations(words[pp])))):
                return False

    return True


def chk_anagrams(file):
    count = 0
    with open(file, 'r') as f:
        for line in f:
            if is_not_anagram(line.strip()):
                count += 1
    return count


if __name__ == "__main__":
    #print(is_passphrase("aa bb cc dd ee"))
    #print(is_passphrase("aa bb cc dd aa"))
    #print(is_passphrase("aa bb cc dd aaa"))
    #print(chk_passphrases('passphrases.txt'))

    print(is_not_anagram("abcde fghij"))
    print(is_not_anagram("abcde xyz ecdab"))
    print(is_not_anagram("a ab abc abd abf abj"))
    print(is_not_anagram("iiii oiii ooii oooi oooo"))
    print(is_not_anagram("oiii ioii iioi iiio"))
    print(chk_anagrams('passphrases.txt'))

