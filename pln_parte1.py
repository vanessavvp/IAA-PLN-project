#!/usr/bin/env python3
"""
Created on thursday April 22 

@author: Vanessa Valentina Villalba Pérez
Proyecto PLN 1º parte
"""

input_file = "ecom-train.csv"
file_content = open(input_file,"rt")
file_data = file_content.read().split()
total_words = len(file_data)
# print (total_words)

vocabulary_file = "vocabulario.txt"
new_file = open(vocabulary_file,"wt")
new_file.write("Número de palabras: " + str(total_words) + "\n")
for word in file_data:
  new_file.write(word + "\n")
