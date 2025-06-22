import argparse, pathlib, logging, pandas as pd, datetime as dt

logging.basicConfig(level=logging.INFO)
p = argparse.ArgumentParser()
p.add_argument('--ids',    required=True)
p.add_argument('--proba',  required=True)
p.add_argument('--dst_dir', required=True)
args = p.parse_args()

ids_df   = pd.read_csv(args.ids, header=None)
proba_df = pd.read_csv(args.proba, header=None)
ids   = ids_df.iloc[:, 0]
proba = proba_df.iloc[:, 0]


submit = pd.DataFrame({'id': ids, 'prediction': proba})

ts   = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
file = pathlib.Path(args.dst_dir) / f"submission_{ts}.csv"
file.parent.mkdir(parents=True, exist_ok=True)
submit.to_csv(file, index=False)
logging.info("SUBMISSION saved → %s", file)
