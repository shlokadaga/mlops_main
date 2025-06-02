import os
import argparse
import yaml
import logging

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="default.yaml", help="Path to config file")
    parser.add_argument("--datasource", default=None, help="Path to data source")

    args = parser.parse_args()

    print(f"Using config file: {args.config}")
    print(f"Using data source: {args.datasource}")
