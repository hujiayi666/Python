import subprocess
import sys


def generate_qr_code():
    print("Generating QR code for QQBot login...")
    proc = subprocess.Popen([sys.executable, '-m', 'qqbot', '-u', 'none', '--qq', '1706373392'], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    while proc.poll() is None:
        line = proc.stdout.readline()
        if line:
            print(line.decode().strip())
        err = proc.stderr.readline()
        if err:
            print(err.decode().strip())

    proc.wait()
    print("QQBot登录已完成。")


if __name__ == "__main__":
    generate_qr_code()
