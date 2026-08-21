Trust in Artificial Intelligence: A Vignette Study

This repository contains the experimental implementation of my Master's thesis at the Technical University of Munich (TUM).

The study investigates how people perceive and trust advice provided by different sources in a decision-making scenario. The experiment was implemented as an online behavioral study using oTree and deployed for participant data collection.

Project
Thesis: Trust in Artificial Intelligence: A Vignette Study
Platform: oTree
Language: Python
Database: PostgreSQL
Deployment: Heroku
Participants: 150
Experiment

Participants were randomly assigned to different experimental conditions and completed a vignette-based study measuring:

Trust and perceived reliability
Willingness to rely on advice
Perceived competence and integrity
Confidence and responsibility
Intention to use the source in the future
General attitudes toward AI and technology

An attention check was included to ensure participant engagement.

Repository Structure
otreehub-master-thesis/
├── vignette_survey/      # Main experimental application
├── _templates/           # Global templates
├── _static/              # Global static files
├── _rooms/               # oTree room configuration
├── settings.py           # Project configuration
├── requirements.txt      # Python dependencies
└── Procfile              # Heroku deployment
Running Locally
git clone https://github.com/elifbanli/otreehub-master-thesis.git
cd otreehub-master-thesis

python3.12 -m venv otree_env
source otree_env/bin/activate

pip install -r requirements.txt
otree devserver
Academic Context

This project was developed as part of my Master's thesis at TUM and was used for the online implementation and data collection of the study.
