import logging
logger = logging.getLogger(__name__)

from fire import Fire

from streaming_pipeline import constants, initialize
from streaming_pipeline.embeddings import EmbeddingModelSingleton
from streaming_pipeline.qdrant import build_qdrant_client


def search(query: str, 
           nn: int) -> None:
    """
    Searches for related documents to the given query string
    """
    initialize()

    client = build_qdrant_client()
    model = EmbeddingModelSingleton()

    hits = client.search(
        collection_name=constants.VECTOR_DB_OUTPUT_COLLECTION_NAME,
        query_vector=model(query, to_list=True),
        limit=nn
    )
    for hit in hits:
        logger.info(hit)


if __name__ == "__main__":
    Fire(search)
