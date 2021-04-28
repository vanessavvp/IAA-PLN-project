#!/usr/bin/env python3
"""
Created on Thursday April 22, 2021

@author: Vanessa Valentina Villalba Pérez
Natural language processing project PLN 1º part

"""
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


def reading_file(input_file):
  file_content = open(input_file,"rt")
  file_data = file_content.read().split() 
  return file_data


def preprocessing_words(file_data_list):
  output_list = []
  for word in file_data_list:
    if word.islower() == False:
      word = word.lower()
    output_list.append(word)
  # stopwords.words('english')
  # en_stops = set(stopwords.words('english'))
  return output_list


def writing_file(output_list, vocabulary_file):
  total_words = len(output_list)
  new_file = open(vocabulary_file,"wt")
  new_file.write("Número de palabras: " + str(total_words) + "\n")
  for word in output_list:
    new_file.write(word + "\n")


def main():
  input_file = "ecom-train.csv"
  output_file = "vocabulario.txt"
  data_list = reading_file(input_file)
  final_list = preprocessing_words(data_list)
  writing_file(final_list, output_file)


main()






