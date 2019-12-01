import pandas as pd
import re
import glob,csv
from operator import is_not
from functools import partial
import json
from translate import Translator
from TurkishStemmer import TurkishStemmer
from polyglot.text import Text
import codecs
import nltk
from nltk.corpus import stopwords
import itertools
import operator


dataset = {"":[]}
list = []
list1 = []
list2 = []
Stemmer = TurkishStemmer()
points = {"":[]}

#Returns array after remove duplicate values
def unique(list1): 
    unique_list = [] 
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

list = unique(list) 
list1 = unique(list1) 
list2 = unique(list2)

#Get Dataset Value by id
def get(checkList,did):
    for element in checkList:
        if (is_phrase_in(did,element)):
            return element.split(",")[1] 
      
#Get Dataset Value  by id
def get_(checkList,did):
    for element in checkList:
        if (is_phrase_in(did, element[0])):
            return element[0].split(",")[1]

#Check str exact match       
def is_phrase_in(phrase, text):
    return re.search(r"\b{}\b".format(phrase), text, re.IGNORECASE) is not None


#Need for train
for num in range(0,3):
    f = open(r'C:\Users\Emre\Desktop\Dataset\dia'+str(num)+".csv")
    for line in f:
        if (line.replace('"', '').splitlines() not in list):
            list.append(line.replace('"', '').splitlines())
    f.close() 



for num in range(0,2):
    f = open(r'C:\Users\Emre\Desktop\Dataset\sym'+str(num)+".csv")
    for line in f:
        if ('(' in line.replace('"', '').splitlines()[0]):
            index = line.replace('"', '').splitlines()[0].find("(")
            list1.append(line.replace('"', '').splitlines()[0][0:index])  
        else:
            list1.append(line.replace('"', '').splitlines()[0])    

    f.close() 


f = open(r'C:\Users\Emre\Desktop\Dataset\diffsydiw.csv')
for line in f:
    if (line.replace('"', '').splitlines() not in list):
         list2.append(line.replace('"', '').splitlines())
f.close() 


#Creating Dataset
'''
for el in list2:
    diseaseId = el[0].split(",")[0]
    diseaseName = get_(list,diseaseId)
    sempId = el[0].split(",")[1]
    sempName = get(list1,sempId)
    if (diseaseName not in dataset):
        if (sempName != None and sempName!=''):
            dataset[diseaseName] = [sempName]
    else:
        if (sempName != None and sempName!=''):
            dataset[diseaseName].append(sempName)
count = 1
'''

#Read created dataset
with open('myfile.txt',encoding="utf8") as handle:
    dataset = json.loads(handle.read())

#Some NLP process(like stem,tokenization) - need for train
'''
for ele in dataset:
    for elem in dataset[ele]:
        ind = dataset[ele].index(elem)
        fullWords = Text(elem)
        fullWords.language="tr"
        cleanedFullTxt = ""
        for word in fullWords.words:
            cleanedFullTxt = cleanedFullTxt + Stemmer.stem(word) + " "
        dataset[ele][ind] = cleanedFullTxt
        print(str(count) + "-)" + str(elem) + " sadeleştirildi.  =>" + str(cleanedFullTxt))
        count+=1
'''
        

#stopwords list
trStopwords = ["a","acaba","altı","altmış","ama","ancak","arada","artık","asla","aslında","ayrıca","az","bana","bazen","bazı","bazıları","belki","ben","benden","beni","benim","beri","beş","bile","bilhassa","bin","bir","biraz","birçoğu","birçok","biri","birisi","birkaç","birşey","biz","bizden","bize","bizi","bizim","böyle","böylece","bu","buna","bunda","bundan","bunlar","bunları","bunların","bunu","bunun","burada","bütün","çoğu","çoğunu","çok","çünkü","da","daha","dahi","dan","de","defa","değil","diğer","diğeri","diğerleri","diye","doksan","dokuz","dolayı","dolayısıyla","dört","e","edecek","eden","ederek","edilecek","ediliyor","edilmesi","ediyor","eğer","elbette","elli","en","etmesi","etti","ettiği","ettiğini","fakat","falan","filan","gene","gereği","gerek","gibi","göre","hala","halde","halen","hangi","hangisi","hani","hatta","hem","henüz","hep","hepsi","her","herhangi","herkes","herkese","herkesi","herkesin","hiç","hiçbir","hiçbiri","i","ı","için","içinde","iki","ile","ilgili","ise","işte","itibaren","itibariyle","kaç","kadar","karşın","kendi","kendilerine","kendine","kendini","kendisi","kendisine","kendisini","kez","ki","kim","kime","kimi","kimin","kimisi","kimse","kırk","madem","mi","mı","milyar","milyon","mu","mü","nasıl","ne","neden","nedenle","nerde","nerede","nereye","neyse","niçin","nin","nın","niye","nun","nün","o","öbür","olan","olarak","oldu","olduğu","olduğunu","olduklarını","olmadı","olmadığı","olmak","olması","olmayan","olmaz","olsa","olsun","olup","olur","olursa","oluyor","on","ön","ona","önce","ondan","onlar","onlara","onlardan","onları","onların","onu","onun","orada","öte","ötürü","otuz","öyle","oysa","pek","rağmen","sana","sanki","şayet","şekilde","sekiz","seksen","sen","senden","seni","senin","şey","şeyden","şeye","şeyi","şeyler","şimdi","siz","sizden","size","sizi","sizin","sonra","şöyle","şu","şuna","şunları","şunu","ta","tabii","tam","tamam","tamamen","tarafından","trilyon","tüm","tümü","u","ü","üç","un","ün","üzere","var","vardı","ve","veya","ya","yani","yapacak","yapılan","yapılması","yapıyor","yapmak","yaptı","yaptığı","yaptığını","yaptıkları","ye","yedi","yerine","yetmiş","yi","yı","yine","yirmi","yoksa","yu","yüz","zaten","zira"]

#write created dataset to file as json
with codecs.open('myfile.txt', 'w', encoding='utf-8') as f:
    json.dump(dataset, f, ensure_ascii=False)

#get input from user then clear symbols
sentences = input("Sorguyu Giriniz: ")
sentences = sentences.replace(".","")
sentences = sentences.replace(",","")
sentences = sentences.replace(":","")
sentences = sentences.replace("!","")
sentences = sentences.replace("?","")
sentences = sentences.replace(":","")

#remove stopwords
for stop in trStopwords:
    if((" " + stop + " ") in sentences):
        sentences = sentences.replace((" " + stop + " ")," ")
   
#create combination of choosed 3 words then compare with dataset   
x = Text(sentences).words
combinations = [x[i:j] for i, j in itertools.combinations(range(len(x)+1), 2)]

combinations = [x for x in combinations if len(x)<4]
combination = []
for com in combinations:
    cleanedFullTxt = ""
    fullWords = Text(' '.join(com))
    for word in fullWords.words:
        cleanedFullTxt = cleanedFullTxt + Stemmer.stem(word) + " "
        combination.append(cleanedFullTxt)       


#Give point for every exact match (comparison making on stemmed word)
for ele in dataset:
    
    for elem in dataset[ele]: 
        point = 0
        for com in unique(combination): 
            if(com.lower().strip() == elem.lower().strip()):
                size = len(com.split(" "))
                if(size==1):
                    point+=1
                elif(size==2):
                    point+=20
                elif(size==3):
                    point+=50         
        if (elem not in points):
            points[elem] = str(point)
        else:
            if (point>int(points[elem])):
                points[elem.lower().strip()] = str(point)



# Final Results
for symp in points:
    if (points[symp] != "0"):
        print(symp)
        print(points[symp])
        print("------")