'''
feature_functions.py
Implements the feature generation mechanism
Author: Anantharaman Narayana Iyer
Date: 21 Nov 2014
'''
from nltk import sent_tokenize, word_tokenize
import nltk
import json
import numpy
import pickle
import datetime

from MyMaxEnt import MyMaxEnt

phones = ["phone", "phones", "smartphone", "smartphones", "mobile"]
org_list = ["Google", "Samsung", "HTC", "Sony", "Apple", "Micromax"]

class FeatureFunctions(object):    
    def __init__(self, wmap, tag_list):
        self.wmap = wmap
        self.supported_tags = tag_list
        self.flist = [self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8, self.f9, self.f10, self.f11, self.f12, self.f13]
        return
        
    
    def f1(self, h, tag):
        

    
    def f2(self, h, tag):
       

    
    def f3(self, h, tag):
        


    
    def f4(self, h, tag):
       

    
    def f5(self, h, tag):
       

    
    def f6(self, h, tag):
        

   
    def f7(self, h, tag):
        


    
    def f8(self, h, tag):
       

    
    def f9(self, h, tag):
        
   
    def f10(self, h, tag):
       

    
    def f11(self, h, tag):
        

   
    def f12(self, h, tag):
        


   
    def f13(self, h, tag):
        
        
    def evaluate(self, xi, tag):
        feats = []
        for f in self.flist:
            feats.append(int(f(xi, tag)))
        return feats

def build_history(data_list, supported_tags):
    history_list = [] # list of all histories
    words_map = {}
    count = 0
    for data in data_list: # data is the inputs entered by a given student
        data1 = data['data']
        for rec in data1:
            updates = rec['updates']
            sent = rec['sentence']
            words = []
            
            for i in range(len(updates)):
                words.append(updates[i]['word'])
                #------------------------------------------------------------------------------------------------
                # NOTE: below code is a temporary hack to build the MAxEnt for just 2 tags - we will change this later
                if (updates[i]['tag'] not in supported_tags):
                    updates[i]['tag'] = "Other"                
                #------------------------------------------------------------------------------------------------

            words_map[count] = {'words': words, 'pos_tags': nltk.pos_tag(words)}
            
            for i in range(len(updates)):
                history = {}
                history["i"] = i
                if i == 0:
                    history["ta"] = "*" # special tag
                    history["tb"] = "*" # special tag
                elif i == 1:
                    history["ta"] = "*" # special tag
                    history["tb"] = updates[i - 1]['tag']
                else:
                    history["ta"] = updates[i - 2]['tag'] 
                    history["tb"] = updates[i - 1]['tag']
                history["wn"] = count
                history_list.append((history, updates[i]['tag'], ))
            count += 1
    return (history_list, words_map)


def test(clf, history_list):
    result = []
    for history in history_list:
        mymap = wmap[history[0]["wn"]]
        words = mymap['words']
        tags = mymap['pos_tags']    
        index = history[0]["i"]
        val = clf.classify(history[0])
        result.append({'predicted': val, 'word': words[index], 'expected': history[1]})
    return result
    

if __name__ == "__main__":
    #----- REPLACE THESE PATHS FOR YOUR SYSTEM ---------------------
    json_file = r"C:\home\ananth\research\pesit\nlp\ner\all_data.json"
    pickle_file = r"C:\home\ananth\research\pesit\nlp\ner\all_data.p"
    # ----------------------------------------------------------------
    
    TRAIN = int(raw_input("Enter 1 for Train, 0 to use pickeled file:  "))
    supported_tags = ["Org", "OS", "Version", "Other"]
    
    tag_set = {"Org": 0, "Other": 1}
    dims = 9
    trg_data_x = []
    trg_data_y = []
    trg_data = {'Org': [], 'Other': []}
    data = json.loads(open(json_file).read())['root']
    print "num stu = ", len(data)
    (history_list, wmap) = build_history(data, supported_tags)
    print "After build_history"
    func_obj = FeatureFunctions(wmap, supported_tags)
    
    clf = MyMaxEnt(history_list, func_obj, reg_lambda = 0.001, pic_file = pickle_file)
    print clf.model
    if TRAIN == 1:
        clf.train()
    result = test(clf, history_list[-500:])
    for r in result:
        print r['word'], r['predicted'], r['expected']
