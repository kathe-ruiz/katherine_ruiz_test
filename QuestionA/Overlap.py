class Overlap:
    line1 = []
    line2 = []

    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2

    def is_iverlap(self):
        if self.validate_input():
            """
            check if lines are separated
            """
            if (
                self.line1[0] < self.line2[0]
                and self.line1[1] < self.line2[0]
                and self.line1[0] < self.line2[1]
                and self.line1[1] < self.line2[1]
            ):
                return False
            if (
                self.line1[0] > self.line2[1]
                and self.line1[1] > self.line2[1]
                and self.line1[0] > self.line2[0]
                and self.line1[1] > self.line2[0]
            ):
                return False
        else:
            return False
        return True

    def validate_input(self):
        if len(self.line1) != 2 or len(self.line2) != 2:
            print("Wrong Inpunt: lines has to be sizes of 2")
            return False
        return True


def main():
    try:
        print("please text x1:")
        x1 = int(input())
        print("please text x2:")
        x2 = int(input())
        print("please text x3:")
        x3 = int(input())
        print("please text x4:")
        x4 = int(input())
        line1 = [x1, x2]
        line2 = [x3, x4]
        overlap = Overlap(line1, line2)
        result = "Overlap" if overlap.is_iverlap() else "not Overlap"
        print("Lines are", result)

    except ValueError:
        print("Wrong input: input has to be an Integer")


if __name__ == "__main__":
    main()
