import time
from storage import save_session

def start_tracking():
    task = input("Ce lucrezi acum? ")
    print("Tracking pornit... Apasă CTRL+C ca să oprești.")

    start_time = time.time()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        end_time = time.time()
        duration = round((end_time - start_time) / 60, 2)
        save_session(task, duration)
        print(f"\n⏱️ Task '{task}' salvat: {duration} minute")
