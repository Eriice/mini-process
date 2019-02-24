flask-v3 启动 flask 和 nginx 之间的通讯

# 最小化一个 docker flask 项目

在 Docker 容器内启动 flask 项目

配置 `docker-compose.yml` 的 ports 属性实现宿主访问容器

运行以下命令行后，在浏览器访问 `localhost` 可看到打印出来的 `hello world`

``` cmd
docker-compose build
docker-compose up -d
````

总结：使用 docker 创建了 flask 项目的容器，flask 项目可通过外部浏览器访问。

注意：在生产环境中，是不允许直接使用 flask 的提供的开发服务器，这里是用作演示。
在生产环境中，是需要配置相应的生产服务器以供 flask 使用。

---- 

# 最小化一个 docker nginx 项目

在 Docker 容器内使用启动 nginx 服务器

配置 `docker-compose.yml` 的 volumes 属性实现**配置挂载**，通过浏览器访问 nginx 服务器时候可以看到 `volume/logs` 的 `access.log` 有访问日志

``` cmd
docker-compose build
docker-compose up -d
````

总结：使用 docker 创建了 nginx 项目的容器，nginx 通过**配置挂载**的方式实现了配置的变更。