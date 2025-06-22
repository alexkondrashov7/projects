import argparse, pathlib, logging, pandas as pd
from final_model import FinalModel

logging.basicConfig(level=logging.INFO)
p = argparse.ArgumentParser()
p.add_argument('--feat', required=True)
p.add_argument('--selector', required=True)
p.add_argument('--model', required=True)
p.add_argument('--proba_out', required=True)
args = p.parse_args()

X = pd.read_parquet(args.feat)
fm = FinalModel(args.selector, args.model)
proba = fm.predict_proba(X)

pathlib.Path(args.proba_out).parent.mkdir(parents=True, exist_ok=True)
pd.Series(proba).to_csv(args.proba_out, index=False, header=False)
logging.info("PREDICT: %d rows → %s", len(proba), args.proba_out)
