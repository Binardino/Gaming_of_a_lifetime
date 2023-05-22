FROM python:3.9

#set working directory to /app level
WORKDIR /app

# COPY requirements.txt .

COPY . . 

#install packages
RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

#Expose port 8501
EXPOSE 8501

#set environment variables for streamlit
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# HEALTHCHECK instruction tells Docker how to test a container check whether still working
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

#run app in Streamlit
ENTRYPOINT ["streamlit", "run", "app/app_gaming.py", "--server.port=8501", "--server.address=0.0.0.0"]