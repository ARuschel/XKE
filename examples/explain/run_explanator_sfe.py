import os
import pandas as pd
import numpy as np
from explain.pipeline import pipeline, process_overall_metrics_wo_emb
from explain.helpers import get_dirs
from tools import train_test


emb_import_paths = [
    "/home/andrey/proj/XKEc/benchmarks/NELL186" #,
#    "/home/arthurcgusmao/Projects/xkbc/algorithms/OpenKE/benchmarks/NELL186/",
]
overalls_output_path = "Exploratory_phase_overalls.tsv"

# Call special functions when running SFE for a dataset (and not to explain an Embedding Model)
for path in emb_import_paths:
    pipeline(path, adapt_run_sfe_wo_emb=True)

metrics_dicts = process_overall_metrics_wo_emb(emb_import_paths)

exists = os.path.isfile(overalls_output_path)
if exists:
    df = pd.read_csv(overalls_output_path, sep='\t')
    df = df.append(pd.DataFrame(metrics_dicts))
    df.to_csv(overalls_output_path, sep='\t')
else:
    pd.DataFrame(metrics_dicts).to_csv(overalls_output_path, sep='\t')
