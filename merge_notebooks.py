import nbformat as nbf

# Change these to your notebook names
notebooks_to_merge = ["portfolio_volatility.ipynb", "Business_Analytics_Term_Project.ipynb"]

merged = nbf.v4.new_notebook()
merged.cells = []

for nb_name in notebooks_to_merge:
    nb = nbf.read(nb_name, as_version=4)
    merged.cells.extend(nb.cells)

nbf.write(merged, "Final.ipynb")
print("Created Final.ipynb")
