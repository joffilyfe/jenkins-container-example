FROM python:3

WORKDIR /app

COPY . ./

CMD [ "python", "./run_tests.py" ]

