import re

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
extra =[]
wordfreq = []
frequency_list =[]
frequency_list = frequency.keys()
def print_word_freq(file):
  
  with open(file) as f:
    for items in f:
      extra.append(items)
     
   
for items in extra:
    clean = re.sub(r"[!?.,]","",items.lower())
    cleaner = clean.split()
    wordfreq.append(cleaner)

for word in list(working_list):  
  if word in STOP_WORDS:
    working_list.remove(word)
    for word in working_list:
      count = frequency.get(word,0)
      frequency[word] = count + 1
     
      
 for words in frequency_list:
               # ^ counting words in text
  print(words,'|' ,frequency[words) 
    
if __name__ == "__main__":

    import argparse
    from pathlib import Path
        
    parser = argparse.ArgumentParser (
    description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

file = Path(args.file)
if file.is_file():
        print_word_freq(file)
else:
        print(f"{file} does not exist!")
        exit(1)
