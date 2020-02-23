import itertools


class CompareVersions:
    version1 = ""
    version2 = ""
    version1_string = ""
    version2_string = ""

    def __init__(self, version1, version2):
        self.version1 = version1.split(".")
        self.version2 = version2.split(".")
        self.version1_string = version1
        self.version2_string = version2

    def compare_version(self):
        loop = itertools.zip_longest(self.version1, self.version2)
        size_loop = len(self.version1)
        if self.version2 > self.version1:
            size_loop = len(self.version2)
        for index, items in enumerate(loop):
            item1 = int(items[0]) if items[0] is not None else None
            item2 = int(items[1]) if items[1] is not None else None
            if item1 and item2:
                if item1 > item2:
                    return 1
                elif item1 < item2:
                    return -1
                elif item1 == item2 and index + 1 == size_loop:
                    return 0
            elif item1 is not None and item1 > 0:
                return 1
            elif item2 is not None and item2 > 0:
                return -1
        return 0

    def print_result(self, result):
        if result > 0:
            return "version 1: {} is greater than version 2: {}".format(
                self.version1_string, self.version2_string
            )
        elif result < 0:
            return "version 1: {} is less than version 2: {}".format(
                self.version1_string, self.version2_string
            )
        else:
            return "version 1: {} is equal than version 2: {}".format(
                self.version1_string, self.version2_string
            )


def main():

    version1 = input("please text version 1\n")
    version2 = input("please text version 2\n")
    compare_versions = CompareVersions(version1, version2)
    try:
        result = compare_versions.compare_version()
        print(compare_versions.print_result(result))
    except ValueError:
        print("Wrong input")


if __name__ == "__main__":
    main()
