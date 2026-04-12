import os

from dotenv import load_dotenv


load_dotenv(dotenv_path='.env')


class DatabaseConfig:
    def __init__(self):
        self.db_driver = os.getenv("DATABASE_DRIVER")
        self.db_name = os.getenv("DATABASE_NAME")
        self.db_user = os.getenv("DATABASE_USER")
        self.db_password = os.getenv("DATABASE_PASSWORD")
        self.db_host = os.getenv("DATABASE_HOST")
        self.db_port = os.getenv("DATABASE_PORT")
        self.db_pool_size = 20
        self.db_max_overflow = 40

    def get_url(self):
        return f"postgresql+{self.db_driver}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


database_config = DatabaseConfig()


class ServerConfig:
    '''
    host: str listen ip
    port: int listen port
    reload: bool reload when code changed
    '''

    def __init__(self):
        self.host = os.getenv('HOST', '0.0.0.0')
        self.port = int(os.getenv('PORT', 8000))
        self.reload = os.getenv('RELOAD', True)


server_config = ServerConfig()


class ProjectConfig:
    '''
    project_name: str project name
    project_version: str project version
    debug: bool enable debug mode
    '''

    def __init__(self):
        self.project_name = os.getenv('PROJECT_NAME', 'FastAPI')
        self.project_version = os.getenv('PROJECT_VERSION', '0.0.1')
        self.debug = os.getenv('DEBUG', False)


project_config = ProjectConfig()
