#!/usr/bin/env python3
"""
Created on Thursday April 22, 2021

@author: Vanessa Valentina Villalba Pérez
Natural language processing project PLN 1º part

"""
import re
import csv
import nltk
import string

nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


vocabulary_size = 0

def read_and_tokenize(input_file):
  with open(input_file, "r", encoding = 'utf-8-sig') as csv_file:
    punctuation_marks = string.punctuation + '…' + '”' + '“' + '-' + '‘'+ '’' + '´' + '—'
    csv_reader = csv.reader(csv_file, delimiter=',')
    list_of_rows = list(csv_reader)
    data = []
    for line in list_of_rows:
      # Every line will be tokenized into a word without taking into account the punctuation marks
      data += word_tokenize(line[1].translate(str.maketrans(dict.fromkeys(punctuation_marks, ' '))))
    return data


def preprocessing_words(data):
  en_stops = set(stopwords.words('english'))
  output_list = set()
  for word in data:
    # Only alphabetics strings will be processed
    if (word.isalpha()):
      word = word.lower()
      # Stopwords will be ignored
      if (word not in en_stops):
        output_list.add(word)
  output_list = sorted(output_list)
  vocabulary_size = len(output_list)
  return output_list


def get_vocabulary_size():
  return vocabulary_size


def delete_file_content(file_name):
  file = open(file_name, 'r+')
  file.truncate(0)
  file.close()


def writing_file(output_list, vocabulary_file):
  output_list.append('<UNK>')
  delete_file_content(vocabulary_file)
  total_words = len(output_list)
  new_file = open(vocabulary_file,"wt")
  new_file.write("Número de palabras: " + str(total_words) + "\n")
  for word in output_list:
    new_file.write(word + "\n")
  # print("The file was successfully written! into \"" + vocabulary_file + "\" file")


def main():
  print("\nLoading...\n")
  input_file = 'ecom-train.csv'
  output_file = 'vocabulario.txt'
  data_list = read_and_tokenize(input_file)
  final_list = preprocessing_words(data_list)
  writing_file(final_list, output_file)


main()



