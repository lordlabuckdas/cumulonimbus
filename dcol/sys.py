import datetime
import json


class System:
    def __init__(self, conn, ip: str) -> None:
        self.conn = conn
        """
        sequentially run through a few commands
        either use one-liner cmds or process info in python
        """
        self.commands = {
            "linux": {
                "hostname": ["hostname", "hostnamectl", "cat /proc/sys/kernel/hostname"],
                "mac_address": "",
                "ad_info": "",
            },
            "win": {
                "hostname": "",
                "mac_address": "",
                "ad_info": "",
            },
        }
        self.ip = ip
        self.os = self.get_os()
        self.mac = self.get_mac()
        self.host = self.get_host()
        self.domain, self.workgroup = self.get_ad_info()

    def get_os(self) -> str:
        """
        run linux and win cmds and compare exit codes or errors
        """
        return ""

    def get_mac(self) -> str:
        return ""

    def get_host(self) -> str:
        return ""

    def get_ad_info(self) -> tuple:
        return ("", "")

    def __repr__(self) -> str:
        return json.dumps(
            {
                "mac_address": self.mac,
                "os": self.os,
                "ad": {"domain": self.domain, "workgroup": self.workgroup},
                "last_seen": datetime.datetime.now(),
                "ip_address": self.ip,
                "hostname": self.host,
            }
        )
