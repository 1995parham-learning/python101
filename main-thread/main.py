import os
import threading

print(f"python process running with process id: {os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"python is currently running {total_threads} thread(s)")
print(f"the current thread is {thread_name}")
