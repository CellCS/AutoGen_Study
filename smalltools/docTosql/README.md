
# convert excel or csv file data into mysql

## MySQL

Step 1: Pull the Docker Image for MySQL

```bash
docker pull mysql/mysql-server:latest
```

Step 2: Deploy and Start the MySQL Container

```bash
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
```
like:

```bash
docker run --name ai-mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql
```

Container shell access and viewing MySQL logs

```bash
docker exec -it ai-mysql bash
mysql -uroot -p
mysql> CREATE DATABASE study_db;
mysql> USE study_db;
```


```bash
DESCRIBE [tablename];
```

Then after db is created, later, could direct use inside docker container

```bash
$> mysql -u root -p study_db;
```


Inspect db

```bash
docker logs ai-mysql
```

```bash
docker inspect [container_name]
```

Creating database dumps

```bash
docker exec some-mysql sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > /some/path/on/your/host/all-databases.sql
```

Restoring data from dump files

```bash
docker exec -i some-mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < /some/path/on/your/host/all-databases.sql
```
