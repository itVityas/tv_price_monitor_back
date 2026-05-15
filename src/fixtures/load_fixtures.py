import json
from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from service.security import hash_password
from model.user import User


class FixtureLoad:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def load_users(self, fixture_file: Path):
        if not fixture_file.exists():
            raise FileNotFoundError(f"Fixture file {fixture_file} not found")
        with open(fixture_file, 'r') as file:
            fixture_data = json.load(file)

        for line in fixture_data:
            username = line.get('username')
            password = line.get('password')
            is_active = line.get('is_active')
            is_admin = line.get('is_admin')

            result = await self.session.execute(select(User).where(User.username == username))
            existing_user = result.scalar_one_or_none()

            if not existing_user:
                new_user = User(
                    username=username,
                    password=hash_password(password),
                    is_active=is_active,
                    is_admin=is_admin
                )
                self.session.add(new_user)
                await self.session.commit()

    async def load_all_fixtures(self, fixtures_dir: Path):
        fixtures_files = fixtures_dir.glob('*.json')
        for fixture_file in fixtures_files:
            if 'user' in fixture_file.name:
                await self.load_users(fixture_file)
