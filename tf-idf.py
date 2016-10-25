### implementing jaccard score calculator and tf-idf values for a set of documents


from __future__ import division
import string
import math
import re

tfidf_dictionary = {}
    # creating a dictionary of if-idf's indexed bt terms

# print stop_word_list

# define funtion for tokenizing the string
tokenize = lambda doc: doc.lower().split(" ")

document_0 = "China has a strong economy that is growing at a rapid pace. However politically it differs greatly from the US Economy."
document_1 = "At last, China seems serious about confronting an endemic problem: domestic violence and corruption."
document_2 = "Japan's prime minister, Shinzo Abe, is working towards healing the economic turmoil in his own country for his view on the future of his people."
document_3 = "Vladimir Putin is working hard to fix the economy in Russia as the Ruble has tumbled."
document_4 = "What's the future of Abenomics? We asked Shinzo Abe for his views"
document_5 = "Obama has eased sanctions on Cuba while accelerating those against the Russian Economy, even as the Ruble's value falls almost daily."
document_6 = "Vladimir Putin is riding a horse while hunting deer. Vladimir Putin always seems so serious about things - even riding horses. Is he crazy?"

num_of_docs = 7
# total number of documents in corpus

all_documents = [document_0, document_1, document_2, document_3, document_4, document_5, document_6]

# calculates the jaccard coefficient
def jaccard_similarity(query, document):
	q_intersection_d = set(query).intersection(set(document))
	q_union_d = set(query).union(set(document))
	jaccard_score = q_intersection_d/q_union_d
	return jaccard_score

def term_frequency(term, tokenized_document):
    return tokenized_document.count(term)

# term frequency 
def logarithmic_tf(term, tokenized_document):
    count = tokenized_document.count(term)
    if count == 0:
        return 0
    else:
    	return 1 + math.log(count)

# computing the inverse document frequency
def compute_idf(tokenized_documents):
    idf_values = {}
    all_tokens_set = set([item for sublist in tokenized_documents for item in sublist])
    for tkn in all_tokens_set:
        contains_token = map(lambda doc: tkn in doc, tokenized_documents)
        idf_values[tkn] = 1 + math.log(len(tokenized_documents)/(sum(contains_token)))
    return idf_values


def clean_data(text_string):
    #defining a list of special characters to be used for text cleaning
    special_characters = [",",".","'",";","\n", "?", "!", ":"] 
    cleaned_string = str(text_string)
    # removing stop words
    for ch in special_characters:
        cleaned_string = cleaned_string.replace(ch, "")
        cleaned_string = cleaned_string.lower()
    return cleaned_string

def remove_stop_words(document):
    # defining a stop word list
    words_file = "stop_words.txt"
    stop_word_list = []
    stop_word_list = [word for line in open(words_file, 'r') for word in line.split(",")]
    cleaned_doc = []
    for term in document:
        if term not in stop_word_list:
            # print term
            term = clean_data(term)
            # remove special characters 
            cleaned_doc.append(term)
    return cleaned_doc    

def tfidf(documents):
    global tfidf_dictionary
    global num_of_docs

    tokenized_documents = []
    for d in documents:
        doc = tokenize(d)
        # print doc
        doc = remove_stop_words(doc)
        tokenized_documents.append(doc)
    print tokenized_documents

    print "\n\ntf-idf's are:"
    count = 0
    
    idf = compute_idf(tokenized_documents)

    for document in tokenized_documents:
        doc_tfidf = []

        print "-----------------------------------------------------------------------------------------"
        print "document " + str(count)
        print "-----------------------------------------------------------------------------------------"
        doc_dictionary = {}
        # indexed by terms to contain tf-idf values
        for term in idf.keys():
            tf = logarithmic_tf(term, document)
            tfidf = tf * idf[term]
            doc_dictionary[term] = tfidf
            print str(term) + "-> tf: " + str(tf) + ", idf: " + str(idf[term]) + ", tfidf: " + str(tfidf) 
            doc_tfidf.append(tfidf)

        tfidf_dictionary["Document" + str(count)] = doc_dictionary


        count = count+1

    return tfidf_dictionary


tfidf_dictionary = tfidf(all_documents)
# print docs
print "\n\n"
 
# this is a dictionary of tf-idf's of every term in every document
print tfidf_dictionary

