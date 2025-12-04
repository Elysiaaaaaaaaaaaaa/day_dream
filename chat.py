from agents.roleplayer.doubao import DoubaoRolePlayer
import os

def main():
    name = input('请输入角色名:')
    if os.path.exists(r'./prompt_card/role/'+name+'.txt'):
        with open(r'./prompt_card/role/'+name+'.txt','r',encoding='utf-8') as f:
            role_prompt = f.read()
    else:
        print('未找到角色提示,请先按要求创建角色')
        return
    roleplayer = DoubaoRolePlayer(name,role_prompt)
    while True:
        message = input()
        ans = roleplayer.get_response(message)
        print(f'{name}:{ans}')
    
if __name__ == '__main__':
    main()
