import ast
from os import walk as os_walk
from os import path as os_path
from nltk import pos_tag


def get_tree(filename):
    tree = None
    with open(filename, 'r', encoding='utf-8') as opened_file:
        main_file_content = opened_file.read()
    try:
        tree = ast.parse(main_file_content)
    except SyntaxError as e:
        pass
    except Exception as e:
        pass
    return tree


def get_trees(filenames):
    trees = []
    for filename in filenames:
        tree = get_tree(filename)
        if not tree:
            continue
        trees.append(tree)

    return trees


def get_filenames_with_ext_in_path(path, ext):
    filenames = []
    for dirname, dirs, files in os_walk(path, topdown=True):
        for file in files:
            if not file.endswith(ext):
                continue
            filenames.append(os_path.join(dirname, file))
    return filenames


def get_functions_from_trees(trees):
    functions = []
    for tree in trees:
        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef):
                continue
            functions.append(node.name.lower())
    return functions


def get_vars_from_trees(trees):
    vars = []
    for tree in trees:
        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef):
                continue
            for assign in node.body:
                if not isinstance(assign, ast.Assign):
                    continue
                for target in assign.targets:
                    vars.append(target.id.lower())
    return vars


def is_node_name_valid(node):
    return not (node.startswith('__') and node.endswith('__'))


def get_valid_names_from_nodes(nodes):
    nodes_names = []
    for node in nodes:
        if is_node_name_valid(node):
            nodes_names.append(node)
    return nodes_names


def check_is_tag_with_ntlk(word, function_name, tags):
    if not word:
        return False
    checked_name = ['we']
    if tags == 'VB':
        checked_name.extend(function_name)
    pos_info = pos_tag(checked_name)
    return tags in pos_info[checked_name.index(word)][1]


def get_words_from_node_name(node_name, tags):
    words = []
    node_name_in_list = node_name.split('_')
    for word in node_name_in_list:
        if not check_is_tag_with_ntlk(word, node_name_in_list, tags):
            continue
        words.append(word)
    return words
