
from nbmultitask import ThreadWithLogAndControls

def run_stream_into_thread(query, thread_print):
    query.awaitTermination()

class StreamRunner():
    def __init__(self, query, name="my stream", **kwargs):
        self.query = query
        self.thread = ThreadWithLogAndControls(
            target=run_stream_into_thread,
            args=(query,),
            name=name,
            use_terminate=True,
            **kwargs
        )
    def start(self):
        self.thread.start()
    
    def stop(self):
        self.query.stop()        
        self.thread.stop()
    
    def status(self):
        return self.query.status()

    def controls(self):
        self.thread.control_panel()