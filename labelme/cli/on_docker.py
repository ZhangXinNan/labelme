#!/usr/bin/env python

<<<<<<< HEAD
=======
from __future__ import print_function

>>>>>>> upstream/master
import argparse
import distutils.spawn
import json
import os
import os.path as osp
import platform
import shlex
import subprocess
import sys

<<<<<<< HEAD
from labelme import logger


def get_ip():
    dist = platform.platform().split('-')[0]
    if dist == 'Linux':
        return ''
    elif dist == 'Darwin':
        cmd = 'ifconfig en0'
        output = subprocess.check_output(shlex.split(cmd))
        if str != bytes:  # Python3
            output = output.decode('utf-8')
        for row in output.splitlines():
            cols = row.strip().split(' ')
            if cols[0] == 'inet':
                ip = cols[1]
                return ip
        else:
            raise RuntimeError('No ip is found.')
    else:
        raise RuntimeError('Unsupported platform.')
=======

def get_ip():
    dist = platform.platform().split("-")[0]
    if dist == "Linux":
        return ""
    elif dist == "Darwin":
        cmd = "ifconfig en0"
        output = subprocess.check_output(shlex.split(cmd))
        if str != bytes:  # Python3
            output = output.decode("utf-8")
        for row in output.splitlines():
            cols = row.strip().split(" ")
            if cols[0] == "inet":
                ip = cols[1]
                return ip
        else:
            raise RuntimeError("No ip is found.")
    else:
        raise RuntimeError("Unsupported platform.")
>>>>>>> upstream/master


def labelme_on_docker(in_file, out_file):
    ip = get_ip()
<<<<<<< HEAD
    cmd = 'xhost + %s' % ip
=======
    cmd = "xhost + %s" % ip
>>>>>>> upstream/master
    subprocess.check_output(shlex.split(cmd))

    if out_file:
        out_file = osp.abspath(out_file)
        if osp.exists(out_file):
<<<<<<< HEAD
            raise RuntimeError('File exists: %s' % out_file)
        else:
            open(osp.abspath(out_file), 'w')

    cmd = 'docker run -it --rm' \
        ' -e DISPLAY={0}:0' \
        ' -e QT_X11_NO_MITSHM=1' \
        ' -v /tmp/.X11-unix:/tmp/.X11-unix' \
        ' -v {1}:{2}' \
        ' -w /home/developer'
    in_file_a = osp.abspath(in_file)
    in_file_b = osp.join('/home/developer', osp.basename(in_file))
=======
            raise RuntimeError("File exists: %s" % out_file)
        else:
            open(osp.abspath(out_file), "w")

    cmd = (
        "docker run -it --rm"
        " -e DISPLAY={0}:0"
        " -e QT_X11_NO_MITSHM=1"
        " -v /tmp/.X11-unix:/tmp/.X11-unix"
        " -v {1}:{2}"
        " -w /home/developer"
    )
    in_file_a = osp.abspath(in_file)
    in_file_b = osp.join("/home/developer", osp.basename(in_file))
>>>>>>> upstream/master
    cmd = cmd.format(
        ip,
        in_file_a,
        in_file_b,
    )
    if out_file:
        out_file_a = osp.abspath(out_file)
<<<<<<< HEAD
        out_file_b = osp.join('/home/developer', osp.basename(out_file))
        cmd += ' -v {0}:{1}'.format(out_file_a, out_file_b)
    cmd += ' wkentaro/labelme labelme {0}'.format(in_file_b)
    if out_file:
        cmd += ' -O {0}'.format(out_file_b)
=======
        out_file_b = osp.join("/home/developer", osp.basename(out_file))
        cmd += " -v {0}:{1}".format(out_file_a, out_file_b)
    cmd += " wkentaro/labelme labelme {0}".format(in_file_b)
    if out_file:
        cmd += " -O {0}".format(out_file_b)
>>>>>>> upstream/master
    subprocess.call(shlex.split(cmd))

    if out_file:
        try:
            json.load(open(out_file))
            return out_file
        except Exception:
<<<<<<< HEAD
            if open(out_file).read() == '':
                os.remove(out_file)
            raise RuntimeError('Annotation is cancelled.')
=======
            if open(out_file).read() == "":
                os.remove(out_file)
            raise RuntimeError("Annotation is cancelled.")
>>>>>>> upstream/master


def main():
    parser = argparse.ArgumentParser()
<<<<<<< HEAD
    parser.add_argument('in_file', help='Input file or directory.')
    parser.add_argument('-O', '--output')
    args = parser.parse_args()

    if not distutils.spawn.find_executable('docker'):
        logger.error('Please install docker.')
=======
    parser.add_argument("in_file", help="Input file or directory.")
    parser.add_argument("-O", "--output")
    args = parser.parse_args()

    if not distutils.spawn.find_executable("docker"):
        print("Please install docker", file=sys.stderr)
>>>>>>> upstream/master
        sys.exit(1)

    try:
        out_file = labelme_on_docker(args.in_file, args.output)
        if out_file:
<<<<<<< HEAD
            print('Saved to: %s' % out_file)
    except RuntimeError as e:
        sys.stderr.write(e.__str__() + '\n')
        sys.exit(1)


if __name__ == '__main__':
=======
            print("Saved to: %s" % out_file)
    except RuntimeError as e:
        sys.stderr.write(e.__str__() + "\n")
        sys.exit(1)


if __name__ == "__main__":
>>>>>>> upstream/master
    main()
