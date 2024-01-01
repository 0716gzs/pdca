# import os
# import os.path
#
#
# def tree(path, depth=0):
#     if depth == 0:
#         print(path)
#     items = os.listdir(path)
#     for item in items:
#         # 输出文件夹中的文件和子文件夹名
#         print('|    ' * depth, end='')
#         print('|----', item)
#         item = os.path.join(path, item)
#         if os.path.isdir(item):
#             # 递归遍历子目录
#             tree(item, depth + 1)
#
#
# tree(r'/Users')


import os


def tree(path):
    def tree_iter(path, prefix=''):
        path = os.path.abspath(path)
        listpath = os.listdir(path)
        for p in listpath:
            isLast = listpath.index(p) == len(listpath) - 1
            abspath = os.path.join(path, p)
            print_tree(p, prefix, isLast)
            if os.path.isdir(abspath):
                next_prefix = prefix
                next_prefix += '    ' if isLast else '|   '
                tree_iter(abspath, next_prefix)

    def print_tree(path, prefix, isLast):
        print(prefix, end='')
        print('\\-- ' if isLast else '|-- ', end='')
        print(path)

    print(path)
    tree_iter(path)


if __name__ == '__main__':
    path = input('Path?\n')
    tree(path)



