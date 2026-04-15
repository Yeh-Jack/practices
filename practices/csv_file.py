# --- Read CSV file
import csv

SKIP_ONE_LINE = "\n\n"

path = "./data/csv/"
maleRows = []


def extract(row, extCol):
    data = []
    for i in extCol:
        data.append(row[i])
    return data


try:
    with open(path + "Titanic.csv", encoding="UTF-8") as file:
        all = list(csv.reader(file))
        extCol = [2, 4, 7, 9]

        row = all[0]
        maleRows.append(extract(row, extCol))

        for row in all:
            if row[3] == "male" and row[10] == "Q":
                maleRows.append(extract(row, extCol))

    print(
        f"There was {len(maleRows)} male on boarded from 'QueensTown', all passengers = {len(all)-1}.",
        end=SKIP_ONE_LINE,
    )

    extractFile = path + "maleQ.csv"
    with open(extractFile, "w", encoding="UTF-8") as file:
        fw = csv.writer(file)
        # fw.writerow(all[0])
        fw.writerows(maleRows)

    print(f"Data extracted and saved to {extractFile}.", end=SKIP_ONE_LINE)

except BaseException as e:
    print(f"Failed on file operation: {e}", end=SKIP_ONE_LINE)
