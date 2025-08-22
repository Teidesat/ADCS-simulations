import sys
import math
from datetime import datetime

# Convert date in format "DD MMM YYYY HH:MM:SS.MMM" to second passed since "01 JAN 2000 00:00:00.000"
def convertDateToSeconds(date: str, referenceDate: str = "") -> float:
    dateFormat = "%d %b %Y %H:%M:%S.%f"
    
    if referenceDate == "":
        referenceDateObject = datetime(2000, 1, 1, 0, 0, 0, 0)
    else: 
        referenceDateObject = datetime.strptime(referenceDate, dateFormat)

    dateObject = datetime.strptime(date, dateFormat)
    timeDifference = dateObject - referenceDateObject

    return timeDifference.total_seconds()


# take the csv output from GMAT and add a time column to be compatible with Matlab's format
def importGMATSimulationToMatlab(inputFilePath: str):
    with open(inputFilePath, "r") as inputFile:
        outputFilePath = inputFilePath + "_matlab.csv"
            
        with open(outputFilePath, "w") as outputFile:
            rows = []
            for row in inputFile:
                rows.append(row)

            rows[0] = "TEIDESAT.Timelapse," + rows[0]
            outputFile.write(rows[0])
            
            referenceDate = rows[1].split(',', 1)[0]

            for row in rows[1:]:
                date = row.split(',', 1)[0]
                timelapse = convertDateToSeconds(date, referenceDate)
                row = str(timelapse) + "," + row
                outputFile.write(row)



importGMATSimulationToMatlab(sys.argv[1])