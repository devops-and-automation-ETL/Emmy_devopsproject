FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

ENV API_SMHI_KEY=${API_SMHI_KEY}

CMD ["python", "app.py"]
