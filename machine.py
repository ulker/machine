# -*- coding: utf-8 -*-
import os, sys, csv, string, re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer

#porter stemmer
def stemmize(text1):
    stemmer = PorterStemmer()
    text1 = " ".join([stemmer.stem(kw) for kw in text1.split(" ")])
    return text1
#noktalama işaretlerini ve özel karakterleri metinden silen fonksiyon   
def remove_punctuation(text1):
    tmp = []
    for i in text1:
       tmp.append(" " if i in ">@#<|!.,;-_*\=)(/&%+^'!:?\"][0123456789$" else i)
    
    tmp = (''.join(tmp))
    return re.sub("\s+", " ", tmp)
	
#ingilizce stopwords leri silen fonksiyon
def remove_stopwords(text1):
    text1 = ' '.join([word for word in text1.split(" ") if word not in stopwords.words("english")])
    return text1

#mail dosyalarını okuyan ve asıl işlemleri yapan fonksiyon
def readFileAndChange(path, newPath):
    directory = os.path.normpath(path)
    with open(newPath, 'a') as f:
        fildnames=['DATA', 'VALUE']
        writer = csv.DictWriter(f, fieldnames=fildnames)

    
        for subdir, dirs, files in os.walk(directory):
            upDirectoryName = subdir.split("/")[-2::][0]
            tempList = []
            for file in files:
                check = False
                with open(os.path.join(subdir, file), 'r') as processFile:
                    for line in processFile:
                        

                        if (line.startswith("X-FileName:") and not check):
                            check = True
                            continue
                        if(("forward" in line) or ("Forwarded" in line) or ("Migration" in line) or ("Original Message" in line)):
                            break
                        if check:
                            line = line.lower()
                            
                            line = remove_punctuation(line)
                            line =remove_stopwords(line)
                            if (len(line) > 5):
                                tempList.append(line.lower())
                    processFile.close()
                tempList = map(lambda s: s.strip(),tempList)
                tempList = [x for x in tempList if x != '']
                if(len(tempList) > 0):
                    writer.writerow({'DATA': ' '.join(tempList), 'VALUE': upDirectoryName})
                tempList = []
    f.close()        
                
                
                
                
               
            #print("File: %s, subdir: %s, " %(' '.join(tempList), upDirectoryName))
    


def main():
    path = "/home/furkan/Masaüstü/veri seti test/"
    newPath = "/home/furkan/Masaüstü/datayenitest.csv"
    readFileAndChange(path, newPath)

if __name__ == "__main__":
    main()