import argparse
from pathlib import Path

import pandas as pd


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='The tool to generate tfrecords file by images and meta')
    parser.add_argument('--base-image-path', required=True, help='base_img_path/an_img_name.jpg')
    parser.add_argument('--meta-path', required=True)
    parser.add_argument('--output-path', required=True)

    args = parser.parse_args()

    df = pd.read_csv(args.meta_path)
    base_image_path = Path(args.base_image_path)

    data = []

    for row in df.itertuples():
        img_path = base_image_path / row.path.replace('.json', '.jpg')
        text = row.text
        data.append(f'{img_path} {text}')

    with open(args.output_path, 'w') as f:
        f.write('\n'.join(data))
