# wfp2_Flask_API

Dieses Repository enthält eine Flask-basierte API, die für den Einsatz in Docker- und Kubernetes-Umgebungen entwickelt wurde.

## Übersicht

Die API ist eine RESTful-Anwendung, die mit dem Flask-Framework erstellt wurde. Sie bietet flexible Bereitstellungsoptionen, darunter Docker-Container und Kubernetes-Orchestrierung.

## Verzeichnisstruktur

- **`main.py`**: Enthält die Hauptlogik der Flask-Anwendung und definiert die Endpunkte.
- **`requirements.txt`**: Listet alle erforderlichen Python-Pakete auf.
- **`Dockerfile`**: Definiert die Schritte zum Erstellen eines Docker-Images.
- **`deployment.yaml`** und **`service.yaml`**: Kubernetes-Konfigurationsdateien für Deployment und Service.

## Voraussetzungen

- **Python 3.6+**: Für die lokale Entwicklung.
- **Docker**: Zum Containerisieren der Anwendung.
- **Kubernetes**: Für die Bereitstellung in einer Cluster-Umgebung.

## Installation und Ausführung

### Lokale Ausführung

1. **Repository klonen**:
   ```bash
   git clone https://github.com/Aman12b/wfp2_Flask_API.git
   cd wfp2_Flask_API
