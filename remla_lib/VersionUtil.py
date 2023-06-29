import json

class VersionUtil:

    version = json.load(open('src/remla_lib/version.json', 'r'))["version"]

    def get_version(self):
        return self.version
    
    def get_version_values(self):
        x1, x2, x3 = map(int, self.version.split("."))
        return x1, x2, x3

    def increment_patch(self):
        x1, x2, x3 = self.get_version_values()
        self.version = f"{x1}.{x2}.{x3+1}"
    
    def increment_minor(self):
        x1, x2, x3 = self.get_version_values()
        self.version = f"{x1}.{x2+1}.{x3}"
    
    def increment_major(self):
        x1, x2, x3 = self.get_version_values()
        self.version = f"{x1+1}.{x2}.{x3+1}"
