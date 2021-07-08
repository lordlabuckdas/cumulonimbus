import argparse
from dcol import DCol


def main():
    ap = argparse.ArgumentParser(description="CLI testing tool for the dcol API")
    ap.add_argument("-t", "--target", help="IP address of the target")
    args = ap.parse_args()
    collector = DCol(args.target)
    try:
        collector.run()
    except Exception as err:
        print(err)
    finally:
        collector.close()


if __name__ == "__main__":
    main()
