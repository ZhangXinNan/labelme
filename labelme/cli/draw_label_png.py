import argparse
<<<<<<< HEAD
import logging

=======

import imgviz
>>>>>>> upstream/master
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image

<<<<<<< HEAD
from labelme import utils


def main():
    logger = logging.Logger('labelme')
    logger.setLevel(logging.INFO)

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('label_png', help='label PNG file')
=======
from labelme.logger import logger


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("label_png", help="label PNG file")
>>>>>>> upstream/master
    args = parser.parse_args()

    lbl = np.asarray(PIL.Image.open(args.label_png))

<<<<<<< HEAD
    logger.info('label shape: {}'.format(lbl.shape))
    logger.info('unique label values: {}'.format(np.unique(lbl)))

    lbl_viz = utils.draw_label(lbl)
=======
    logger.info("label shape: {}".format(lbl.shape))
    logger.info("unique label values: {}".format(np.unique(lbl)))

    lbl_viz = imgviz.label2rgb(lbl)
>>>>>>> upstream/master
    plt.imshow(lbl_viz)
    plt.show()


<<<<<<< HEAD
if __name__ == '__main__':
=======
if __name__ == "__main__":
>>>>>>> upstream/master
    main()
