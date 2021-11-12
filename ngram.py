import re


def unigram(training_data):
    unigram_probability = {}
    word_count = {}
    count = 0
    for sentences in training_data:
        if '\'' in sentences:
            sentences = re.sub(r'\s\'', '\'', sentences)
        for w in re.split(r'\s+', sentences):
            if w != '.' and w != '\n':
                count += 1
                if w.lower() in word_count:
                    word_count[w.lower()] += 1
                else:
                    word_count[w.lower()] = 1

    for k, v in word_count.items():
        unigram_probability[k] = v / count


    return unigram_probability


def bigram(training_data):
    bigram_probability = {}
    word_count = {}
    count = 0
    for sentences in training_data:
        if '\'' in sentences:
            sentences = re.sub(r'\s\'', '\'', sentences)

        temp = '<s>'
        for w in re.split(r'\s+', sentences):
            if w != '.' and w != '\n':
                count += 1
                s = w.lower() + '|' + temp

                if s in word_count:
                    word_count[s] += 1
                else:
                    word_count[s] = 1

                temp = w.lower()

            if w == '.':
                count += 1
                s = '</s>' + '|' + temp

                if s in word_count:
                    word_count[s] += 1
                else:
                    word_count[s] = 1

                temp = '<s>'

    for k, v in word_count.items():
        bigram_probability[k] = v / count


    return bigram_probability


def trigram(training_data):
    trigram_probability = {}
    word_count = {}
    count = 0
    for sentences in training_data:
        if '\'' in sentences:
            sentences = re.sub(r'\s\'', '\'', sentences)

        temp1, temp2 = '<s>', '<s>'
        for w in re.split(r'\s+', sentences):
            if w != '.' and w != '\n':
                count += 1
                s = w.lower() + '|' + temp1 + ' ' + temp2

                if s in word_count:
                    word_count[s] += 1
                else:
                    word_count[s] = 1

                temp1 = temp2
                temp2 = w.lower()

            if w == '.':
                count += 1

                s1 = '</s>' + '|' + temp1 + ' ' + temp2
                s2 = '</s>' + '|' + '</s>' + ' ' + temp2

                if s1 in word_count:
                    word_count[s1] += 1
                else:
                    word_count[s1] = 1

                if s2 in word_count:
                    word_count[s2] += 1
                else:
                    word_count[s2] = 1

                temp1, temp2 = '<s>', '<s>'

    for k, v in word_count.items():
        trigram_probability[k] = v / count

    return trigram_probability

