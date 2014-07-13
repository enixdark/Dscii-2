import sys
import json
def hw():
   print 'Hello, world!'

def lines(fp):
   print str(len(fp.readlines()))

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
			df = json.loads(line)['text']
			data.append(df)
		except:
			pass
	return data
	 
	 
def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	data_sent_file = read_file(sent_file)
	data_json = json_read(tweet_file)
	num = 0
	for line in data_json:
		#if num > 10:break
		num_pos = 0
		num_neg = 0
		key_none = []
		for w in line.split(" "):
			w = w.strip("""!@#$%^&*.,"'""").encode('utf-8').lower()
			if w in data_sent_file.keys():
				if data_sent_file[w] < 0:
					num_neg +=1
				elif data_sent_file[w] > 0:
					num_pos +=1
			else:
				key_none.append(w)
		for i in key_none:
			data_sent_file[i] = 0 if num_pos == num_neg else (num_pos - num_neg) / (num_pos + num_neg) * 5
			print i,data_sent_file[i]
		#num+=1
	

if __name__ == '__main__':
   main()
