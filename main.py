import pathlib
import os
from n_grams import run_n_grams
from containment import calcs

docs_path = pathlib.Path(__file__).parent / 'data'

dir = os.scandir(str(docs_path))
paths = []
for file in dir:
    if file.is_file():
        paths.append(str(docs_path) + '/' + file.name)

file_grams = run_n_grams(paths, 10)
calcs(file_grams,10)




