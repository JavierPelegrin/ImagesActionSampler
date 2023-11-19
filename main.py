import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

parameters = {
    "vertical":{
        "image1": {"y": 900, "x": 0, "h": 880, "w": 610},
        "image2": {"y": 900, "x": 618, "h": 880, "w": 610},
        "image3": {"y": 0, "x": 618, "h": 880, "w": 610},
        "image4": {"y": 0, "x": 0, "h": 880, "w": 610},
    },
    "horizontal":{
        "image1": {"x": 960, "y": 0, "h": 880, "w": 610},
        "image2": {"x": 960, "y": 618, "h": 880, "w": 610},
        "image3": {"x": 0, "y": 618, "h": 880, "w": 610},
        "image4": {"x": 0, "y": 0, "h": 880, "w": 610},
    }
}


def main(argv):

    img_path = argv[0]
    
    if not img_path.endswith("/"):
        img_path += "/"

    for filename in os.listdir(img_path):
        if filename.endswith(".JPG"):
            path = os.path.join(img_path, filename)
            img = cv2.imread(path)
            size = img.shape

            output_path = os.path.join(output_dir, f"{filename}.mp4")
            
            if size[0] < 1810:
                fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                video_writer = cv2.VideoWriter(output_path, fourcc, 3.75, (880,610))

                for key, values in parameters["horizontal"].items():
                    cropped = img[values["y"]: values["y"] + values["w"], values["x"]: values["x"] + values["h"]]
                    video_writer.write(cropped)
            else:
                fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                video_writer = cv2.VideoWriter(output_path, fourcc, 3.75, (610,880))


                for key, values in parameters["vertical"].items():
                    cropped = img[values["y"]: values["y"] + values["h"], values["x"]: values["x"] + values["w"]]
                    video_writer.write(cropped)

            video_writer.release()
    print("All videos created successfully.")


if __name__ == "__main__":

    output_dir = "output_videos"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if len(sys.argv) < 2:
        print("Please provide the path to the images.")
        sys.exit(1)

    main(sys.argv[1:])