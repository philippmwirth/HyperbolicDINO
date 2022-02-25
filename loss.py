import sys
sys.path.append('./lightly')
sys.path.append('./hyperbolic-image-embeddings')

from lightly.loss import DINOLoss
from hyptorch.nn import HyperbolicDistanceLayer


class HyperbolicDINOLoss(DINOLoss):
    """TODO: implement """


if __name__ == '__main__':
    pass # TODO: simple test
