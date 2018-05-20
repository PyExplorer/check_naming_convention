from os import path as os_path

from git import Repo
from git import exc
from git.util import rmtree
from parser_args import parse_args

from formatter import format_csv, format_json, format_txt
from utils import (
    get_filenames_with_ext_in_path, get_functions_from_trees,
    get_top_words, get_trees, get_valid_names_from_nodes, get_vars_from_trees,
    get_words_from_node_name
)


def clone_repository(repo, dest_dir):
    try:
        repo = Repo.clone_from(repo, os_path.join('.', dest_dir))

        return repo
    except exc.GitCommandError as e:
        print(
            'Something wrong happened, {} with status {}'.format(
                e.stderr, e.status)
        )
    return


def get_words_in_path(path, tags, node_handler, ext):
    filenames = get_filenames_with_ext_in_path(path, ext)
    trees = get_trees(filenames)
    node_names = node_handler(trees)
    valid_node_names = get_valid_names_from_nodes(node_names)
    words = []
    for node_name in valid_node_names:
        words_from_node = get_words_from_node_name(node_name, tags)
        words.extend(words_from_node)
    return words


def create_report(words, handler):
    return handler(words)


def output_report(report, filename):
    if filename == 'stdout':
        print(report)
        return
    with open(filename, 'w') as f:
        f.write(report)


def main():
    tags = {
        'verbs': 'VB',
        'nouns': 'NN'
    }
    plang = {
        'python': 'py'
    }
    node_handler = {
        'func': get_functions_from_trees,
        'var': get_vars_from_trees
    }
    format_handler = {
        'txt': format_txt,
        'json': format_json,
        'csv': format_csv,
    }

    args = parse_args()
    if args.noclone:
        working_dir = os_path.join('.', args.dir)
    else:
        repo = clone_repository(args.repo, args.dir)
        if not repo:
            exit(1)
        working_dir = repo.working_dir

    if not os_path.exists(working_dir):
        exit(1)

    words = get_words_in_path(
        working_dir,
        tags[args.pos],
        node_handler[args.node],
        plang[args.plang]
    )
    top_words = get_top_words(words)
    report = create_report(top_words, format_handler[args.format])
    output_report(report, args.file.format())
    if args.clear:
        rmtree(working_dir)


if __name__ == '__main__':
    main()
