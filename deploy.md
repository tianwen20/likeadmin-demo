# 网站部署全过程
1. 服务器安装系统，建议选择：Ubuntu 20.04.6；其他版本安装宝塔有些问题
2. 安装宝塔，安装必要的插件
3. 上传代码，添加sshkey，拉取仓库
4. 使用docker部署，编写Dockerfile以及docker-compose.yml
5. 打包镜像：sudo docker build -t work/work-platform .
6. 第一次启动mysql需要执行数据库的初始化sql
docker exec -i work-mysql mysql -uroot -pwork_platform --default-character-set=utf8mb4 < db/install.sql
7. 启动容器：
cd docker/
docker stop work-platform work-redis work-mysql 
docker start work-platform work-redis work-mysql 
docker rm work-platform work-redis work-mysql 
docker-compose up -d
docker logs -f work-platform
8. 修改代码直接重启
docker stop work-platform
docker start work-platform
docker restart work-platform
docker logs -f --tail 1000 work-platform
9. 前端更新
-> /data/workspace/work_platform/docker/www/admin
-> /data/workspace/work_platform/docker/www/pc
10. 修改server的config文件，按照实际情况修改
11. 查看日志进行调试：
tail -f -n 100 ./docker/logs/run_front.log
tail -f -n 100 ./docker/logs/run_admin.log
docker exec -it work-platform  /bin/bash
12. 管理端的密码：admin/ FGcDXWSPIEru





# 可以注意避免的点
1. 在部署时，提前将mysql等的数据目录创建好