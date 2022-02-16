import graphviz
import ast
import inspect
from hw_01 import easy

graph = graphviz.Graph()
cnt = 0


class NodeVisitor:
    def visit(self, node):
        global cnt
        style = nodename(node)

        graph.node(str(cnt), style[0], fillcolor=style[1], shape=style[2], style='filled')
        node_cnt = cnt
        cnt += 1

        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        graph.edge(str(node_cnt), str(self.visit(item)))
            elif isinstance(value, ast.AST):
                graph.edge(str(node_cnt), str(self.visit(value)))
        return node_cnt


def nodename(node):
    name = node.__class__.__name__
    color = '#DDEDAA'
    shape = 'rectangle'
    if isinstance(node, ast.Constant):
        color = '#DDEDAA'
        shape = 'rectangle'
        name = name + ' ' + str(node.value)
    elif isinstance(node, ast.Name):
        color = '#F0CF65'
        shape = 'square'
        name = name + ' ' + str(node.id)
    elif isinstance(node, ast.arg):
        color = '#D7816A'
        shape = 'diamond'
        name = name + ' ' + str(node.arg)
    elif isinstance(node, ast.FunctionDef):
        color = '#BD4F6C'
        shape = 'octagon'
        name = name + ' ' + str(node.name)
    return (name, color, shape)


def fibonacciast():
    ast_obj = ast.parse(inspect.getsource(easy.fibonacci))
    n = NodeVisitor()
    n.visit(ast_obj)
    graph.render(directory='artifacts')


if __name__ == "main":
    fibonacciast()
