from pathlib import Path
from typing import Dict
import urllib.request

import pandas as pd
import pyreadr

from .config import (
    DATA_DIR,
    NANIAR_BASE_URL,
    NANIAR_DATASETS,
    PIMA_COLUMN_NAMES,
    PIMA_URL,
)


def _download_file(url: str, destination: Path) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request) as response, destination.open("wb") as output:
        output.write(response.read())
    return destination


def load_pima_dataset(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """Download and load the Pima Indians diabetes dataset."""
    file_path = _download_file(PIMA_URL, data_dir / "pima-indians-diabetes.csv")
    return pd.read_csv(file_path, header=None, names=PIMA_COLUMN_NAMES)


def load_naniar_datasets(data_dir: Path = DATA_DIR) -> Dict[str, pd.DataFrame]:
    """Download and load the oceanbuoys, pedestrian and riskfactors datasets."""
    datasets = {}
    for dataset_name in NANIAR_DATASETS:
        file_path = _download_file(
            f"{NANIAR_BASE_URL}/{dataset_name}.rda",
            data_dir / f"{dataset_name}.rda",
        )
        datasets[dataset_name] = pyreadr.read_r(file_path)[dataset_name]
    return datasets


def load_all_datasets(data_dir: Path = DATA_DIR) -> Dict[str, pd.DataFrame]:
    """Download and load all datasets used by the notebooks."""
    datasets = load_naniar_datasets(data_dir)
    datasets["pima"] = load_pima_dataset(data_dir)
    return datasets