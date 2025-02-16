from functools import lru_cache
from os import path

from dotenv import load_dotenv
from pydantic import BaseSettings as Base

__all__ = ['get_settings']

ENV_FILES = ('.env', '.env.prod')
ROOT_PATH = path.dirname(path.abspath(path.join(__file__, '..')))


class BaseSettings(Base):
    """配置基类"""

    class Config:
        env_file = ENV_FILES
        env_file_encoding = 'utf-8'


class Settings(BaseSettings):
    """应用配置
        server目录为后端项目根目录, 在该目录下创建 ".env" 文件, 写入环境变量(默认大写)会自动加载, 并覆盖同名配置(小写)
            eg.
            .env 文件内写入:
                UPLOAD_DIRECTORY='/tmp/test/'
                REDIS_URL='redis://localhost:6379'
                DATABASE_URL='mysql+pymysql://work_platform:root@localhost:3306/work_platform?charset=utf8mb4'

                上述环境变量会覆盖 upload_directory 和 redis_url
    """

    # 当前域名
    domain: str = "http://localhost"
    # 上传文件路径
    upload_directory: str = "/workspace/www/uploads/"
    # 上传图片限制
    upload_image_size = 1024 * 1024 * 10
    # 上传视频限制
    upload_video_size = 1024 * 1024 * 30
    # 上传图片扩展
    upload_image_ext = {'png', 'jpg', 'jpeg', 'gif', 'ico', 'bmp'}
    # 上传视频扩展
    upload_video_ext = {'mp4', 'mp3', 'avi', 'flv', 'rmvb', 'mov'}
    # 上传路径URL前缀
    upload_prefix: str = "/uploads"

    # 数据源配置
    database_type: str = "mysql"
    database_host: str = "mysql"
    database_name: str = "work_platform"
    database_port: int = 3306
    database_user: str = "root"
    database_password: str = "work_platform"
    # 数据库连接池最小值
    database_pool_min_size = 5
    # 数据库连接池最大值
    database_pool_max_size = 20
    # 数据库连接最大空闲时间
    database_pool_recycle = 300

    # Redis源配置
    redis_host: str = "redis"
    redis_port: int = 6379
    redis_default_db: int = 0
    redis_password: str = "work_platform"

    # 是否启用静态资源
    enabled_static: bool = True
    # 静态资源URL路径
    static_path: str = "/static"
    # 静态资源本地路径
    static_directory: str = path.join(ROOT_PATH, 'static')

    # CORS 跨域资源共享
    # 允许跨域的源列表 eg. '["*"]'   '["http://localhost", "http://localhost:8080", "https://www.example.org"]'
    cors_allow_origins: str = '["*"]'

    # 模式
    mode: str = 'prod'  # dev, prod

    # 全局配置
    # 版本
    version: str = 'v1.0.0'
    # 项目根路径
    root_path: str = ROOT_PATH
    # 默认请求超时
    request_timeout: int = 100
    # Mysql表前缀
    table_prefix: str = 'la_'
    # 时区
    timezone: str = 'Asia/Shanghai'
    # 日期时间格式
    datetime_fmt: str = '%Y-%m-%d %H:%M:%S'
    # 系统加密字符
    secret: str = 'UVTIyzCy'
    # Redis键前缀
    redis_prefix: str = 'Like:'
    # 短信验证码
    redis_sms_code: str = 'smsCode:'
    # 禁止修改操作 (演示功能,限制POST请求)
    disallow_modify: bool = False
    # 短信验证码
    redisSmsCode = "smsCode:"


@lru_cache()
def get_settings() -> Settings:
    """获取并缓存应用配置"""
    # 读取server目录下的配置
    for f in ENV_FILES:
        load_dotenv(dotenv_path=path.join(ROOT_PATH, f))
    return Settings()
