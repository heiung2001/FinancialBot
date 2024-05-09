import logging
logger = logging.getLogger(__name__)

import traceback
from pathlib import Path
from typing import Optional, Union

import numpy as np
from transformers import AutoModel, AutoTokenizer

from streaming_pipeline import constants
from streaming_pipeline.base import SingletonMeta


class EmbeddingModelSingleton(metaclass=SingletonMeta):

    def __init__(self) -> None:
        pass
