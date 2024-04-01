FROM python:3.10-slim as worker
LABEL authors="Cy.Feng"
WORKDIR /workspace
RUN apt-get update && \
    apt-get install -y --no-install-recommends libgomp1 libgl1-mesa-glx libglib2.0-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir paddlepaddle==2.5.2 -i https://mirror.baidu.com/pypi/simple && \
    pip install --no-cache-dir -r requirements.txt
COPY main.py func.py /workspace/
EXPOSE 58337
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "58337", "--reload"]