
import ipywidgets as widgets
from IPython.display import display
from pyspark.sql import SparkSession

class SparkRunner(SparkSession):

    class Builder(SparkSession.builder.__class__):

        def __init__(self):
            self.stop_button = widgets.Button(description='stop')
            self.stop_button.on_click(self.stop)
            self.stop_button.button_style = 'danger'
            self.spark = None

        def getOrCreate(self):
            self.spark = super(self.__class__, self).getOrCreate()
            display(self.stop_button)
            display(widgets.HTML(
                value="<a href='%s' target='_blank'>Spark UI</h3>" % self.spark.sparkContext.uiWebUrl
            ))
            return self.spark
        
        def stop(self, e=None):
            self.spark.stop()
    
    builder = Builder()