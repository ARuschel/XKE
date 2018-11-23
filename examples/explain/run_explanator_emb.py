import os
import pandas as pd
import numpy as np
from explain.pipeline import pipeline, process_overall_metrics
from explain.helpers import get_dirs
from tools import train_test


emb_import_paths = [
#     "/home/arthurcgusmao/Projects/xkbc/algorithms/OpenKE/results/WN11/TransE/1527008113",
#    "/home/arthurcgusmao/Projects/xkbc/algorithms/OpenKE/results/FB13/TransE/1527033688",
    "/home/andrey/proj/XKEc/results/FB13/TransE/1542997124",
]
overalls_output_path = "~/Andrey_tests.tsv"


for path in emb_import_paths:
    pipeline(path)

metrics_dicts = process_overall_metrics(emb_import_paths)

pd.DataFrame(metrics_dicts).to_csv(overalls_output_path, sep='\t')
