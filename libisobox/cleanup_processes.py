import os
import signal


def cleanup_processes(mountpoint):
    print("Killing all processes in chroot...")
    pids = [pid for pid in os.listdir("/proc") if pid.isdigit()]

    for pid in pids:
        try:
            cwd = "/proc/" + pid + "/cwd/"
            procpwd = os.path.realpath(cwd)
            if mountpoint in procpwd:
                os.kill(int(pid), signal.SIGTERM)
                print("Killed " + pid)

        except IOError:  # proc has already terminated
            continue