import csv
import json
import sys
import os

def UnicodeDictReader(file, **kwargs):
    csv_reader = csv.DictReader(file, **kwargs)
    for row in csv_reader:
        yield dict([(key, unicode(value, 'utf-8')) for key, value in row.iteritems()])

def get_clean_list(data):
    clean_data = data.replace(" ", "")
    if len(clean_data):
        split_data = clean_data.split(",")
        return [x.lower() for x in split_data if x.strip() is not ""]
    else:
        return []

def get_description(desc, prereq, notes=None):
    description = desc
    if prereq:
        description = u"{0}\n\nPREREQUISITES:\n-----\n* {1}".format(
            description,
            prereq,
        )

    if notes:
        description = u"{0}\n\nNOTES:\n-----\n* {1}".format(
            description,
            notes,
        )
    return description

files = []
# if this is a directory, get all csv files in it
if os.path.isdir(sys.argv[1]):
    for file in os.listdir(sys.argv[1]):
        if not file.startswith(".") and file.endswith(".csv"):
            files.append("{0}/{1}".format(sys.argv[1], file))
else:
    files.append(sys.argv[1])

for file in files:
    if file.endswith(".csv"):

        with open(file, "rbU") as f:

            tcreader = UnicodeDictReader(f)
            cases = []
            for row in tcreader:
                case = {
                    u"name": unicode(row["Summary"]),
                    u"description": unicode(get_description(row["Description"], row["Pre-requisites"], notes=row["Notes"])),
                    u"created_by": unicode("mbarone976@gmail.com"),
                    u"tags": get_clean_list(row["Tags"]),
                    u"suites": get_clean_list(row["Labels"]),
                    u"steps": [
                        {
                            u"instruction": unicode(row["Procedure"]),
                            u"expected": unicode(row["Expected Result"])
                        }
                    ]
                }
                cases.append(case)
            result = {"cases": cases}

            with open("{0}{1}".format(file[:-4], ".json"), "w") as outfile:
                outfile.write(json.dumps(result, indent=4))
                outfile.close()
            print file + ": " + str(len(cases))


