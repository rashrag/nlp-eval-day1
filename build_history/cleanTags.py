import random
import json
def history():
    data = json.loads(open("all_data.json").read())['root'] #list of sentences
    #print(len(data))
    for i in range(len(data)):
        #print(i)
        #print(type(i))
        dataOfStudent =  data[i]['data']#per data for a student
        #print(type(dataOfStudent))
        for j in range(len(data[i]['data'])):#each sentence
            for k in range(len(data[i]['data'][j]['updates'])):
                if(data[i]['data'][j]['updates'][k]['tag'] == "Date"):
                    data[i]['data'][j]['updates'][k]['tag'] = "Other"
                elif(data[i]['data'][j]['updates'][k]['tag'] == "Model"):
                    data[i]['data'][j]['updates'][k]['tag'] = "Version"
                elif(data[i]['data'][j]['updates'][k]['tag'] == "Location"):
                    data[i]['data'][j]['updates'][k]['tag'] = "Other"
                elif(data[i]['data'][j]['updates'][k]['tag'] == "Size"):
                    data[i]['data'][j]['updates'][k]['tag'] = "Feature"
                elif(data[i]['data'][j]['updates'][k]['tag'] == "App"):
                    data[i]['data'][j]['updates'][k]['tag'] = "Other"
                #print(data[i]['data'][j]['updates'][k]['tag'])
    newDict = {}
    newDict['root'] = data;
    newJson = json.dumps(newDict);
    f = open("new_all_data.json","w");
    f.write(newJson);
history()
