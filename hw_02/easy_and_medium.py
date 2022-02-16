from pdflatex import PDFLaTeX

def generatetable(matrix):
    table = '\\begin{tabular}{ | ' + '|'.join(['l '] * len(matrix[0])) + '|}\n' + '\\hline\n' + "".join(
        list(map(lambda s: ' & '.join(s) + ' \\\\\n', matrix))) + '\\hline\n' + \
            '\\end{tabular}\n' + '\n\\includegraphics[height = 11cm]{Graph.pdf}\n'
    return table


def beginning():
    return '\\documentclass[12pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{graphicx}\n\\begin{document}\n'


def ending():
    return '\\end{document}'


def generatelatex(matrix):
    return beginning() + generatetable(matrix) + ending()


if __name__ == '__main__':
    open('artifacts/python-2.2.tex', 'w').write(generatelatex([['A', 'B', 'C', 'D', 'E', ]] * 10))
