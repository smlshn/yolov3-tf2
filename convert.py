from absl import app, flags, logging
from absl.flags import FLAGS
import numpy as np
from yolov3_tf2.models import YoloV3, YoloV3Tiny
from yolov3_tf2.utils import load_yolov3_from_darknet

flags.DEFINE_string('weights', './data/yolov3.weights', 'path to weights file')
flags.DEFINE_string('output', './data/yolov3.h5', 'path to output')
flags.DEFINE_boolean('tiny', False, 'yolov3 or yolov3-tiny')


def main(_argv):
    if FLAGS.tiny:
        yolo = YoloV3Tiny()
        load_yolov3_tiny_from_darknet(yolo, FLAGS.weights)
    else:
        yolo = YoloV3()
        load_yolov3_from_darknet(yolo, FLAGS.weights)

    logging.info('weights loaded')

    img = np.random.random((1, 320, 320, 3)).astype(np.float32)
    o2 = yolo(img)
    logging.info('sanity check passed')

    yolo.save_weights(FLAGS.output)
    logging.info('weights saved')

if __name__ == '__main__':
    app.run(main)