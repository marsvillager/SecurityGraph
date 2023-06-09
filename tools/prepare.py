import os
import subprocess

from neo4j import GraphDatabase
from tools.config import Config


def update_attack() -> None:
    """
    Download or update mitre source data.
    """
    if os.path.exists(Config.MITRE_ATTACK_DATA_PATH + "enterprise-attack"):
        subprocess.call(["git", "-C", Config.MITRE_ATTACK_DATA_PATH, "pull"], shell=False)
        return
    else:
        subprocess.call(["git", "clone", Config.ATTACK_URL, Config.MITRE_ATTACK_DATA_PATH], shell=False)


def update_d3fend() -> None:
    """
    Download or update mitre source data.
    """
    if os.path.exists(Config.D3FEND_DATA_PATH + "api"):
        subprocess.call(["git", "-C", Config.D3FEND_DATA_PATH, "pull"], shell=False)
        return
    else:
        subprocess.call(["git", "clone", Config.D3FEND_URL, Config.D3FEND_DATA_PATH], shell=False)


def connect_to_neo4j(uri, user, password):
    """
    Define the function to connect to Neo4j.
    """
    driver = GraphDatabase.driver(uri, auth=(user, password))
    return driver
