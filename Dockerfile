FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 这些文件很小，改了不影响大层缓存
COPY app.py .
COPY index.html .

# data.json 很大且很少变，放在最后
COPY data.json .

EXPOSE 51985

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:51985", "--timeout", "60", "app:app"]
