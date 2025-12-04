import time
import json
from volcenginesdkarkruntime import Ark
import os
client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key="c96dbd1f-aeab-461c-90d6-8096b0baeecd",
)


class DoubaoRolePlayer:
    def __init__(self,rolename, role_prompt,memory_link = None):
        if memory_link is None:
            self.memory = {
                "role": rolename,
                "content": role_prompt,
                "history":[]
            }
            os.makedirs(r'./memory/'+rolename,exist_ok=True)
            json.dump(self.memory,open(r'./memory/'+rolename+'/memory.json','w'),ensure_ascii=False,indent=4)
        else:
            self.memory = json.loads(memory_link)
        self.role_prompt = role_prompt
        self.rolename = rolename
    
    def get_response(self,message):
        now_time = "当前时间"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        completion = client.responses.create(
        # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
            model="doubao-seed-1-6-251015",
            input=[
                {
                    'role':'system',
                    'content':str(self.memory)
                },
                {
                    "role":'system',
                    'content':now_time
                },
                {
                    'role':'user',
                    'content':message
                }
            ],
            thinking={"type": "disabled"},
        )
        ans = completion.output[-1].content[0].text
        self.memory['history'].append({
            'time':now_time,
            'user':message,
            f'{self.rolename}':ans
        })
        json.dump(self.memory, open(r'./memory/'+self.rolename+'/memory.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
        return ans