#!/usr/bin/python

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

usernames = []
df = df.toPandas()
df_string = df["user"].dropna()
for user in df_string:
	usernames.append(user.screen_name)
	
top = Counter(usernames).most_common(10)
print(top)