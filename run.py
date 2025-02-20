import argparse
from FPSR.utils import RecTrainer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', '-d', type=str, default='amazon-cds', help='Name of Datasets')
    args, _ = parser.parse_known_args()

    RecTrainer(dataset=args.dataset).train(verbose=False)
