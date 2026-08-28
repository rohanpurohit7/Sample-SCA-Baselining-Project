FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY target/coordinationhub.jar app.jar
USER 10001
ENTRYPOINT ["java", "-jar", "app.jar"]

