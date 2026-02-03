<<<<<<< HEAD
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
=======
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
>>>>>>> d271ac02bcff173701a74d6a74264cec6e1e213f
