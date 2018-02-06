import re
import string
frequency = {}
document_text = open('lyrics.txt', 'r')
text_string = document_text.read().lower()
text_string.replace(',','')
# words='kill,'
match_pattern = re.findall(r'\bdie|death|dead|dying|kill|hell|evil\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print (words, frequency[words])