from argparse import ArgumentParser


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
        '-o', '--format', choices=['txt', 'json', 'csv'], default='txt',
        help='Select format to output results'
    )

    parser.add_argument(
        '-f', '--file', default='stdout',
        help='Select file to output results'
    )

    parser.add_argument(
        '-r', '--repo',
        default='https://github.com/PyExplorer/habr_nouns.git',
        help='Select repo to clone'
    )

    parser.add_argument(
        '-d', '--dir',
        help='Select dict for analyze - we don\'t clone repo in this case',
        default='repos',
    )

    parser.add_argument(
        '--plang', choices=['python'],
        default='python',
        help='programming language to parse'
    )

    parser.add_argument(
        '--noclone',
        help='no clone from repo - take only from dir (-d)',
        action='store_true'
    )

    parser.add_argument(
        '--clear',
        help='clear repo after script finished',
        action='store_true'
    )
    return parser.parse_args()
