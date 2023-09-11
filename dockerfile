FROM python:slim
ENV TOKEN='our token'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]