class FrontConfig:
    """前台公共配置"""

    # 登录缓存键
    frontendTokenKey = "frontend:token:"

    # 登录有效时间 (单位秒)
    token_valid_time = 7200
    # 登录续签时间 (不足以下秒数续签)
    token_renew_time = 1800

    #  免登录验证
    not_login_uri = [
        "/endpoint/index",
        "/endpoint/config",
        "/endpoint/policy",
        "/endpoint/search",
        "/endpoint/hotSearch",
        "/endpoint/decorate",
        "/endpoint/sms/send",
        "/endpoint/upload/image",

        "/endpoint/login/check",
        "/endpoint/login/codeUrl",
        "/endpoint/login/oaLogin",
        "/endpoint/login/register",
        "/endpoint/login/forgotPassword",

        "/endpoint/article/category",
        "/endpoint/article/detail",
        "/endpoint/article/list",
        "/endpoint/pc/getConfig",
        "/endpoint/pc/index",
        "/endpoint/pc/articleCenter",
        "/endpoint/pc/articleDetail",
        "/endpoint/login/getScanCode",
        "/endpoint/login/scanLogin"
    ]
