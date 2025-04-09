from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from src.config.settings import settings

def get_qdrant_client():
    return QdrantClient(
        url=settings.QDRANT_ENDPOINT,
        api_key=settings.QDRANT_API_KEY,
        prefer_grpc=True
    )
