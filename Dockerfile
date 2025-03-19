FROM odoo:18.0

USER root

# Install git, vim, and other useful development tools
RUN apt-get update && apt-get install -y \
    git \
    vim \
    python3-pip \
    && pip3 install --break-system-packages black \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Make sure the PATH includes the location where pip installs packages
ENV PATH="$PATH:/usr/local/bin"