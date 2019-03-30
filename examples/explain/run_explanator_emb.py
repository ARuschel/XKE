import os
import pandas as pd
import numpy as np
from explain.pipeline import pipeline, process_overall_metrics
from explain.helpers import get_dirs
from tools import train_test


emb_import_paths = [
#     "/home/arthurcgusmao/Projects/xkbc/algorithms/OpenKE/results/WN11/TransE/1527008113",
#    "/home/arthurcgusmao/Projects/xkbc/algorithms/OpenKE/results/FB13/TransE/1527033688",
    "/home/andrey/proj/XKEc/results/NELL186/Analogy/1526567410_sfe_ar",
]
overalls_output_path = "Exploratory_phase_overalls.tsv"


for path in emb_import_paths:
    pipeline(path)

metrics_dicts = process_overall_metrics(emb_import_paths)

exists = os.path.isfile(overalls_output_path)
if exists:
    df = pd.read_csv(overalls_output_path, sep='\t')
    df = df.append(pd.DataFrame(metrics_dicts))
    df.to_csv(overalls_output_path, sep='\t')
else:
    pd.DataFrame(metrics_dicts).to_csv(overalls_output_path, sep='\t')
