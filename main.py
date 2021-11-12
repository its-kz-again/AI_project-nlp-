import re
from ngram import unigram, bigram, trigram
from predict import predict


with open('Train_data.txt', 'r') as train:
    training_data = train.readlines()


for i, t in enumerate(training_data):
    training_data[i] = re.sub(r'[^a-zA-Z.\']', ' ', t)

with open('Test_data.txt', 'r') as test:
    data = test.readlines()[1:]


unigram_probability = unigram(training_data)
bigram_probability = bigram(training_data)
trigram_probability = trigram(training_data)

test_data = []
for i, t in enumerate(data):
    data = re.sub(r'[^a-zA-Z.\'$]', ' ', t)
    data = re.sub(r'\s+\'', '\'', data)
    data = list(re.findall(r'[^\s]+', data))

    data.insert(0, '<s>')
    data.insert(0, '<s>')
    data.pop()
    data.append('</s>')
    data.append('</s>')
    index = data.index('$')
    data = data[index - 2:index + 3]

    test_data.append(list(map(lambda x: x.lower(), data)))

predict(trigram_probability, bigram_probability, unigram_probability, test_data)
