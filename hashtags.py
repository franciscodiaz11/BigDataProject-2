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
df = spark.read.json("hdfs://localhost/data/day3.txt")

#hashtag_pattern = re.compile()

hashtags = []
df = df.toPandas()
df_text = df['text'].dropna()
list_of_hashtags = df_text.str.findall(r"(?:\s|^)#[A-Za-z0-9\-\.\_]+(?:\s|$)")
for l in list_of_hashtags:
	if(l):
		for hashtag in l:
			hashtags.append(hashtag.replace("\n","").replace(" ", ""))
top = Counter(hashtags).most_common(10)
print(top)
#unique = np.unique(hashtags, return_counts=True)
#np.sort(unique)
#print(unique[0][:10],unique[1][:10])

