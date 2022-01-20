import networkx as nx

chain_end_observed = nx.DiGraph()
chain_end_observed.add_edges_from(
    [
        ("H","M"),
        ("M","Y")
    ]
)
print(nx.d_separated(chain_end_observed, {"H"}, {"Y"}, {"Y"}))


collider_parent_observed = nx.DiGraph()
collider_parent_observed.add_edges_from(
    [
        ("L","A"),
        ("J","A")
    ]
)
print(nx.d_separated(collider_parent_observed, {"L"}, {"J"}, {"L"}))

# g.add_edges_from(
#     [
#         ("A", "M"),
#         ("L", "A"),
#         ("M", "Y"),
#         ("H", "L"),
#         ("H", "M"),
#         ("J", "A"),
#         ("J", "Y"),
#         ("D", "Y"),
#         ("C", "D"),
#         ("C", "A"),
#         ("C", "L"),
#     ]
# )
#               start, end, conditioned on
# d_separated(G, A, B, Z)
# print(nx.d_separated(g, {"H"}, {"J"}, {"Y"}))
# print(nx.d_separated(g, {"H"}, {"J"}, {"L"}))
# print(nx.d_separated(g, {"A"}, {"Y"}, {"J","M","C"}))
# print(nx.d_separated(g, {"L"}, {"Y"}, {"A","M","C","D"}))

