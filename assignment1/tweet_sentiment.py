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

	for line in data_json:
		sent = 0
		for w in line.split():
			w = w.strip("""!@#$%^&*."'""").encode('utf-8')	
			if w not in data_sent_file.keys():
				sent += data_sent_file[w]
		print "\t", sent

if __name__ == '__main__':
   main()
