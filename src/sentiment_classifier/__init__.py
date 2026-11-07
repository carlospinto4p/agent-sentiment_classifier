"""A sentiment classifier built with agents7.

`CONFIG_PATH` is what the package's `agents7.agents` entry point names,
so a tool that lists installed agents (such as `agents7-ui`) finds the
config without knowing where the package was installed.
"""

from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.yml"
GOLDEN_SET_PATH = Path(__file__).parent / "data" / "golden_set.jsonl"
