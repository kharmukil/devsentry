import shutil


class DiskTool:
    def check_disk_usage(self) -> dict:
        total, used, free = shutil.disk_usage("/")

        return {
            "total_bytes": total,
            "used_bytes": used,
            "free_bytes": free,
        }
