#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from engineering_team.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'feature_name': 'AI Habit Progress Dashboard',
        'service_name': 'habit-tracker-service',
        'repo': 'https://github.com/example/habit-tracker-service'
    }
    
    try:
        EngineeringTeam().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")