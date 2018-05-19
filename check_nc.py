from argparse import ArgumentParser
from git import Repo
from git import exc
from git.util import rmtree
from os import path as os_path

from utils import get_trees
from utils import get_filenames_with_ext_in_path
from utils import get_functions_from_trees
from utils import get_vars_from_trees
from utils import get_valid_names_from_nodes
from utils import get_words_from_node_name


def parse_args():
    parser = ArgumentParser(
        description='Clone repository and check naming convention '
        'for multiple-word identifiers.'
    )

    subparsers = parser.add_subparsers(help='sub-command help')

    parser_freq = subparsers.add_parser(
        'freq',
        help='Find frequency for part of speech'
    )
    parser_freq.add_argument(
        '-p', '--pos', choices=['verbs', 'nouns'], default='verbs',
        help='Select part of speech to analyze'
    )

    parser_freq.add_argument(
        '-n', '--node', choices=['func', 'var'], default='func',
        help='Select node to search names - functions of local variables'
    )

    parser.add_argument(
        '-o', '--output', choices=['stdout', 'json', 'csv'], default='stdout',
        help='Select destination to output results'
    )

    parser.add_argument(
        '-f', '--file', default='./results.{}',
        help='Select file to output results'
    )

    parser.add_argument(
        '-r', '--repo',
        default='https://github.com/PyExplorer/habr_nouns.git',
        help='Select repo to clone'
    )

    parser.add_argument(
        '-pl', '--plang', choices=['python'],
        default='python',
        help='programming language to parse'
    )

    return parser.parse_args()


def clone_repository(repo):
    try:
        repo = Repo.clone_from(repo, os_path.join('.', 'repos'))

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


def get_top_words(words):
    return []


def create_report(words):
    return []


def output_report(report, output):
    return


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

    args = parse_args()

    repo = clone_repository(args.repo)
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
    report = create_report(top_words)
    output_report(report, args.output)
    rmtree(working_dir)


if __name__ == '__main__':
    main()
