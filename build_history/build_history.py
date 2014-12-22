import json
def build_history(data_list, supported_tags):
    history_list = [] # list of all histories
    sents = []
    count = 0
    expected = []
    for data in data_list: # data is the inputs entered by a given student
        data1 = data['data']
        for rec in data1:
            updates = rec['updates']
            sent = rec['sentence']
            words = []

            expected.append(updates)
            
            for i in range(len(updates)):
                words.append(updates[i]['word'])
                #------------------------------------------------------------------------------------------------
                # NOTE: below code is a temporary hack to build the MAxEnt for just 2 tags - we will change this later. we are using our own file now.
                if (updates[i]['tag'] not in supported_tags):
                    if updates[i]['tag'] == "Model":
                        updates[i]['tag'] = "Version"
                    else:
                        updates[i]['tag'] = "Other"                
                #------------------------------------------------------------------------------------------------

            sents.append(words)
            
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
    return (history_list, sents, expected)
if __name__ == "__main__":
    supported_tags_list = ["Org", "Family", "Price", "Phone", "Feature", "OS", "Version", "Other"]
    data = json.loads(open("new_all_data.json").read())['root']
    
    (history_list, sents, expected, ) = build_history(data, supported_tags_list)
    print(len(history_list), len(sents), len(expected))
