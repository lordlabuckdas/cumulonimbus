import argparse

# from dcol import DataCollector


def main():
    ap = argparse.ArgumentParser(description="CLI testing tool for the dcol API")
    ap.add_argument("-t", "--target", help="IP address of the target")
    ap.add_argument("-k", "--key", help="location of the ssh key")
    # args = ap.parse_args()
    # dcol = None
    # try:
    #     dcol = DataCollector(args.target, args.key)
    # except Exception as err:
    #     print(err)
    # if not dcol:
    #     print("DataCollector cannot be initialized!")
    #     exit(1)
    # try:
    #     dcol.run()
    # except Exception as err:
    #     print(err)
    #     print("Quitting!")
    # finally:
    #     dcol.close()


"""
{
    "mac_address": self.mac,
    "os": self.os,
    "domain": self.domain,
    "workgroup": self.workgroup,
    "last_seen": datetime.datetime.now(),
    "ip_address": self.ip,
    "hostname": self.host,
}
"""

"""
self.commands = {
    "linux": {
        "hostname": ["hostname", "hostnamectl | awk '/hostname/ {print $3}'", "cat /proc/sys/kernel/hostname"],
        "mac_address": [
            "ifconfig | awk '/ether/ {print $2}' | head -n 1",
            "ip link show | awk '/ether/ {print $2}' | head -n 1",
        ],
        "ad_info": [""],
    },
    "win": {
        "hostname": [""],
        "mac_address": ["getmac"],
        "ad_info": [""],
    },
}
"""

if __name__ == "__main__":
    main()
