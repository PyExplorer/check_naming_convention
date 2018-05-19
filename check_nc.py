from argparse import ArgumentParser
from git import Repo
from git import exc
from os import path as os_path


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
        '-w', '--where', choices=['func', 'var'], default='func',
        help='Select place to search names - functions of local variables'
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
        default='https://github.com/PyExplorer/check_naming_convention.git',
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


def get_words(tags, params):
    return []


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

    args = parse_args()
    print(args)
    repo = clone_repository(args.repo)
    if not repo:
        exit(1)
    if not os_path.exists(repo.working_dir):
        exit(1)

    words = get_words(tags[args.pos], args.where)
    top_words = get_top_words(words)
    report = create_report(top_words)
    output_report(report, args.output)


if __name__ == '__main__':
    main()
