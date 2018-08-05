FROM python:3
MAINTAINER pramodh.ayyappan92@gmail.com
COPY requirements.txt ./
COPY github_stats.py ./
CMD ["python", "./github_stats.py"]
