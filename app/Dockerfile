FROM python:3.10

# Update Linux and upgrade pip in one layer
RUN apt-get update && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip

#set working directory to /app level
WORKDIR /app

# COPY contents
COPY . . 

#install packages
RUN pip install -r requirements.txt

#Expose port 8501
EXPOSE 8501

#set environment variables for streamlit
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# HEALTHCHECK instruction tells Docker how to test a container check whether still working
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

#run app in Streamlit
ENTRYPOINT ["streamlit", "run", "home_page.py", "--server.port=8501", "--server.address=0.0.0.0"]