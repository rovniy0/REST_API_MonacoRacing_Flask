
import argparse
from report_app import print_report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", type=str)
    parser.add_argument("--driver", type=str)
    parser.add_argument('--asc', type=str)
    parser.add_argument('--desc', type=str)
    args = parser.parse_args()
    if args.files and args.desc:
        print_report(args.files, order='desc')
    elif args.files and args.driver:
        print_report(args.files, driver=' '.join(args.driver))
    else:
        print_report(args.files)


if __name__ == '__main__':
    main()
