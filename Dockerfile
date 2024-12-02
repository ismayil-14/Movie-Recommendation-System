FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
EXPOSE 8501

CMD ["sh", "-c", "flask run --port=5000 & streamlit run s_app.py --server.port 8501"]
