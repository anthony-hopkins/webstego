FROM ahop1983/stego-toolkit-updated:latest

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update

WORKDIR /opt/webstego/
COPY ./templates templates
COPY ./static static
COPY ./main.py main.py
COPY ./Dockerfile Dockerfile
ENTRYPOINT ["python"]
CMD ["main.py"]
