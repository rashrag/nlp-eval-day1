import random
import json

def history():
	f = open("all_data.json","r")
	data = json.loads(f.read())['root']
	print (type(data))
	print (len(data))
	for i in range(len(data)):
                print(data[0])
                break
	'''
	sentences = []
	for i in range(1531):
		sentences.append([])
	
	count = 0
	for i in data:
		for j in data[i]:
			for k in j["data"]:
				print k["sentence"]
				count += 1
				#print count
				list1 = []
				list2 = []
				for l in k["sentence"].split(" "):
					list1.append(l)
					#print type(k["updates"])
					for q in k["updates"]:
						if q["word"]== l:
							#print l
							m = q["tag"]
					list2.append(m)
				#print list2
				print sentences[count]
				print(count)
				print "------------"
				#sentences[count].append([list1,list2])
				sentences[count].append(list1)
				sentences[count].append(list2)
	
	print(sentences[1:])
	#a = [[["other","org","family","other"],["Hello","Samsung","Galaxy","!"]],[["other","other","family","family"],["i","bought","nexus","4"]]]
	#main_list=[]
	global main_list
	tag_list = []
	c = 0
	history = []
	sentences = sentences[1:]
	for sentence in sentences:
	    #print sentence
	    c +=len(sentence[1])
	    for i in range(len(sentence[1])):
	        if i == 0:
	            #history = []
	            history = ["*","*",sentence[0],i]
	            main_list.append(history)
	            tag_list.append(sentence[1][i])
	            #print (history)
	        elif i == 1:
	            #history = []
	            history =["*",sentence[1][i-1],sentence[0],i]
	            main_list.append(history)
	            tag_list.append(sentence[1][i])
	            #print (history)
	        else:
	            #history = []
	            history = [sentence[1][i-2],sentence[1][i-1],sentence[0],i]
	            main_list.append(history)
	            tag_list.append(sentence[1][i])
	print(len(main_list))
	#print c
	print("^^^")
	
#print(main_list)
#print(len(sentences))
#print(tag_list)

def feature1(history,tag):
        if history[1]=="Org":
                if tag=="Family":
                        return 1
	return 0
def feature2(history,tag):
        if history[0]=="Org":
                if history[1]=="Family":
                        if tag=="Family":
                                return 1
	return 0
def feature3(history,tag):
        if history[0]=="*":
                if history[1]=="*":
                        if tag=="Other":
                                return 1
	return 0
def feature4(history,tag):
        if history[0]=="*":
                if history[1]=="Other":
                        if tag=="Org":
                                return 1
	return 0
def feature5(history,tag):
        if history[0]=="Org":
                if history[1]=="Family":
                        if tag=="Other":
                                return 1
	return 0


#print len(main_list)
#print len(tag_list)
def create_data(main_list, tag_list):
	features = {}
	for i in main_list:
		for j in tag_list:
			vector_list= []
			one = feature1(i,j)
			vector_list.append(one)
			two = feature2(i,j)
			vector_list.append(two)
			three = feature3(i,j)
			vector_list.append(three)
			four = feature4(i,j)
			vector_list.append(four)
			five = feature5(i,j)
			vector_list.append(five)
			#print(vector_list)
			i[2] = tuple(i[2])
			hist = tuple(i)
			key = (hist,j)
			print type(key)
			print key
			features[key] = []
			features[key] = vector_list
		#print features
	return features


def random_fifty():
	global main_list
	num_list = random.sample(range(0,len(main_list)),50)
	new_list = []
	for i in num_list:
		new_list.append(main_list[i])
		
	return new_list

	'''		
global main_list
main_list = []		
tags = ["Other","Family","Org"]
history()
#condensed = random_fifty()
#print len(condensed)
#feature_dict = create_data(condensed, tags)
