# class FileSystem:
#     # valid file path is / with one or concatenated strings of len >= 1 lowercase english letters
#     def __init__(self):
#         self.path_val = {}

#     def createPath(self, path: str, value: int) -> bool:
#         print(f"path: {path}")
#         file_paths = path.split("/")
#         print(f"file paths {file_paths}")
#         for path in file_paths:
#             if path not in self.path_val:
#                 self.path_val[path] = value
#             else:
#                 return False
#         return True
#     def get(self, path: str) -> int:
#         return self.path_val.get(path, -1)
class FileSystem:
    def __init__(self):
        # Seed with root so that "/a" can be created.
        self.paths = {"/": -1}

    def createPath(self, path: str, value: int) -> bool:
        # 1) Can't recreate an existing path
        if path in self.paths:
            return False

        # 2) Extract parent: e.g. "/a/b" → parent "/a"
        idx = path.rfind('/')
        parent = path[:idx] if idx > 0 else "/"

        # 3) Parent must exist
        if parent not in self.paths:
            return False

        # 4) Insert and succeed
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        # Return the stored value or -1
        return self.paths.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)