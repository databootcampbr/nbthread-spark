NBThread Spark
##############

Spark multithread in IPython Notebooks.

It's now simple to execute Spark Structured Streaming in Jupyter Notebooks

Install
=======

.. code:: shell

    pip install nbthread_spark --process-dependency-links

Usage
=====

Given a Socket Stream:

.. code:: python

    TCP_IP = "localhost"
    TCP_PORT = 9005

    from pyspark.sql.functions import from_json
    from pyspark.sql import SparkSession
    from pyspark.sql.types import StructField, StructType, IntegerType

    schema = StructType([
        StructField("bip", IntegerType(), True),
        StructField("is_on", IntegerType(), True)
    ])

    spark = SparkSession \
        .builder \
        .appName("IOTStreamApp") \
        .getOrCreate()

    iot_stream = spark \
        .readStream \
        .format("socket") \
        .option("host", TCP_IP) \
        .option("port", TCP_PORT) \
        .load()

    iot_expanded = iot_stream.withColumn('value_json', 
                                        from_json('value', schema)
                                        ).drop('value').select('value_json.*')

    query = iot_expanded \
        .writeStream \
        .outputMode("update") \
        .format("memory") \
        .queryName("iot_table") \
        .start()

You can run queries using this:

.. code:: python

    from nbthread_spark.stream import StreamRunner

    runner = StreamRunner(query)
    
    runner.controls()
    ## you will see buttons ;)

    runner.start() # start without controls

    runner.status() # show stream status

    runner.stop() # stop streaming and thread

For Stream Manager you can control lot of streams in a easy way:

.. code:: python

    from nbthread_spark.manager import StreamManager

    sm = StreamManager()

    sm.append(runner)
    sm.append(runner1)
    sm.append(runner2)

    sm.all_controls()
    ## you will see all buttons from streams ;)

    sm.start_all() # start all streams

    sm.stop_all() # stop all streams

Special Thanks
==============

Here_ the list of students that contribute with this module.

.. _Here: https://github.com/databootcampbr/nbthread-spark/blob/master/CONTRIBUTORS.md    