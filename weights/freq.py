from utils.preprocessor import Preprocessor
from sys import stdout


class input:

    def input_from_file(self, input_file):
        input.text = open(input_file, 'r+').read()
        return input.text


class output:

    def display(self, word):
        print (word)

    def write_to_file(self, output_file, word):
        with open(output_file, 'w') as f:
            f.write(word)


class weights:

    __tot_freq = []
    __term_freq_matrix = []
    __inverse_document_freq = []

    def ret_tot_freq(self):
        return weights.__tot_freq

    def get_tot_files(self, number):
        weights.__tot_files = number

    def update_term_freq_matrix(self, number):
        for i in range(1, number):
            sentence = open('out%i.txt' % i, 'r+').read()
            arr = []
            for each_word in feature_set.unique_features.split():
                arr.append(sentence.count(each_word))
            weights.__term_freq_matrix.append(arr)

    def ret_term_freq_matrix(self):
        return weights.__term_freq_matrix

    def update_inverse_document_freq(self, tot_files, unique_features):
        for each_word in unique_features.split():
            docs = 0
            for i in range(1, tot_files):
                data = open('out%i.txt' % i, 'r+').read()
                if data.count(each_word) > 0:
                    docs += 1
            weights.__inverse_document_freq.append(docs)

    def ret_inverse_document_freq(self):
        return weights.__inverse_document_freq


class feature_set:

    all_features = " "

    unique_features = " "
    __tot_files = 0

    def get_all_features(self, word):
        all_features = word

    def ret_all_features(self):
        return feature_set.all_features

    def update_unique_features(self, sentence):
        for word in sentence.split():
            if word not in feature_set.unique_features:
                feature_set.unique_features += word + ' '

    def ret_features(self):
        return feature_set.unique_features

    def ret_tot_files(self):
        return feature_set.__tot_files

    def get_tot_files(self, number):
        feature_set.__tot_files = number


def main():
    a = input()
    b = output()
    prep1 = Preprocessor()
    i = 1
    c = weights()
    f = feature_set()
    while 1:
        try:
            with open('%d.txt' % i):
                inputdataset = a.input_from_file('%d.txt' % i)
                filter1 = prep1.to_lower_case(inputdataset)
                filter2 = prep1.stop_word_eliminate(filter1)
                filter3 = prep1.stem_word(filter2)
                b.write_to_file('out%i.txt' % i, filter3)
                f.all_features += filter3 + ' '
                i += 1
        except IOError:
            break

    f.get_tot_files(i-1)
    f.update_unique_features(f.all_features)

    for each_word in f.unique_features.split():
        c.ret_tot_freq().append(f.all_features.count(each_word))

    #j = 0
    #for each_word in f.unique_features.split():
    #    stdout.write(each_word + ' ' + str(c.ret_tot_freq()[j]) + '\n')
    #    j += 1

    c.update_term_freq_matrix(f.ret_tot_files())
    c.update_inverse_document_freq(f.ret_tot_files(),f.unique_features)

    #print c.ret_inverse_document_freq()
    #print c.ret_term_freq_matrix()

main()
