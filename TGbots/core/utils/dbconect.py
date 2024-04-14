import asyncpg.pool

class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, user_nickname, user_name, user_mail, user_phone):
        query = f"INSERT INTO Testbot (user_id, user_nickname, user_name, user_mail, user_number) VALUES ({user_id}, '{user_nickname}', '{user_name}', '{user_mail}', '{user_phone}') ON CONFLICT (user_id) DO UPDATE SET user_name='{user_name}'"
        await self.connector.execute(query)