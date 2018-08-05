FROM python:3
MAINTAINER pramodh.ayyappan92@gmail.com
COPY requirements.txt ./
COPY github_stats.py ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./github_stats.py"]
