#!/usr/bin/python3
import subprocess


def sshpush():
    subprocess.call('git push git@github.com:boraxpr/bitesofpy.git'.split())


if __name__ == '__main__':
    sshpush()
