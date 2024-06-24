from langchain_core.language_models import BaseLanguageModel
from prompt import GEN_SQL_PROMPT, ANSWER_PROMPT
from langchain_core.output_parsers import StrOutputParser
import re
from sql_database import ISQLDatabase


# 审批助手
class ApprovalAssistant:
    def __init__(self, llm: BaseLanguageModel, db: ISQLDatabase):
        self.llm = llm
        self.db = db
        self.gen_sql_chain = self._create_chain(GEN_SQL_PROMPT)
        self.table_info = self.db.get_table_info()
        self.answer_chain = self._create_chain(ANSWER_PROMPT)

    def _create_chain(self, prompt):
        return prompt | self.llm | StrOutputParser()

    @staticmethod
    def extract_code(txt: str) -> str:
        code_block_pattern = r'```sql(.*?)```'
        code_blocks = re.findall(code_block_pattern, txt, re.DOTALL)
        if code_blocks:
            return code_blocks[0]
        else:
            return ""

    def chat(self, question: str, history: str = "") -> str:
        answer = self.gen_sql_chain.invoke(
            {
                "question": question,
                "chat_history": history,
                "table_info": self.table_info,
                "top_k": 10,
            }
        )

        # 提取sql
        sql_str = self.extract_code(answer)
        if not sql_str:
            return answer
        print(sql_str)
        # 执行sql
        try:
            result = self.db.run(sql_str)
        except Exception as e:
            print(e)
            return "这个问题我还不太明白，你可以描述的更多一点。"

        # 解析执行sql的的结果返回，这里可以用大模型去解析
        answer = self.answer_chain.invoke(
            {
                "question": question,
                "query_sql": sql_str,
                "table_info": self.table_info,
                "query_result": result,
            }
        )

        return answer
