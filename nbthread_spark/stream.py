
import time
from nbmultitask import ThreadWithLogAndControls

class StreamRunner():
    def __init__(self, query, name="my stream", **kwargs):
        self.log_thread = None
        self.log_running = True
        self.name = name
        self.query = query
        self.thread = ThreadWithLogAndControls(
            target=self.run_stream_into_thread,
            name=self.name,
            use_terminate=True,
            **kwargs
        )
        self.thread.terminate = self.stop_thread

    def stop_thread(self):
        self.query.stop()
        self.log_thread.stop()

    def stop_log(self):
        self.log_running = False

    def get_log_from_query(self, thread_print):
        while self.log_running:
            thread_print(self.status())
            time.sleep(2)

    def run_stream_into_thread(self, thread_print):
        self.log_thread = ThreadWithLogAndControls(
                target=self.get_log_from_query,
                name="%s_log" %self.name,
                use_terminate=True
            )
        self.log_thread.terminate = self.stop_log
        self.thread.log = self.log_thread.log
        self.log_thread.start()
        self.thread.watch()
        self.query.awaitTermination()

    def start(self):
        self.thread.start()
    
    def stop(self):
        self.thread.stop()
    
    def status(self):
        return self.query.status

    def controls(self):
        self.thread.control_panel()
