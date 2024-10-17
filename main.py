import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import mysql.connector

class MyHandler(FileSystemEventHandler):
    def __init__(self, connection):
        self.connection = connection

    def on_modified(self, event):
        if not event.is_directory:
            self.log_event(event.src_path, 'modified')

    def on_created(self, event):
        if not event.is_directory:
            self.log_event(event.src_path, 'created')

    def on_deleted(self, event):
        if not event.is_directory:
            self.log_event(event.src_path, 'deleted')

    def log_event(self, file_path, event_type):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO events (event_type, file_id) 
            VALUES (%s, (SELECT id FROM files WHERE file_path = %s))
        """, (event_type, file_path))
        self.connection.commit()

if __name__ == "__main__":
    connection = mysql.connector.connect(
        host='junction.proxy.rlwy.net',
        port='51368',
        user='root',
        password='ubibqlVggPZrducxInrBIVdrlRhxGzgr',
        database='railway'
    )

    path = "media/"
    event_handler = MyHandler(connection)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    connection.close()
