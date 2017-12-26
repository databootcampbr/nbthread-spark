
import ipywidgets as widgets
from IPython.display import display

class StreamManager(list):
    
    def start_all(self):
        for stream in self:
            stream.start()
    
    def stop_all(self):
        for stream in self:
            stream.stop()
    
    def all_controls(self):
        for stream in self:
            display(widgets.HTML(
                value="<h3>%s</h3>" % stream.name
            ))
            stream.controls()