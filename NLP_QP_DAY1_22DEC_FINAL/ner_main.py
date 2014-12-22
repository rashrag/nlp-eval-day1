import cleanTags
import build_history
import feature_functions
import mymaxent

cleanTags.clean();

(history_list, sents, expected) = build_history.call(); #return is (history_list, sents, expected)

#create feature function obj call it func
func_obj = feature_functions.FeatureFunction()

maxentclf = mymaxent.MyMaxEnt(history_list,func_obj,reg_lambda=0.001);
maxentclf.train();

#change this 10
mytaglist=[]

print expected[:10]

for hist in history_list[:10]:
	tag = maxentclf.classify(hist[0]);
	mytaglist.append(tag);
print mytaglist;


