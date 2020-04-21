from pyspark.context import SparkContext
from pyspark import SQLContext
from pyspark.sql import Row

sc = SparkContext()
sqlContext = SQLContext(sc)

l = [('Ankit',25),('Jalfaizy',22),('saurabh',20),('Bala',26)]
rdd = sc.parallelize(l)
people = rdd.map(lambda x: Row(name=x[0], age=int(x[1])))
schemaPeople = sqlContext.createDataFrame(people)
schemaPeople.show()