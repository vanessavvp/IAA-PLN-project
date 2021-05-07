#!/usr/bin/env python3
"""
Created on Wednesday May 5, 2021

@author: Vanessa Valentina Villalba Pérez
Natural language processing project PLN 2º part
"""
import re
import csv
import math
import nltk
import string

# nltk.download('stopwords')
# nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import vocabulario


class_b, class_c, class_e, class_h = {}, {}, {}, {}
vocabulary_size = 0
total_class_b = 0
total_class_c = 0
total_class_e = 0
total_class_h = 0
unk_added = False
total_words = []
entries_b = 0
entries_c = 0
entries_e = 0
entries_h = 0


def reading_file(input_file):
  with open(input_file, "r", encoding = 'utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lines = list(csv_reader)
    return lines
    

def preprocessing_words(entire_line):
  punctuation_marks = string.punctuation + '…' + '”' + '“' + '-' + '‘'+ '’' + '´' + '—'
  data = entire_line.translate(str.maketrans(dict.fromkeys(punctuation_marks, ' ')))
  en_stops = set(stopwords.words('english'))
  output_list = []
  single_words = data.split()
  for word in single_words:
    # Only alphabetics words will be processed
    if (word.isalpha()):
      word = word.lower()
      # Stopwords will be ignored
      if (word not in en_stops):
        output_list += [word]
  output = sorted(output_list)
  return output


def adding_words(iteration, lines, class_to_be_added):
  words = preprocessing_words(lines[iteration][1])
  for word in words:
    if word in class_to_be_added:
      class_to_be_added[word] += 1
    else:
      class_to_be_added[word] = 1


def initialize_dictionaries(lines):
  for i in range(len(lines)):
    if (lines[i][0] == 'Books'):
      adding_words(i, lines, class_b)
    if (lines[i][0] == 'Clothing & Accessories'):
      adding_words(i, lines, class_c)
    if (lines[i][0] == 'Electronics'):
      adding_words(i, lines, class_e)
    if (lines[i][0] == 'Household'):
      adding_words(i, lines, class_h)

  
def counting_entries(file_name, total_entries):
  text = 'Numero de documentos del corpus: ' + str(total_entries) + '\n'
  write_file(file_name, text)
 

def corpus_documents_number(lines):
  global entries_b, entries_c, entries_e, entries_h
  # Numero de repeticiones de cada entrada en el csv, de cada clase
  for i in range(len(lines)):
    if (lines[i][0] == 'Books'):
      entries_b += 1
    if (lines[i][0] == 'Clothing & Accessories'):
      entries_c += 1
    if (lines[i][0] == 'Electronics'):
      entries_e += 1
    if (lines[i][0] == 'Household'):
      entries_h += 1
  counting_entries('aprendizajeB.txt', entries_b)
  counting_entries('aprendizajeC.txt', entries_c)
  counting_entries('aprendizajeE.txt', entries_e)
  counting_entries('aprendizajeH.txt', entries_h)


def corpus_words_number():
  text = 'Numero de palabras del corpus: ';
  total_class_b = sum(class_b.values()) 
  total_class_c = sum(class_c.values())
  total_class_e = sum(class_e.values())
  total_class_h = sum(class_h.values())
  write_file('aprendizajeB.txt', text + str(total_class_b))
  write_file('aprendizajeC.txt', text + str(total_class_c))
  write_file('aprendizajeE.txt', text + str(total_class_e))
  write_file('aprendizajeH.txt', text + str(total_class_h))


def print_frec_log(file_name, words_class):
  text = '\nPalabra: '
  text2 = ' Frec: '
  text3 = ' LogProb: '
  for key in total_words:
    key = key.rstrip('\n')
    word = key
    frec = words_class[key] if key in words_class else 0
    log = math.log((frec + 1) / (len(words_class) + vocabulary_size))
    write_file(file_name, text + word + text2 + str(frec) + text3 + str(log))


def frequency_and_log_prob():
  print_frec_log('aprendizajeB.txt', class_b)
  print_frec_log('aprendizajeC.txt', class_c)
  print_frec_log('aprendizajeE.txt', class_e)
  print_frec_log('aprendizajeH.txt', class_h)


def write_file(file_name, text):
  new_file = open(file_name,"at")
  new_file.write(text)


def read_vocabulary_file(file_name):
  global total_words, vocabulary_size
  new_file = open(file_name,"r")
  words = (new_file.readline()).split()
  vocabulary_size = int(words[3])
  total_words = new_file.readlines()
  new_file.close()


def main():
  vocabulario.delete_file_content('aprendizajeB.txt')
  vocabulario.delete_file_content('aprendizajeC.txt')
  vocabulario.delete_file_content('aprendizajeE.txt')
  vocabulario.delete_file_content('aprendizajeH.txt')
  file = 'ecom-train.csv'
  lines = reading_file(file)
  read_vocabulary_file('vocabulario.txt')
  corpus_documents_number(lines)
  initialize_dictionaries(lines)
  corpus_words_number()
  frequency_and_log_prob()


main()