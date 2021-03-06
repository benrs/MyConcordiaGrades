FROM joyzoursky/python-chromedriver:3.7-alpine3.8-selenium

WORKDIR /grades

COPY . .
COPY entry.sh /entry.sh

RUN apk update && apk add bash && pip install selenium==3.8.0

ADD crontab /etc/cron.d/grades-cron
RUN chmod 0644 /etc/cron.d/grades-cron
RUN crontab /etc/cron.d/grades-cron
RUN touch /grades/cron.log

ENTRYPOINT ["/entry.sh"]
