import datetime
from pathlib import Path
from typing import Optional, List

from bytewax.dataflow import Dataflow
from bytewax.inputs import Input
from bytewax.outputs import Output
from pydantic import parse_obj_as

from streaming_pipeline.embeddings import EmbeddingModelSingleton


def build(
        is_batch: bool = False,
        from_datetime: Optional[datetime.datetime] = None,
        to_datetime: Optional[datetime.datetime] = None,
        model_cache_dir: Optional[Path] = None,
        debug: bool = False
) -> Dataflow:
    """
    Builds a dataflow pipeline for processing news articles.
    """

    model = EmbeddingModelSingleton(cache_dir=model_cache_dir)
    is_input_mocked = debug is True and is_batch is False

    flow = Dataflow()
    flow.input(
        "input",
        _build_input(is_batch, from_datetime, to_datetime, is_input_mocked)
    )
    flow.flat_map(lambda messages: parse_obj_as(List[NewsArticle], messages))
    if debug:
        flow.inspect(print)
    flow.map(lambda article: article.to_document())
    flow.map(lambda document: document.compute_chunk(model))
    flow.map(lambda document: document.compute_embeddings(model))
    flow.output(
        "output",
        _build_output(model, in_memory=debug)
    )
    return flow