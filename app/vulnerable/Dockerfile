FROM openjdk:8-jre
WORKDIR /app
COPY target/coordinationhub.jar app.jar
ENV DB_PASSWORD=changeme
USER root
ENTRYPOINT ["java", "-jar", "app.jar"]

