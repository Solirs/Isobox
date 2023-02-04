import os
import signal


# This gently kills all processes whose cwd is inside the running isobox's "mountpoint"
# Basically killing every process in the chroot jail
def cleanup_processes(mountpoint):
    print("Killing all processes in chroot...")

    # List of all processes
    pids = [pid for pid in os.listdir("/proc") if pid.isdigit()]

    for pid in pids:
        try:
            cwd = "/proc/" + pid + "/cwd/"
            procpwd = os.path.realpath(cwd)
            if procpwd.startswith(mountpoint):
                os.kill(int(pid), signal.SIGTERM)
                print("Killed " + pid)

        except IOError:  # proc has already terminated
            continue
