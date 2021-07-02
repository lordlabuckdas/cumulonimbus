import argparse
from dcol import DataCollector


def main():
    ap = argparse.ArgumentParser(description="CLI testing tool for the dcol API")
    ap.add_argument("-t", "--target", help="IP address of the target")
    ap.add_argument("-k", "--key", help="location of the ssh key")
    args = ap.parse_args()
    dcol = None
    try:
        dcol = DataCollector(args.target, args.key)
    except Exception as err:
        print(err)
    if not dcol:
        print("DataCollector cannot be initialized!")
        exit(1)


if __name__ == "__main__":
    main()
