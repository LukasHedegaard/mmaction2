#!/usr/bin/env bash
cd ../
python build_rawframes.py \
    ../../data/tvseries/videos/ \
    ../../data/tvseries/rawframes/ \
    --level 1 \
    --flow-type tvl1 \
    --ext mkv \
    --task both  \
    --new-short 256

echo "Raw frames (RGB and tv-l1) Generated for train set"

cd tvseries/
