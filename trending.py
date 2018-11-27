#!/usr/bin/python

import sys
import re
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.functions import split
from pyspark.sql.types import *
from collections import Counter
import numpy as np

reload(sys)
sys.setdefaultencoding('utf8')
spark = SparkSession \
	.builder \
	.appName("Python Spark SQL basic example") \
	.config("spark.some.config.option", "some-value") \
	.getOrCreate()
	
nonstop = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can","say", "will", "just", "don", "should", "now","que", "la", "el", "ella", "los", "en","de","por"]	
words = []
df = spark.read.json("hdfs://localhost/data/day3.txt")
df = df.toPandas()
df_text = df['text'].dropna()
list_of_words = df_text.values#findall(r"/^[a-zA-Z]+$/")
for l in list_of_words:
	#if(l):
	for word in l.split():
		if(word.lower() not in nonstop and len(word)>2 ):
			words.append(word.replace("\n","").replace(" ", ""))
top = Counter(words).most_common(10)
print(top)
			