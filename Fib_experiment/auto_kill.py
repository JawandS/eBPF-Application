import os, signal

THREADS = 7
counter = 0


def handler(sig, frame):
    global counter
    counter += 1
    print("Caught signal", counter)

    if counter >= THREADS:
        name = "bpftrace"
        for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
            fields = line.split()
            # extracting Process ID from the output
            pid = fields[0]
            # terminating process
            print("killing " + name + " with pid " + pid)
            # kill process
            os.kill(int(pid), signal.SIGINT)  # SIGINT is the signal for "Interrupt"

        exit(0)

while 1:
    signal.signal(signal.SIGUSR1, handler)
