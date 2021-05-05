#!/usr/bin/env python3
"""
Created on Wednesday May 5, 2021

@author: Vanessa Valentina Villalba Pérez
Natural language processing project PLN 2º part
"""
import re
import csv
import nltk
import string

# nltk.download('stopwords')
# nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class_b, class_c, class_e, class_h = {}, {}, {}, {}

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
    words = preprocessing_words(lines[i][1])
    for word in words:
      if (lines[i][0] == 'Books'): 
        if (word in class_b):
          class_b[word] += 1
        else:
          class_b[word] = 1
      if (lines[i][0] == 'Clothing & Accesories'):
        if (word in class_c):
          class_c[word] += 1
        else:
          class_c[word] = 1
      if (lines[i][0] == 'Electronics'):
        if (word in class_e):
          class_e[word] += 1
        else:
          class_e[word] = 1
      if (lines[i][0] == 'Household'):
        if (word in class_h):
          class_h[word] += 1
        else:
          class_h[word] = 1

  
def corpus_documents_number(lines):
  text = 'Numero de documentos del corpus: ' + str(len(lines)) + '\n'
  writing_file('aprendizajeH.txt', text)
  writing_file('aprendizajeB.txt', text)
  writing_file('aprendizajeC.txt', text)
  writing_file('aprendizajeE.txt', text)


def corpus_words_number(file_name):
  print('hola')
  # data = read_and_tokenize(file_name)
  # preprocessing_words(data)

def writing_file(file_name, text):
  new_file = open(file_name,"wt")
  new_file.write(text)
  print("\nThe file was successfully written! into \"" + file_name + "\" file")


def main():
  file = 'ecom-train.csv'
  lines = reading_file(file)
  corpus_documents_number(lines)
  initialize_dictionaries(lines)
  #corpus_words_number(file)
  

main()