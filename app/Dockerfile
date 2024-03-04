FROM python:3.10

# create and activate virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3.10 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Update Linux and upgrade pip in one layer
RUN apt-get update && \
    apt-get clean && \
    apt-get install g++ -y && \
    apt-get install gcc -y && \
    apt-get install -y default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip

#set working directory to /app level
WORKDIR /app

# COPY requirements.txt
COPY requirements.txt requirements.txt 

#install packages
RUN pip install -r requirements.txt

#COPY all contents
COPY . .

#Expose port 8501
EXPOSE 8501

#set environment variables for streamlit
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

#change user
RUN groupadd -r gaming_reader && useradd -g gaming_reader gaming_reader
#set ownership & permissions
RUN chown -R gaming_reader:gaming_reader /app
#switch user
USER gaming_reader

# HEALTHCHECK instruction tells Docker how to test a container check whether still working
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

#run app in Streamlit
ENTRYPOINT ["streamlit", "run", "home_page.py", "--server.port=8501", "--server.address=0.0.0.0"]