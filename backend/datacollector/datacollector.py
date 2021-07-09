import datetime
import nmap
from pymongo import MongoClient

client = MongoClient("mongodb://db/")
systems_table = client.assets.systems


class DataCollector:
    def __init__(self, ip) -> None:
        self.ip = ip
        self.mac_address = None
        self.os = None
        self.domain = None
        self.workgroup = None
        self.hostname = None

        #contains all the ids inserted in the current session. Can be used for security checks
        #since we initiate connection everytime for insertion, if id.len() > 1, we can raise some exceptions
        self._ids = list()

    def insert(self) -> None:
        id = systems_table.insert_one(
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
        self._ids.append(id)

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

    #other checks can be implemented here
    def compromised(self) -> bool:
        return len(self._ids) > 0

    def close(self) -> None:
        pass
