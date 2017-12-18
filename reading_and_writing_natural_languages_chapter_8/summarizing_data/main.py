import re
import string
import requests

from pprint import pprint

_BASE_URL = 'http://pythonscraping.com/files/inaugurationSpeech.txt'


def is_common(ngram):
    common_words = [
        "the", "be", "and", "of", "a", "in", "to", "have", "it",
        "i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
        "they", "is", "an", "at", "but", "we", "his", "from", "that", "not",
        "by", "she", "or", "as", "what", "go", "their", "can", "who", "get",
        "if", "would", "her", "all", "my", "make", "about", "know", "will",
        "as", "up", "one", "time", "has", "been", "there", "year", "so",
        "think", "when", "which", "them", "some", "me", "people", "take",
        "out", "into", "just", "see", "him", "your", "come", "could", "now",
        "than", "like", "other", "how", "then", "its", "our", "two", "more",
        "these", "want", "way", "look", "first", "also", "new", "because",
        "day", "more", "use", "no", "man", "find", "here", "thing", "give",
        "many", "well"
    ]

    for word in ngram:
        if word in common_words:
            return True
    return False


def clean_input(data_input):
    data_input = re.sub('\n+', ' ', data_input).lower()
    data_input = re.sub('\[[0-9]*\]', '', data_input)
    data_input = re.sub('\s+', ' ', data_input)
    data_input = bytes(data_input, 'UTF-8')
    data_input = data_input.decode('ascii', 'ignore')

    clean_input_list = list()
    data_input = data_input.split(' ')

    for item in data_input:
        item = item.strip(string.punctuation)

        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            clean_input_list.append(item)

    return clean_input_list


def ngrams(data_input, n):
    data_input = clean_input(data_input)
    output = dict()

    for i in range(len(data_input) - n + 1):
        ngram_temp = data_input[i:i+n]
        if not is_common(ngram_temp):
            ngram_temp = ' '.join(ngram_temp)
            if ngram_temp not in output:
                output[ngram_temp] = 0

            output[ngram_temp] += 1

    output = [{'ngram': key, 'frequency': value} for key, value in output.items()]
    return output


def get_text_summary(sorted_ngrams, original_text):

    summary_sentences = list()
    text_sentences = re.split('\.|\!|\?', original_text)
    for ngram in sorted_ngrams:

            if n

    return '\n\n'.join(summary_sentences)

def main():
    content = requests.get(_BASE_URL).text

    ngram_list = ngrams(content, 2)
    sorted_n_grams = sorted(ngram_list, key=lambda x: x['frequency'], reverse=True)
    print(len(sorted_n_grams))
    print()
    pprint(sorted_n_grams[:50])
    print()
    print()
    print()
    summary_n_grams = [ngram['ngram'] for ngram in sorted_n_grams[:5]]
    summary = get_text_summary(summary_n_grams, content)
    print(summary)


if __name__ == '__main__':
    main()
