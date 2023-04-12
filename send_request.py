import argparse
import logging
import os
from simple_cog_client import client_factory


logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description="Client for the server")
parser.add_argument(
    "--url",
    type=str,
    default="http://localhost:8080/predictions",
    help="URL of the server",
)
parser.add_argument(
    "-i",
    "--input",
    type=str,
    help="A pair name=value for each input",
    action="append",
    default=[],
)
parser.add_argument(
    "-d",
    "--save-dir",
    type=str,
    default=".",
    help="Directory to save the output images",
)

args = parser.parse_args()

client = client_factory(args.url)
response = client(args.input)

for name, value in response.items():
    if name == "image":
        original_img_path = [
            pair.split("=")[1]
            for pair in args.input
            if pair.startswith("image=")
        ][0]
        original_img_name = os.path.basename(original_img_path).split(".")[0]
        
        new_img_path = os.path.join(args.save_dir, 'processed-'+original_img_name+".png")
        value.save(new_img_path)
        
