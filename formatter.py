import json
import io
import csv


def format_txt(words):
    res = "Top words ({}) / frequent".format(len(words))
    res_template = "\n {} / {}"
    for word, freq in words:
        res += res_template.format(word, freq)
    return res


def format_json(words):
    prepared_dict = dict()
    prepared_dict['stat'] = {'top_words': len(words)}
    prepared_dict['top_words'] = words
    return json.dumps(prepared_dict)


def format_csv(words):
    output = io.StringIO()
    writer = csv.writer(
        output,
        delimiter=',',
        quoting=csv.QUOTE_NONNUMERIC
    )
    writer.writerow(['word', 'frequency'])

    for row in words:
        writer.writerow(row)

    return output.getvalue()