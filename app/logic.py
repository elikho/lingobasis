# -*- coding: utf-8 -*-

import os, codecs
from app import app
import nltk
from nltk.tokenize import RegexpTokenizer
from requests import get
import json

__WORD_CNT_TO_RETURN = 15
__YANDEX_API_KEY = 'trnsl.1.1.20150219T133029Z.d1217a4690e3926d.7896cbb6c0ca4fc88e369f8cdad31f8d39153ab2'

def process_file(filename):
	with codecs.open('app/static/top1000.txt', 'rb', 'utf-8') as f:
		top1000 = f.read().split(',')

	with codecs.open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb', 'utf-8') as f:
		raw = f.read()

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

def translate(words):
	result = {}
	for word in words:
		req = u'https://translate.yandex.net/api/v1.5/tr.json/translate?' + \
			'key=' + __YANDEX_API_KEY + \
			'&text=' + word + \
			'&lang=' + 'ru'
		resp = get(req)
		translation = json.loads(resp.text)['text'][0]#.decode('utf-8')
		result[word] = translation
	
	return (True, result) # True for Yandex Translate, else False



