Odoo Docker Development Environment

This repository contains a Docker Compose setup for Odoo development. It provides a containerized environment with Odoo and PostgreSQL, making it easy to develop and test Odoo modules.
Prerequisites

    Docker Desktop (with Docker Compose)
    Git (optional, for version control)

Project Structure


    odoo-docker/
    ├── docker-compose.yml
    ├── start.sh
    ├── config/
    │   └── odoo.conf
    └── addons/
        └── your_custom_modules

Quick Start

Clone this repository:

    git clone <repository-url>
    cd odoo-docker


Start the containers:

    docker-compose up -d

    Access Odoo at: http://localhost:8000

Development Configuration

The setup includes several development-friendly features:
Development Flags

In docker-compose.yml, the Odoo service uses these development flags:

    --dev=xml: Auto-reload XML changes without restart
    -u module_name: Update specific module on restart

Dont use

    -i base 
flag after first run to preserve data

Example configuration:

command: odoo -d odoo_db --dev=xml -u your_module --db_user=odoo --db_password=odoo --db_host=db

Custom Modules

Place your custom modules in the ./addons directory. They will be automatically available in Odoo.

To update your module, use:

    docker-compose restart odoo18

Database Management

    PostgreSQL runs on port 5432
    Default credentials:
        User: odoo
        Password: odoo
        Database: odoo_db

Common Operations

Restart Odoo (preserving data):

    docker-compose restart odoo18

View Logs:

    docker-compose logs -f odoo18

Clean Up

Remove containers:

    docker-compose down

Remove containers and volumes:

    docker-compose down -v

List volumes:

    docker volume list

Remove specific volume:

    docker volume rm <volume_name>

Benefits of This Setup
Development-Friendly:

    Auto-reload for XML changes
    Easy module updates
    Persistent data storage

Containerized Environment:

    Consistent development environment
    Easy to share with team members
    No dependency conflicts

Data Persistence:

    Docker volumes for the database
    Mounted local directories for custom modules
    Configuration persistence

Configuration Files
odoo.conf

    [options]
    addons_path = /mnt/extra-addons
    data_dir = /var/lib/odoo

Troubleshooting

    Port Conflicts: If ports 8000 or 5432 are in use, modify the port mappings in docker-compose.yml.
    Module Not Found: Ensure your module is in the ./addons directory and properly structured.
    Database Reset: Remove the -i base flag after the first run to prevent database reinitialization.

For Team Members

To use this development environment:

    Install Docker Desktop
    Clone this repository
    Run docker-compose up -d
    Access Odoo at http://localhost:8000

All custom modules should be placed in the ./addons directory.
Notes

    The -i base flag should only be used on the first run.
    Use --dev=xml for XML development.
    Use -u module_name to update specific modules.

This should maintain the formatting when pasted into your README file. If you use an editor like VS Code, make sure the file is saved with the .md extension for proper rendering of the markdown.