#! /usr/bin/env python
__author__ = 'zieghailo'

import cv2
import numpy as np

def video2frames(path, skip=1, mirror=False):
    video_object = cv2.VideoCapture(path)

    index = 0
    last_mirrored = True
    while True:
        success, frame = video_object.read()
        if success:
            if index % skip == 0:
                print last_mirrored
                if mirror and last_mirrored:
                    frame = _mirror_image(frame)
                last_mirrored = not last_mirrored

                cv2.imwrite(path[:-4] + "_" + str(index) + ".jpg", frame)  # assumes that the extension is three letters long
        else:
            break

        index += 1


def _mirror_image(image):
    return np.fliplr(image)


def main():
    import argparse
    parser = argparse.ArgumentParser("Enter the filename of a video")
    parser.add_argument('filename')
    parser.add_argument('--skip', help="Only save every nth frame")
    parser.add_argument('--mirror', action='store_true', help="Flip every other image")
    args = parser.parse_args()

    if args.skip is None:
        args.skip = 1
    if args.mirror is None:
        args.mirror = False

    video2frames(args.filename, int(args.skip), bool(args.mirror))

if __name__ == "__main__":
    main()

