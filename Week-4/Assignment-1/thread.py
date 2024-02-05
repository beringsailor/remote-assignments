import threading
from time import sleep

def do_job(number):
    sleep(3)
    print(f"Job {number} finished")

# rewrite everything inside this main function and keep others untouched
def main():
    threads = []
    for i in range(5):
        thread = threading.Thread(target=do_job, args=(i,))
        threads.append(thread)

        threads[i].start()
    for thread in threads:
        thread.join()

main()

# Reminder:
# 1. You dont need to take care about the order of job execution, just make sure all jobs are
# executed and finished.
