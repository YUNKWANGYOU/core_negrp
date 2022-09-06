import plotly.graph_objects as go
import networkx as nx


class NetworkGraphHandler() :
    
    def __init__(self):
        self.G = nx.random_geometric_graph(200, 0.125)
        self.edge_x = []
        self.edge_y = []
        self.node_x = []
        self.node_y = []
        self.node_adjacencies = []
        self.node_text = []
        
    def generate_edges(self): 
        for edge in self.G.edges():
            x0, y0 = self.G.nodes[edge[0]]['pos']
            x1, y1 = self.G.nodes[edge[1]]['pos']
            self.edge_x.append(x0)
            self.edge_x.append(x1)
            self.edge_x.append(None)
            self.edge_y.append(y0)
            self.edge_y.append(y1)
            self.edge_y.append(None)
    def trace_edges(self):
        self.edge_trace = go.Scatter(
            x=self.edge_x, y=self.edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')

    def generate_nodes(self):
        for node in self.G.nodes():
            x, y = self.G.nodes[node]['pos']
            self.node_x.append(x)
            self.node_y.append(y)

    def trace_nodes(self):
        self.node_trace = go.Scatter(
            x=self.node_x, y=self.node_y,
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                # colorscale options
                #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                colorscale='YlGnBu',
                reversescale=True,
                color=[],
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line_width=2))

    def make_connection(self):
        for node, adjacencies in enumerate(self.G.adjacency()):
            self.node_adjacencies.append(len(adjacencies[1]))
            self.node_text.append('# of connections: '+str(len(adjacencies[1])))

        self.node_trace.marker.color = self.node_adjacencies
        self.node_trace.text = self.node_text

    def make_figure(self) :
        self.fig = go.Figure(data=[self.edge_trace, self.node_trace],
                    layout=go.Layout(
                        title='<br>Network graph made with Python',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20,l=5,r=5,t=40),
                        annotations=[ dict(
                            text="Network",
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002 ) ],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                        )
        
        
if __name__ == "__main__" :
    negrp = NetworkGraphHandler()
    negrp.generate_edges()
    negrp.trace_edges()
    negrp.generate_nodes()
    negrp.trace_nodes()
    negrp.make_connection()
    negrp.make_figure()
    negrp.fig.show()