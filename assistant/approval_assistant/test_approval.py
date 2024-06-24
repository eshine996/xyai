from sql_database import ISQLDatabase
from approval import ApprovalAssistant
from langchain_openai import AzureChatOpenAI

llm = AzureChatOpenAI(
    azure_endpoint="https://gpt4--0125.openai.azure.com",
    azure_deployment="gpt-4o",
    openai_api_version="2024-02-15-preview",
    openai_api_key="f28640f4bbd34db0a76fe0a3d27da5c7"
)

sql_uri = "postgresql://xyapps:Xyadm01$@10.0.40.11:32311/xyai"
db = ISQLDatabase.from_uri(sql_uri)

agent = ApprovalAssistant(
    db=db,
    llm=llm
)

history = """
Human:给我一个项目
AI:根据你提供的查询结果，以下是最后一个项目的详细信息：

| EIS_ID | 商机名称 | 部门 | 商机编号 | 立项日期 | 销售姓名 | 客户名称 | 项目类型 | 业务类型 | 预估签单日期 | 预估合同金额 | 预估毛利额 | 预估毛利率 | 立项审批状态 | 当前审批领导ID |
|--------|-----------|------|----------|-----------|----------|----------|----------|----------|--------------|--------------|------------|--------------|--------------|-----------------|
| 7887   | 2024年研学服务平台-劳动研学实践活动服务-天津市津南区葛沽实验小学 | 天津晓羊 | XY0113-20240600261 | 0001-01-01 | 杨洋凯 | 天津市津南区教育局 | 纯自有软件（买断方式） | B端商机 | 0001-01-01 | 122500.0 | 13117.257 | 12.1 | 2 | 03680745021061256 |

希望以上信息对你有帮助！如果还有其他问题，请随时提问。
"""
response = agent.chat("给我相关的利润表", history=history)
# response = agent.chat("我有多少个项目？")

print(response)
