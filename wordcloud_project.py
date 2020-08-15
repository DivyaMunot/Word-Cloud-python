#importing all the libraries

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import io
import sys


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    file_contents2 = ""
    for index, char in enumerate(file_contents):
        if char.isalpha() == True or char.isspace():
            file_contents2 += char

    file_contents2 = file_contents2.split()
    file_without_uninteresting_words = []
    
    for word in file_contents2:
        if word.lower() not in uninteresting_words and word.isalpha() == True:
            file_without_uninteresting_words.append(word)
            
    frequencies = {}
    
    for word in file_without_uninteresting_words:
        if word.lower() not in frequencies:
            frequencies[word.capitalize()] = 1
        else:
            frequencies[word.capitalize()] += 1
    
    #wordcloud
    
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()
    
# Display your wordcloud image
font_path = '/content/GoodBoom.ttf'     # you can change the font style from here

cloud = wordcloud.WordCloud(width = 1000, height = 1000,
                            font_path = font_path,
                            random_state = 1,
                            colormap='prism',
                            collocations=False,
                            background_color = 'white',
                            min_font_size = 10)

# words displayed in wordcloud
myimage = calculate_frequencies("GAYU DV BESTFRIENDS nustaabhyas gossips dreamhouse FOREVER redvelvetcake SCHOOLFRIENDS coffee fun LOVE rumaliroti blog secrets FRIENDSHIP tinder TOGETHER ca engineer nightouts MASTI pasta ENJOYMENT endlesscalls MOMENTS amazon LIFELONG JOY partyyy HAPPINESS linkedin WORLD FAMILY")
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(myimage, interpolation = 'bilinear')
plt.axis('off')
plt.show()
