from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(
        description=
        'Clone repository and check naming convention '
        'for multiple-word identifiers.'
    )

    subparsers = parser.add_subparsers(help='sub-command help')

    parser_freq = subparsers.add_parser('freq', help='Find frequency for part of speech')
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
        '-r', '--repo', default='https://github.com/django/django.git',
        help='Select repo to clone'
    )

    parser.add_argument(
        '-pl', '--plang', choices=['python'],
        default='python',
        help='programming language to parse'
    )

    return parser.parse_args()


def main():
    args = parse_args()
    print


if __name__ == '__main__':
    main()
