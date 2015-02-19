import os, codecs
from app import app
import nltk
from nltk.tokenize import RegexpTokenizer

__WORD_CNT_TO_RETURN = 50

def process_file(filename):
	with codecs.open('app/static/top1000.txt', 'rb', 'utf-8') as f:
		top1000 = f.read().split(',')

	with codecs.open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb', 'utf-8') as f:
		raw = f.read()
	
	#nltk.download('punkt')
	# tokens = nltk.word_tokenize(raw)
	# text = nltk.Text(tokens)

	# vocabulary = nltk.FreqDist(text)

	# with open(os.path.join(app.config['RESULT_FOLDER'], filename), 'wb') as f:
	# 	f.write('\n'.join([pair[0] for pair in vocabulary.most_common(50) if len(pair[0])>2]))

	# most_commons = vocabulary.most_common(50) # >> [('word', frequency), ('word', frequency), ... ]

	# return most_commons
	# return filename


	tokenizer = RegexpTokenizer(r'\w+-\w+|\w+')
	tokens = tokenizer.tokenize(raw)
	text = nltk.Text(tokens)

	lowered_text = [w.lower() for w in text]

	extract = [w for w in lowered_text if w not in top1000 and len(w)>1]

	vocabulary = nltk.FreqDist(extract)
	with open(os.path.join(app.config['RESULT_FOLDER'], filename), 'wb') as f:
		f.write('\n'.join([pair[0] for pair in vocabulary.most_common(__WORD_CNT_TO_RETURN) if len(pair[0])>1]))

	most_commons = vocabulary.most_common(__WORD_CNT_TO_RETURN) # >> [('word', frequency), ('word', frequency), ... ]

	return most_commons