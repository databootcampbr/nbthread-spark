
import ipywidgets as widgets

class StreamManager(list):
    
    def start_all(self):
        for stream in self:
            stream.start()
    
    def stop_all(self):
        for stream in self:
            stream.stop()
    
    def all_controls(self):
        for stream in self:
            widgets.HTML(
                value="<h3>%s</h3>" % stream.name
            )
            stream.controls()