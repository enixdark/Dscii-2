import sys
import json

count = 0.0
def read_file(files):
	scores = {} # initialize an empty dictionary
	for line in files:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	return scores# Print every (term, score) pair in the dictionary

def json_read(files):
	data = []
	for line in files:
		try:
			df = json.loads(line)[u'text']
			data.append(df)
		except:
			pass
	return data
	
def process(tweet):
	global count
	data = {}
	for line in tweet:
		for w in line.split():
			w = w.strip("""!@#$%^&*., "'""").encode('utf-8').lower()
			if w!="":
				if data.has_key(w):
					data[w] += 1
				else:
					data[w] = 1
					count +=1
	return data

				
	 
def main():
	global count
	#sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[1])
	#data_sent_file = read_file(sent_file)
	data_json = json_read(tweet_file)
	data = process(data_json)
	for _d in data.keys():
		_calulator = float(data[_d]/count)
		print _d,str(round(_calulator,5))
	#tweet_file.close()
	
	

if __name__ == '__main__':
   main()
