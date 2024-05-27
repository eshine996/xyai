from utils.dify.dataset import DifyDataset
from config import settings

dd = DifyDataset(
    endpoint=settings.DIFY_DOMAIN,
    api_key=settings.DIFY_API_KEY
)

dd.create_dataset("mytest-9")
