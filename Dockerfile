FROM odoo:18.0

USER root

# Install git and other useful development tools
RUN apt-get update && apt-get install -y \
    git \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 