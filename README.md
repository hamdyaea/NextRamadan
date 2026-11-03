Source code of www.nextramadan.info     
    
   
   
Developer : Hamdy Abou El Anein    
Hamdy Abou El Anein     


## Maintenance and verification

Python 3 with Flask 3.1+. Install `requirements.txt` in an isolated environment. Start with `gunicorn app:app`. Run `python3 -m unittest -v` for offline regression tests. This change is prepared for review only; no production deployment was performed.

The bundled calendar ends in February 2026. Until reviewed future dates are supplied, the site returns HTTP 503 instead of crashing or inventing dates. Local moon-sighting practices must be considered when updating the calendar. The historical Twitter script is not part of the web service and must not run unattended.
