'''
feature_functions.py
Implements the feature generation mechanism
Author: Anantharaman Narayana Iyer
Date: 21 Nov 2014
6th Dec: Org gazeteer added
7th Dec: 
'''
from nltk import sent_tokenize, word_tokenize
import nltk
import json
import numpy
import pickle
import datetime


phones = ["phone", "phones", "smartphone", "smartphones", "mobile", "tablet", "tablets", "phablet", "phablets"]
org_list = ['Samsung', 'Apple', 'Microsoft', 'Nokia', 'Sony', 'LG', 'HTC', 'Motorola', 'Huawei', 'Lenovo', 'Xiaomi', 'Acer', 'Asus', 'BlackBerry',
            'Alcatel', 'ZTE', 'Toshiba', 'Vodafone', 'T-Mobile', 'Gigabyte', 'Pantech', 'XOLO', 'Lava', 'Micromax', 'BLU', 'Spice', 'Prestigio',
            'verykool', 'Maxwest', 'Celkon', 'Gionee', 'vivo', 'NIU', 'Yezz', 'Parla', 'Plum']
org_list1 = [m.lower() for m in org_list]
os_list = ["iOS", "Android", "Windows", "Symbian", "Bada", "Unix", "Linux", "Ubuntu", "OS", "RIM", "Firefox"]
os_list1 = [m.lower() for m in os_list]
currency_symbols = ["rs", "inr", "$", "usd", "cents", "rupees"]
size_list = ["inch", "cm", "inches", "cms", r'"', "''", "pixel", "px", "mega", "gb", "mb", "kb", "kilo", "giga", "mega-pixel" ]

brand_product_bigrams_dict = [] # use the web service from Ner_client to get this: ner.get_brand_product_bigrams() # gazeteer based 7th Dec 2014
product_names = []
for v in get_brand_product_bigrams_dict().values():
    for v1 in v:
        product_names.append(v1.lower())

product_name_tokens = [] # some time product names may be strings with many words, we will split these so that we can compare it with input word token
for p in product_names:
    product_name_tokens.extend(p.split())


class FeatureFunctions(object):
    def __init__(self, tag_list = None):
        self.wmap = {}
        self.flist = {"self.fPhone_1","self.fPhone_2","self.fPhone_3",""} #[self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8, self.f9, self.f10, self.f11, self.f12, self.f13]
        self.fdict = {}
        self.check = False
        for k, v in FeatureFunctions.__dict__.items():
            if hasattr(v, "__call__"):
                if k[0] == 'f':
                    self.flist[k] = v # .append(v)
                    tag = k[1:].split("_")[0]
                    val = self.fdict.get(tag, [])
                    val.append(v)
                    self.fdict[tag] = val

        self.supported_tags = self.fdict.keys()        
        return

    def set_wmap(self, sents): # given a list of words sets wmap
        for i in range(len(sents)):
            self.wmap[i] = {'words': sents[i], 'pos_tags': nltk.pos_tag(sents[i])}
        return

    def check_list(self, clist, w):
        #return 0
        w1 = w.lower()
        for cl in clist:
            if w1 in cl:
                return 1
        return 0

    #------------------------------- Phone tag ---------------------------------------------------------
    # The following is an example for you to code your own functions
    # returns True if wi is in phones tag = Phone
    # h is of the form {'ta':xx, 'tb':xx, 'wn':xx, 'i':xx}
    # self.wmap provides a list of sentences (tokens) where each element in the list is a dict {'words': word_token_list, 'pos_tags': pos_tags_list}
    # each pos_tag is a tuple returned by NLTK tagger: (word, tag)
    # h["wn"] refers to a sentence number
    
    def fPhone_1(self, h, tag):
        if tag != "Phone":
            return 0
        words = self.wmap[h["wn"]]['words']        
        if (words[h["i"]].lower() in phones):
           self.check = True
           return 1
        else:
            return 0

   def fPhone_2(self, h, tag):
	if tag != "Phone":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (h['tb'])== "Org":
            self.check = True
            return 1
	else:
		return 0

   def fPhone_3(self, h, tag):
	if tag != "Phone":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (h['tb'])== "Version":
            self.check = True
            return 1
	else:
	    return 0
	

   def fPhone_4(self, h, tag):
	if tag != "Phone":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (h['tb'])== "Family":
            self.check = True
            return 1
	else:
            return 0

    def fOrg_1(self, h, tag):
        if tag != "Org":
            return 0
        words = self.wmap[h["wn"]]['words']        
        if (words[h["i"]].lower() in org_list1):
            self.check = True
            return 1
        else:
            return 0

    def fOrg_2(self, h, tag):
        if tag != "Org":
            return 0
        words = self.wmap[h["wn"]]['words']        
        if (words[h["i"]].lower() in org_list1):
            if(words[h["i"]+ 1].lower() in phones):
                self.check = True
                return 1
        else:
            return 0
    def fOrg_3(self, h ,tag): #low
        if tag != "Org":
            return 0
        words = self.wmap[h["wn"]]['words']
        if(words[h["i"] - 1 ].lower() == "from"):
            if(words[h["i"]].lower() in org_list1):
                self.check = True
                return 1
        else:
            return 0

    def fOrg_4(self, h, tag): #low
        if tag != "Org":
            return 0
        words = self.wmap[h["wn"]]['words']
        if(words[h["i"] - 1 ].lower() == "by"):
            if(words[h["i"]].lower() in org_list1):
                self.check = True
                return 1
        else:
            return 0
    def fOrg_5(self, h, tag): #low
        if tag != "Org":
            return 0
        words = self.wmap[h["wn"]]['words']
        if(words[h["i"] - 1 ].lower().startswith('wh')):
            if(words[h["i"]].lower() in org_list1):
                self.check = True
                return 1
        else:
            return 0

    def fOS_1(self, h, tag):
        if tag != "OS":
            return 0
        words = self.wmap[h["wn"]]['words']
        if( words[h["i"]].lower() in os_list1):
            self.check = True
            return 1
        else:
            return 0
    def fOS_2(self, h, tag):
        if tag != "OS":
            return 0
        words = self.wmap[h["wn"]]['words']
        if( words[h["i"]+ 1 ].lower() in phones):
            self.check = True
            return 1
        else:
            return 0
    def fOS_3(self, h, tag): #low
        if tag != "OS":
            return 0
        words = self.wmap[h["wn"]]['words']
        if( words[h["i"] - 2 ].lower() == "supported"):
            self.check = True
            return 1
        else:
            return 0
    def fOS_4(self, h, tag): #low
        if tag != "OS":
            return 0
        words = self.wmap[h["wn"]]['words']
        if( words[h["i"] - 2].lower() == "run"):
            self.check = True
            return 1
        else:
            return 0
        
    def fOS_5(self, h, tag):
        if tag != "OS":
            return 0
        words = self.wmap[h["wn"]]['words']
        tags = self.wmap[h["wn"]]['pos_tags']
        if( words[h["i"]].lower() in os_list1):
            if( tags[h["i"] + 1] == "CD"):
                self.check = True
                return 1
        else:
            return 0

    def fPrice_1(self, h, tag): 
        if tag != "Price":
            return 0
        words = self.wmap[h["wn"]]['words']
        if( words[h["i"]].lower().endswith('k')):
            self.check = True
            return 1
        else:
            return 0

    def fPrice_2(self, h, tag): 
        if tag != "Price":
            return 0
        words = self.wmap[h["wn"]]['words']
        if( words[h["i"]].lower().endswith('usd')):
            self.check = True
            return 1
        else:
            return 0

    def fPrice_3(self, h, tag): 
        if tag != "Price":
            return 0
        words = self.wmap[h["wn"]]['words']
        tags = self.wmap[h["wn"]]['pos_tags']
        if( tags[h["i"]] == "CD"):
            if(len(words[h["i"]]) > 4):
                self.check = True
                return 1
        else:
            return 0

    def fPrice_4(self, h, tag): 
        if tag != "Price":
            return 0
        words = self.wmap[h["wn"]]['words']
        if( "," in words[h["i"]].lower()):
            self.check = True
            return 1
        else:
            return 0

    def fPrice_5(self, h, tag): 
        if tag != "Price":
            return 0
        words = self.wmap[h["wn"]]['words']
        if( words[h["i"]].lower() in currency_symbols):
            self.check = True
            return 1
        else:
            return 0

    def fPrice_6(self, h, tag): 
        if tag != "Price":
            return 0
        words = self.wmap[h["wn"]]['words']
        tags = self.wmap[h["wn"]]['pos_tags']
        if( h["tb"] == "Price"):
            if(tags[h["i"]] == "CD"):
                self.check = True
                return 1
        else:
            return 0

    def evaluate(self, xi, tag):
        feats = []
        for t, f in self.fdict.items():
            if t == tag:
                for f1 in f:
                    feats.append(int(f1(self, xi, tag)))
            else:
                for f1 in f:
                    feats.append(0)
        return feats

 
   '''
   def fVersion_1(self, h, tag):
	if tag != "Version":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (h['tb'])== "Family":
		return 1
		if(words[])
	else:
		return 0
	
   '''
    #------------------------------- Functions for Org tag ---------------------------------------------------------
    #------------------------------- Functions for Family tag ---------------------------------------------------------  
    #------------------------------- Functions for OS tag ---------------------------------------------------------        
    #------------------------------- Functions for Version tag ---------------------------------------------------------
    #------------------------------- Functions for Other tag ---------------------------------------------------------
    #------------------------------- Functions for Price tag ---------------------------------------------------------  
    #------------------------------- Functions for Size tag ---------------------------------------------------------  
    #------------------------------- Functions for Feature tag ---------------------------------------------------------  

if __name__ == "__main__":
    pass
