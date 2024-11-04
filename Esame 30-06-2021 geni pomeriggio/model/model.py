import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self.graph = nx.Graph()

        self._listLocalizations = []
        self._listConnectedLocalizations = []
        self._listGenes = []
        self.listTuple = []
        self.listaCoppie = []


    def getLocalization(self):
        self._listLocalizations = DAO.getAllLocalization()
        return self._listLocalizations

    def build_graph(self):

        self._nodes = DAO.getAllLocalization()
        self.graph.add_nodes_from(self._nodes)

        self._listConnectedLocalizations = DAO.getAllConnectedLocalizations()
        for tupla in self._listConnectedLocalizations:
            if tupla[0] in self._nodes and tupla[1] in self._nodes:
                self.graph.add_edge(tupla[0], tupla[1], weight=tupla[2])

    def archiAdiacenti(self):
        listaVicini = []
        for g in self._nodes:
            for vicino in self.graph.neighbors(g):
                peso = self.graph[g][vicino]["weight"]
                listaVicini.append((g, vicino, peso))
        return listaVicini

    def get_nodes(self):
        return self.graph.nodes()

    def get_edges(self):
        return list(self.graph.edges(data=True))

    def get_num_of_nodes(self):
        return self.graph.number_of_nodes()

    def get_num_of_edges(self):
        return self.graph.number_of_edges()