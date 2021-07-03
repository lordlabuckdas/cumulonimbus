class DataCollector:
    def __init__(self, ip: str, key: str) -> None:
        # establish connection
        self.ip = ip
        self.key = key
        self.os = None

    def run(self):
        """
        create connection
        pass it to system obj
        """
        pass

    def close(self) -> None:
        """
        close ssh connection
        and cleanup
        """
        pass
