class Memm(object):
    def __init__(self): 
        print "MEMM"
        return


    def viterbi(tagset, sentence, maxent_clf):
	pi = dict()
	bp = dict()
	u
	pi[(0, '*', '*')] = 1

	final_u = ""
        final_v = ""

	for k in range(1, len(sentence)+1):
            for u in tagset:
		for v in tagset:
	    	    prods = {}
		    max_prod = 0
		    for t in tagset:
			prod = pi[(k-1, t, u)] * clf.p_y_given_x((t, u, sentence, k), v)
		    	if(prod > max_prod):
				max_prod = prod
				bp[(k ,u, v)] = t
				pi[(k ,u, v)] = max_prod
				final_u = u
				final_v = v


	
	finaltags = {}
	finaltags[len(sentence)] = final_v
	finaltags[len(sentence) - 1] = final_u

	for k in range(len(sentence)-2, 1, -1):
		finaltags[k] = bp[(k+2, finaltags[k+1], finaltags[k+2])]

	print finaltags

