FROM joyzoursky/python-chromedriver:3.7-alpine3.8-selenium

WORKDIR /grades

COPY . .

RUN apk update && apk add bash && pip install selenium==3.8.0

ADD crontab /etc/cron.d/grades-cron
RUN chmod 0644 /etc/cron.d/grades-cron
RUN crontab /etc/cron.d/grades-cron

# Create the log file to be able to run tail
RUN touch /grades/cron.log

CMD ["crond", "-l 2", "-f"]