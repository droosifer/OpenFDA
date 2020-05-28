# Combining Json files into one big file.


import glob


json_files = glob.glob('files/*.json')


output_file = ['outputfile.json']


def cat_json(output_filename, input_filenames):
    with open(output_filename, "w") as outfile:
        first = True
        for infile_name in input_filenames:
            with open(infile_name) as infile:
                if first:
                    outfile.write('[')
                    first = False
                else:
                    outfile.write(',')
                outfile.write(infile.read())
        outfile.write(']')


cat_json('output_file.json', json_files)


print(json_files)
