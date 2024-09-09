# 2daw-m12-01-taller-1-poo-python

Codi d'exemple del taller 1: POO amb Python

## Entorn virtual

Per començar a treballar amb un entorn virtual, el primer pas és crear-lo. Per això, obre un terminal integrat des del Visual Code i executa:

Amb linux:

    python3 -m venv .venv

Amb windows:

	python -m venv .venv

El següent pas és activar-lo. Per això executa:

Amb linux:

	source .venv/bin/activate

Amb Windows:

	.venv\Scripts\activate

Al prompt veuràs que ets dins de l'entorn.

Ara ja pots instal·lar els paquets que necessitis, com per exemple:

	pip install flask

Per generar el fitxer `requeriments.txt`: 

    pip freeze > requirements.txt

Aquest fitxer es fa servir per instal·lar exactament les mateixes llibreries:

    pip install -r requirements.txt

Per sortir de l'entorn virtual, executa:

	deactivate
