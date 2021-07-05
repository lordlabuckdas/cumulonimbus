import argparse
import datetime
import nmap
from pymongo import MongoClient

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

client = MongoClient("mongodb://db/")
systems_table = client.assets.systems


def scan_target(ip: str):
    # some parsing to check if subnet or single ip
    nm = nmap.PortScanner()
    nm.scan(ip)
    if nm[ip].state() != "up":
        return
    # OS detection with -O flag
    # ad domain and workgroup - script
    # mac address - use script if needed
    item = {"last_seen": datetime.datetime.now(), "hostname": nm[ip].hostname()}
    systems_table.insert_one(item)


def main():
    ap = argparse.ArgumentParser(description="CLI testing tool for the dcol API")
    ap.add_argument("-t", "--target", help="IP address of the target")
    args = ap.parse_args()
    scan_target(args.target)


if __name__ == "__main__":
    main()
