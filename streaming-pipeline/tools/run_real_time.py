from streaming_pipeline import initialize
from streaming_pipeline.flow import build

from bytewax.dataflow import Dataflow


def build_flow(
        env_file_path: str = ".env",
        logging_config_path: str = "logging.yaml",
        model_cache_dir: str = None,
        debug: bool = False
) -> Dataflow:
    """
    Builds a Bytewax flow for real-time data processing.
    """
    initialize(logging_config_path=logging_config_path, env_file_path=env_file_path)

    flow = build(model_cache_dir=model_cache_dir, debug=debug)
    return flow
