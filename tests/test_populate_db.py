from pymongo import MongoClient

client = MongoClient()
systems_table = client.assets.systems

docs = [
    {
        "mac_address": "00:0d:83:b1:c0:8e",
        "os": "linux",
        "domain": "abc.com",
        "workgroup": "abc",
        "last_seen": "2021/06/23 12:45:23",
        "ip_address": "192.168.1.5",
        "hostname": "ubuntu-dell-xps13",
    },
    {
        "mac_address": "50:7d:83:41:b0:4e",
        "os": "linux",
        "domain": "abc.com",
        "workgroup": "pqr",
        "last_seen": "2021/06/24 12:45:23",
        "ip_address": "192.168.1.6",
        "hostname": "ubuntu-dell-xps14",
    },
    {
        "mac_address": "22:2a:03:81:d0:8c",
        "os": "linux",
        "domain": "abc.com",
        "workgroup": "abc",
        "last_seen": "2021/06/25 12:45:23",
        "ip_address": "192.168.1.7",
        "hostname": "ubuntu-dell-xps15",
    },
    {
        "mac_address": "32:39:82:a1:d0:51",
        "os": "win",
        "domain": "xyz.com",
        "workgroup": "pqr",
        "last_seen": "2021/06/26 12:45:23",
        "ip_address": "192.168.1.8",
        "hostname": "ubuntu-dell-xps16",
    },
    {
        "mac_address": "87:9d:23:51:b0:8e",
        "os": "win",
        "domain": "xyz.com",
        "workgroup": "abc",
        "last_seen": "2021/06/27 12:45:23",
        "ip_address": "192.168.1.9",
        "hostname": "ubuntu-dell-xps17",
    },
    {
        "mac_address": "16:35:73:a1:d0:4d",
        "os": "win",
        "domain": "xyz.com",
        "workgroup": "pqr",
        "last_seen": "2021/06/28 12:45:23",
        "ip_address": "192.168.1.15",
        "hostname": "ubuntu-dell-xps18",
    },
]

systems_table.insert_many(docs)
