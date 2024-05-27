from uuid import UUID
import requests
import json


class DifyDataset:
    def __init__(self, endpoint: str, api_key: str):
        self.endpoint = endpoint
        self.api_key = api_key

    # 创建空的知识库
    def create_dataset(self, dataset_name) -> UUID:
        url = self.endpoint + "/v1/datasets"
        resp = requests.request(
            method="POST",
            url=url,
            headers={
                "Authorization": "Bearer {}".format(self.api_key),
            },
            json={"name": dataset_name}
        )

        if resp.status_code > 500:
            raise Exception("dataset backend request error")

        json_content = json.loads(resp.content.decode())
        if 500 > resp.status_code >= 400:
            raise Exception(json_content.get("message"))

        _id = json_content.get("id")
        return _id

        # 删除知识库

    def delete_dataset_by_id(self, dataset_id: UUID):
        pass
    # 通过文件更新知识库
