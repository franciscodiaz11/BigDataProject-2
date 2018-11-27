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
	
keywords = ["trump", "flu","zika","diarrhea","ebola","headache","measles"]	
words = []
df = spark.read.json("hdfs://localhost/data/day1.txt")
df = df.toPandas()
df_text = df['text'].dropna()
list_of_words = df_text.values#findall(r"/^[a-zA-Z]+$/")
for l in list_of_words:
	#if(l):
	for word in l.split():
		if(word.lower() in keywords ):
			words.append(word.lower().replace("\n","").replace(" ", ""))
top = Counter(words).most_common(10)
print(top)
			