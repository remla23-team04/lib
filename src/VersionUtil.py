class VersionUtil:

    version = "0.0.0"

    def get_version(self):
        return self.version

    def increment_version(self):
        x1, x2, x3 = self.version.split(".")
        self.version = x1 + "." + x2 + (int(x3) + 1)