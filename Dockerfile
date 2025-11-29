FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -y git python3 python3-pip genisoimage qemu-system-x86 qemu-utils qemu-system-common
RUN apt install -y build-essential libcairo2-dev libjpeg-turbo8-dev libpng-dev libtool-bin libossp-uuid-dev libvncserver-dev freerdp2-dev libssh2-1-dev libtelnet-dev libwebsockets-dev libpulse-dev libvorbis-dev libwebp-dev libssl-dev libpango1.0-dev libswscale-dev libavcodec-dev libavutil-dev libavformat-dev tomcat9 tomcat9-admin tomcat9-common tomcat9-user mariadb-server
RUN apt install -y nginx

WORDIR /opt
RUN git clone https://github.com/kavat/vmcloak

WORKDIR /opt/vmcloak
RUN pip install -r pip_requirements.txt
ENV PATH="${PATH}:/root/.local/bin"

WORDIR /tmp
RUN wget https://downloads.apache.org/guacamole/1.5.5/source/guacamole-server-1.5.5.tar.gz
RUN tar -xvf guacamole-server-1.5.5.tar.gz
WORKDIR /tmp/guacamole-server-1.5.5
RUN ./configure --enable-allow-freerdp-snapshots
RUN make && make install && ldconfig

WORDIR /tmp
RUN wget https://downloads.apache.org/guacamole/1.5.5/binary/guacamole-1.5.5.war
RUN mv /tmp/guacamole-1.5.5.war /var/lib/tomcat9/webapps/guacamole.war
RUN mkdir -p /etc/guacamole/{extensions,lib}

WORKDIR /tmp
RUN wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.26.tar.gz
RUN tar -xf mysql-connector-java-8.0.26.tar.gz
RUN cp mysql-connector-java-8.0.26/mysql-connector-java-8.0.26.jar /etc/guacamole/lib/
RUN wget https://downloads.apache.org/guacamole/1.5.5/binary/guacamole-auth-jdbc-1.5.5.tar.gz
RUN tar -xf guacamole-auth-jdbc-1.5.5.tar.gz
RUN mv guacamole-auth-jdbc-1.5.5/mysql/guacamole-auth-jdbc-mysql-1.5.5.jar /etc/guacamole/extensions/

RUN printf '\npassword\npassword\ny\ny\ny\ny\n' | mysql_secure_installation
COPY docker_templates/init_mariadb.sql .
RUN cat /tmp/init_mariadb.sql | mysql -u root -ppassword
RUN cat /tmp/guacamole-auth-jdbc-1.5.5/mysql/schema/*.sql | mysql -u root -ppassword guacamole_db

COPY docker_templates/guacamole.properties /etc/guacamole/guacamole.properties
COPY docker_templates/nginx-vmcloak.conf /tmp/cuckoo-web.conf /etc/nginx/sites-available/cuckoo-web.conf

EXPOSE 80
ENTRYPOINT ["/bin/bash"]
