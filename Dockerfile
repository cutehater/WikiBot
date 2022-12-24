FROM python:3.10

RUN pip install aiohttp && pip install wikipedia && pip install aiogram

COPY ./main.py ./
CMD ["python", "./main.py"]