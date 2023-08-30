import csv


def get_dimension(file: str) -> tuple[int, int]:
    with open(file) as f:
        data = list(csv.reader(f))
        return (len(data[0]), len(data))


def vmerge(file1: str, file2: str, dst_file: str):
    cols1, _ = get_dimension(file1)
    cols2, _ = get_dimension(file2)
    cols = max(cols1, cols2)

    with open(dst_file, "w") as dst:
        writer = csv.writer(dst)

        for file, f_cols in [(file1, cols1), (file2, cols2)]:
            additional_cols = [None] * (cols - f_cols)
            with open(file, "r") as src:
                reader = csv.reader(src)
                for row in reader:
                    writer.writerow(row + additional_cols)


def hmerge(file1: str, file2: str, dst_file: str):
    cols1, rows1 = get_dimension(file1)
    cols2, rows2 = get_dimension(file2)
    rows = max(rows1, rows2)

    with open(dst_file, "w") as dst:
        writer = csv.writer(dst)

        with open(file1, "r") as src1:
            reader1 = csv.reader(src1)
            with open(file2, "r") as src2:
                reader2 = csv.reader(src2)

                for _ in range(rows):
                    row1 = next(reader1, [None] * cols1)
                    row2 = next(reader2, [None] * cols2)
                    writer.writerow(row1 + row2)
