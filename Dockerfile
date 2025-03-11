FROM ubuntu:latest
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends git ffmpeg python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
RUN pip3 install aiohttp gunicorn

# Make port available
EXPOSE 8080

# Use the run command from run_cmd.txt
CMD sh -c "$(cat run_cmd.txt)"
