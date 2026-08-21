from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
PIMA_URL = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
NANIAR_BASE_URL = "https://raw.githubusercontent.com/njtierney/naniar/master/data"
NANIAR_DATASETS = ("oceanbuoys", "pedestrian", "riskfactors")
PIMA_COLUMN_NAMES = (
    "pregnancies", "glucose", "blood_pressure", "skin_thickness",
    "insulin", "bmi", "diabetes_pedigree", "age", "outcome",
)