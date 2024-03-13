
import argparse
import os
import cv2
import math
import numpy as np
import tqdm

parser = argparse.ArgumentParser(description='Evaluation')
parser.add_argument('--params', type=str, help='params helper.')
parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)

def main():
    args = parser.parse_args()



if __name__ == '__main__':
    main()
