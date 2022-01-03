# Preparing TVSeries

## Introduction

<!-- [DATASET] -->

```BibTeX
@InProceedings{geest2016online,
  author={De Geest, Roeland and Gavves, Efstratios and Ghodrati, Amir and Li, Zhenyang and Snoek, Cees and Tuytelaars, Tinne},
  title={Online Action Detection},
  booktitle={European Conference on Computer Vision (ECCV)},
  year={2016},
  pages={269--284},
}
```

For basic dataset information, please refer to the official [website](https://homes.esat.kuleuven.be/psi-archive/rdegeest/TVSeries.html).
Before we start, please make sure that current working directory is `$MMACTION2/tools/data/tvseries/`.

## Extract TVSeries features using MMAction2

### Step 1. Download Dataset and annotations
Please follow the guideline in the official website [website](https://homes.esat.kuleuven.be/psi-archive/rdegeest/TVSeries.html).

The dataset should be stored in the following format:
```
tvseries
├── videos
│   ├── 24_ep1.mkv
│   ├── 24_ep2.mkv
│   ├── ...
├── splits
│   ├── classes.txt
│   ├── GT-test.txt
│   ├── GT-train.txt
│   ├── GT-val.txt
```

### Step 2. Extract RGB and Flow

Before extracting, please refer to [install.md](/docs/install.md) for installing [denseflow](https://github.com/open-mmlab/denseflow).

Use following scripts to extract both RGB and Flow.

```shell
bash extract_frames.sh
```

The command above can generate images with new short edge 256. If you want to generate images with short edge 320 (320p), or with fix size 340x256, you can change the args `--new-short 256` to `--new-short 320` or `--new-width 340 --new-height 256`.
More details can be found in [data_preparation](/docs/data_preparation.md)



### Step 3. Extract features with finetuned ckpts

Extract RGB features
```shell
python tsn_feature_extraction.py \
  --data-prefix ../../../data/tvseries/rawframes \
  --output-prefix ../../../data/tvseries/rgb_feat \
  --modality RGB \
  --ckpt /path/to/rgb_checkpoint.pth
```
Extract Flow features
```shell
python tsn_feature_extraction.py \
  --data-prefix ../../../data/tvseries/rawframes \
  --output-prefix ../../../data/tvseries/flow_feat \
  --modality Flow \
  --ckpt /path/to/flow_checkpoint.pth
```

Concatenate features
```shell
python feature_postprocessing.py \
  --rgb ../../../data/tvseries/rgb_feat \
  --flow ../../../data/tvseries/flow_feat \
  --dest_file ../../../data/tvseries/rgbflow_features.pkl
```


### Step 4. Check Directory Structure

After the whole data pipeline for tvseries preparation,
you will get the features, videos, frames and annotation files.

In the context of the whole project (for tvseries only), the folder structure will look like:

```
mmaction2
├── mmaction
├── tools
├── configs
├── data
│   ├── tvseries
│   │   ├── videos
│   │   │   ├── 24_ep1.mkv
│   │   │   ├── ...
│   │   ├── splits
│   │   │   ├── classes.txt
│   │   │   ├── GT-test.txt
│   │   │   ├── GT-train.txt
│   │   │   ├── GT-val.txt
│   │   ├── rawframes
│   │   │   ├── 24_ep1
│   │   │   │   ├── img_00000.jpg
│   │   │   │   ├── flow_x_00000.jpg
│   │   │   │   ├── flow_y_00000.jpg
│   │   │   │   ├── ...
│   │   ├── rgb_feat
│   │   │   ├── 24_ep1.npy
│   │   │   ├── ...
│   │   ├── flow_feat
│   │   │   ├── 24_ep1.npy
│   │   │   ├── ...
│   │   ├── rgbflow_features.pkl

```
