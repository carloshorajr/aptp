from pathlib import Path


class BootService:

    @staticmethod
    def hostname():

        return Path(
            "/etc/host_hostname"
        ).read_text().strip()


    @staticmethod
    def boot_id():

        return Path(
            "/proc/sys/kernel/random/boot_id"
        ).read_text().strip()