import argparse,pathlib,logging
from prepare import PrepareData

logging.basicConfig(level=logging.INFO)
p = argparse.ArgumentParser()

p.add_argument('--input',required=True)
p.add_argument('--ids_out', required=True)
p.add_argument('--feat_out', required=True)
args = p.parse_args()

feats, ids = PrepareData(args.input).transform_dataset()
pathlib.Path(args.ids_out).parent.mkdir(parents=True, exist_ok=True)
ids.to_csv(args.ids_out, index=False, header=False)
feats.to_parquet(args.feat_out, index=False)
logging.info("PREPARED: ids=%s  feats=%s", ids.shape, feats.shape)
