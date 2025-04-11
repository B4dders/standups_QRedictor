import os
import sys
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd
from pandas import DataFrame

if getattr(sys, "frozen", False):
    SCRIPT_DIR = Path(sys.executable).parent
    OUTPUT_DIR = SCRIPT_DIR / "standup_log"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
else:
    SCRIPT_DIR = Path(__file__).parent

TRACKER = SCRIPT_DIR / "tracker.xlsx"


def create_dataframe(filepath: str) -> DataFrame:
    return pd.read_excel(filepath, header=0)


@dataclass
class Participator:
    name: str
    nominations: dict = field(default_factory=dict)
    nominated: dict = field(default_factory=dict)
    next_likely_pos: dict = field(default_factory=dict)
    next_likely_picks: dict = field(default_factory=dict)
    separator_bias: float = field(default_factory=float)


STANDUPS = create_dataframe(TRACKER)
