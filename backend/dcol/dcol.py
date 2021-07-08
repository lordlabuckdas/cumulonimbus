import datetime
import nmap
from pymongo import MongoClient

client = MongoClient("mongodb://db/")
systems_table = client.assets.systems


class DCol:
    def __init__(self, ip) -> None:
        self.ip = ip
        self.mac_address = None
        self.os = None
        self.domain = None
        self.workgroup = None
        self.hostname = None

    def insert(self) -> None:
        systems_table.insert_one(
            {
                "mac_address": self.mac_address,
                "os": self.os,
                "domain": self.domain,
                "workgroup": self.workgroup,
                "last_seen": datetime.datetime.now(),
                "ip_address": self.ip,
                "hostname": self.hostname,
            }
        )

    def unauth_scan(self) -> None:
        nm = nmap.PortScanner()
        nm.scan(self.ip)
        if nm[self.ip].state() != "up":
            return
        self.hostname = nm[self.ip].hostname()

    def auth_scan(self) -> None:
        pass

    def run(self) -> None:
        self.unauth_scan()
        self.auth_scan()
        self.insert()

    def close(self) -> None:
        pass
