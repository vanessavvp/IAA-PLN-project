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


class_b, class_c, class_e, class_h = {}, {}, {}, {}
vocabulary_size = 0
total_class_b = 0
total_class_c = 0
total_class_e = 0
total_class_h = 0


def reading_file(input_file):
  with open(input_file, "r", encoding = 'utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lines = list(csv_reader)
    return lines
    

def preprocessing_words(entire_line):
  punctuation_marks = string.punctuation + '…' + '”' + '“' + '-' + '‘'+ '’' + '´' + '—'
  data = entire_line.translate(str.maketrans(dict.fromkeys(punctuation_marks, ' ')))
  en_stops = set(stopwords.words('english'))
  output_list = set()
  single_words = data.split()
  for word in single_words:
    # Only alphabetics words will be processed
    if (word.isalpha()):
      word = word.lower()
      # Stopwords will be ignored
      if (word not in en_stops):
        output_list.add(word)
  output_list = sorted(output_list)
  return output_list


def initialize_dictionaries(lines):
  for i in range(len(lines)):
    if (lines[i][0] == 'Books'): 
      words = preprocessing_words(lines[i][1])
      for word in words:
        if (word in class_b):
          class_b[word] += 1
        else:
          class_b[word] = 1

    if (lines[i][0] == 'Clothing & Accessories'):
      words = preprocessing_words(lines[i][1])
      for word in words:
        if (word in class_c):
          class_c[word] += 1
        else:
          class_c[word] = 1

    if (lines[i][0] == 'Electronics'):
      words = preprocessing_words(lines[i][1])
      for word in words:
        if (word in class_e):
          class_e[word] += 1
        else:
          class_e[word] = 1

    if (lines[i][0] == 'Household'):
      words = preprocessing_words(lines[i][1])
      for word in words:
        if (word in class_h):
          class_h[word] += 1
        else:
          class_h[word] = 1

  
def corpus_documents_number(lines):
  text = 'Numero de documentos del corpus: ' + str(len(lines)) + '\n'
  writing_file('aprendizajeB.txt', text)
  writing_file('aprendizajeC.txt', text)
  writing_file('aprendizajeE.txt', text)
  writing_file('aprendizajeH.txt', text)
  

def corpus_words_number():
  text = 'Numero de palabras del corpus: ';
  total_class_b = sum(class_b.values()) 
  total_class_c = sum(class_c.values())
  total_class_e = sum(class_e.values())
  total_class_h = sum(class_h.values())
  writing_file('aprendizajeB.txt', text + str(total_class_b))
  writing_file('aprendizajeC.txt', text + str(total_class_c))
  writing_file('aprendizajeE.txt', text + str(total_class_e))
  writing_file('aprendizajeH.txt', text + str(total_class_h))


def frequency_and_log_prob(voc_size):
  text = '\nPalabra: '
  text2 = ' Frec: '
  text3 = ' LogProb: '
  for key in class_b:
    word = str(key)
    frec = class_b[key]
    log = math.log((frec + 1) / (len(class_b) + voc_size))
    writing_file('aprendizajeB.txt', text + word + text2 + str(frec) + text3 + str(log))

  for key in class_c:
    word = str(key)
    frec = class_c[key]
    writing_file('aprendizajeC.txt', text + word + text2 + str(frec))

  for key in class_e:
    word = str(key)
    frec = class_e[key]
    writing_file('aprendizajeE.txt', text + word + text2 + str(frec))

  for key in class_h:
    word = str(key)
    frec = class_h[key]
    writing_file('aprendizajeH.txt', text + word + text2 + str(frec))


def writing_file(file_name, text):
  new_file = open(file_name,"at")
  new_file.write(text)
  # print("\nThe file was successfully written! into \"" + file_name + "\" file")


def delete_file_content(file_name):
  file = open(file_name, 'r+')
  file.truncate(0)
  file.close()


def read_vocabulary_file(file_name):
  new_file = open(file_name,"r")
  words = (new_file.readline()).split()
  vocabulary_size = int(words[3])
  print(vocabulary_size)
  new_file.close()
  frequency_and_log_prob(vocabulary_size)


def main():
  delete_file_content('aprendizajeB.txt')
  delete_file_content('aprendizajeC.txt')
  delete_file_content('aprendizajeE.txt')
  delete_file_content('aprendizajeH.txt')
  file = 'ecom-train.csv'
  lines = reading_file(file)
  corpus_documents_number(lines)
  initialize_dictionaries(lines)
  corpus_words_number()
  read_vocabulary_file('vocabulario.txt')

main()