import re


def back_off_model(data, trigram, bigram, unigram):

    # alpha = 0.999975
    # beta = 0.000020
    # gama = 0.000005

    alpha = 0.8
    beta = 0.15
    gama = 0.05

    bigram_probability = 0
    unigram_probability = 0
    trigram_probability = 0

    if data.split('|')[0] + '|' + re.split(r'\s+', data)[1] in bigram:
        bigram_probability = bigram[data.split('|')[0] + '|' + re.split(r'\s+', data)[1]]
    if data.split('|')[0] in unigram:
        unigram_probability = unigram[data.split('|')[0]]
    if data.split('|')[0] + '|' + re.split(r'\s+', data)[0] + ' ' + re.split(r'\s+', data)[1] in trigram:
        trigram_probability = trigram[
            data.split('|')[0] + '|' + re.split(r'\s+', data)[0] + ' ' + re.split(r'\s+', data)[1]]

    return alpha * trigram_probability + beta * bigram_probability + gama * unigram_probability


