import requests as req
from bs4 import BeautifulSoup as bs
import random
import json

def GetSubtitle(Vid):
    # Grab the HTML
    url = "https://tw.voicetube.com/videos/"+ str(Vid) +"?ref=new"
    headers = { "Host": "tw.voicetube.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "close",
                "Upgrade-Insecure-Requests": "1"}
    # Parse the HTML
    r = req.get(url, headers=headers)
    # Get sequences
    soup = bs(r.text, 'html.parser')
    soup = soup.find(id="show-caption-table")
    soup = soup.select('tr td > span')
    # Json format
    sequence = []
    for i in soup:
        sequence.append(i.get_text())

    """
    #Generate output files
    with open(str(Vid)+".txt", "wb") as file:
        for i in sequence:
            #for j in i.keys():
                #file.write(('\"' + j + '\"\n').encode('utf8'))
            for j in i.values(): 
                file.write(('\"' + j + '\"\n').encode('utf8'))
    """
    return GetWordList(Vid,sequence)
    
def GetWordList(Vid,seq):
    # Grab the HTML
    url = "https://tw.voicetube.com/videos/"+ str(Vid) +"?ref=new"
    headers = { "Host": "tw.voicetube.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "close",
                "Upgrade-Insecure-Requests": "1"}
    # Parse the HTML
    r = req.get(url, headers=headers)
    url = "https://tw.voicetube.com/videos/ajax_get_vols/"+ str(Vid) +"/tw"
    cookies = r.cookies
    r = req.get(url, headers=headers,cookies=cookies)
    soup = bs(r.text, 'html.parser')
    #print(soup.prettify())
    soup = soup.find(id="toeic")
    #print(soup.prettify())
    soup = soup.select('ol li > b')
    
    word = []
    for i in soup:
        word.append(i.get_text())
    #print(word)
    qz_word = []
    for i in seq:
        for j in word:
            if j in i:
                qz_word.append(i)
    qz = list(set(qz_word))
    awsr = []
    for i in range(0,len(qz)):
        for j in word:
            if j in qz[i]:
                awsr.append(str(VocabularyQuiz(j,qz[i])))
                
    return(','.join(awsr))
                
def VocabularyQuiz(word,sentence):
    foo = []
    seq = sentence.replace(word,'____')
    #print(seq)
    foo.append(seq.capitalize())
    r = req.get('http://www.thesaurus.com/browse/'+str(word)+'?s=t')
    soup = bs(r.text, "html.parser")
    soup = soup.find(class_="container-info antonyms")
    ind = []
    
    if soup!=None:
        soup = soup.select('div ul li a > span')
        for i in soup:
            ind.append(i.get_text())
    else:
        pass
    
    r = req.get('http://www.synonym.com/synonyms/'+str(word))
    soup = bs(r.text, "html.parser")
    soup = soup.find(class_="antonyms")
    if soup!=None:
        soup = soup.select('li > a')
        for i in soup:
            ind.append(i.get_text())
    else:
        pass
    
    ind = list(set(ind))
    #print(ind)
    abcd = ['A','B','C','D']
    if len(ind)>=3:
        aws = random.sample(ind,3) + [word]
        for i in range(0,len(aws)):
            foo.append('('+abcd[i]+') '+str(aws[i]))
    else:
        aws = ind + [word]
        for i in range(0,len(aws)):
            foo.append('('+abcd[i]+') '+str(aws[i]))
    return(','.join(foo))






if __name__ == "__main__":
    Vid = 44509
    print(GetSubtitle(Vid))
