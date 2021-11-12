from back_off_model import back_off_model


def predict(trigram, bigram, unigram, test):
    count = 0

    values = list(unigram.values())
    values.sort()
    values.reverse()
    bad_selected_words = []

    for k, v in unigram.items():
        if v in values[0:75]:
            bad_selected_words.append(k)

    answer = []
    with open('labels.txt', 'r') as file:
        answer = file.readlines()
        answer = list(map(lambda x: x.split(', ')[1].split('\n')[0].lower(), answer))
    correct = 0
    mishe = []

    for t in test:
        probable_word = {}
        for k in trigram.keys():
            p = back_off_model(k, trigram, bigram, unigram)

            if k.__contains__('|' + t[0] + ' ' + t[1]):
                word = k.split('|')[0]
                if word not in probable_word.keys():
                    if word in unigram.keys():
                        probable_word[word] = p
                else:
                    probable_word[word] += p
            if k.__contains__(t[3] + '|' + t[1]):
                word = k.split(' ')[1]
                if word not in probable_word.keys():
                    if word in unigram.keys():
                        probable_word[word] = p
                else:
                    probable_word[word] = p
            if k.__contains__(t[4] + '|') and k.__contains__(' ' + t[3]):
                word = k.split('|')[1].split(' ')[0]
                if word not in probable_word.keys():
                    if word in unigram.keys():
                        probable_word[word] = p
                else:
                    probable_word[word] = p

        for k in bigram.keys():

            if k.__contains__('|' + t[1]):
                word = k.split('|')[0]

                p1 = back_off_model(word + '|' + t[0] + ' ' + t[1], trigram, bigram, unigram)
                p2 = back_off_model(t[3] + '|' + t[1] + ' ' + word, trigram, bigram, unigram)
                p3 = back_off_model(t[4] + '|' + word + ' ' + t[3], trigram, bigram, unigram)

                if word not in probable_word.keys():
                    if word in unigram.keys():
                        probable_word[word] = p1 + p2 + p3

                else:
                    probable_word[word] += p1 + p2 + p3

            if k.__contains__(t[3] + '|'):

                word = k.split('|')[1]
                p1 = back_off_model(word + '|' + t[0] + ' ' + t[1], trigram, bigram, unigram)
                p2 = back_off_model(t[3] + '|' + t[1] + ' ' + word, trigram, bigram, unigram)
                p3 = back_off_model(t[4] + '|' + word + ' ' + t[3], trigram, bigram, unigram)

                if word not in probable_word.keys():
                    if word in unigram.keys():
                        probable_word[word] = p1 + p2 + p3
                else:
                    probable_word[word] += p1 + p2 + p3

        pr_word = {}
        for key, pr in probable_word.items():
            if key not in bad_selected_words:
                pr_word[key] = pr
        print(pr_word.keys())

        try:
            max_probability = max(pr_word.values())
        except:
            max_probability = 0

        count += 1
        if answer[count - 1] in probable_word:
            mishe.append(answer[count - 1])

        words = []
        for k, v in pr_word.items():
            if v == max_probability:
                words.append(v)
                print(count, k, v)
                if answer[count - 1] == k:
                    correct += 1
                    print('correct')
                break

    print('correct = ' + str(correct))
    print('Accuracy =', int(correct) / 80)
    # print(mishe)
