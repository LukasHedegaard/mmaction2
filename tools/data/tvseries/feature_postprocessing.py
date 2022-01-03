import argparse
import os
import os.path as osp

from mmcv import dump, load


def parse_args():
    parser = argparse.ArgumentParser(description="ANet Feature Prepare")
    parser.add_argument("--rgb", default="", help="rgb feature root")
    parser.add_argument("--flow", default="", help="flow feature root")
    parser.add_argument("--dest_file", default="", help="destination file name")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    rgb_feat = os.listdir(args.rgb)
    flow_feat = os.listdir(args.flow)
    assert set(rgb_feat) == set(flow_feat)

    # Format: { "vid_name": {"rgb": feat, "flow": feat} }
    all_feat = {
        name[:-4]: {  # Remove ".pkl"
            "rgb": load(osp.join(args.rgb, name)),
            "flow": load(osp.join(args.flow, name)),
        }
        for name in rgb_feat
    }

    dump(all_feat, args.dest_file)


if __name__ == "__main__":
    main()
