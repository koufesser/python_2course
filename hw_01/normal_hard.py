import graphviz
import ast
import inspect
from hw_01 import easy

graph = graphviz.Graph()
cnt = 0


class NodeVisitor:
    def visit(self, node):
        global cnt
        node_name = nodename(node)
        graph.node(str(cnt), node_name)
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
    if isinstance(node, ast.Constant):
        name = name + ' ' + str(node.value)
    elif isinstance(node, ast.Name):
        name = name + ' ' + str(node.id)
    elif isinstance(node, ast.arg):
        name = name + ' ' + str(node.arg)
    elif isinstance(node, ast.FunctionDef):
        name = name + ' ' + str(node.name)
    return name


ast_obj = ast.parse(inspect.getsource(easy.fibonacci))
n = NodeVisitor()
n.visit(ast_obj)
graph.render()
