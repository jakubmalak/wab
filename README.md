# wab

## Hello world service
- used project manager: [PDM](https://pdm.fming.dev/latest/)
 - install pdm - `(Invoke-WebRequest -Uri https://pdm.fming.dev/install-pdm.py -UseBasicParsing).Content | python-`
 - init project - `pdm init` - just enter...

- REST Framework: [FastAPI](https://fastapi.tiangolo.com/)
 - add FastAPI - `pdm add fastapi`

- install all dependencies - `pdm install` 
- nainstalovat python extension, spustin python a v dalsim terminalu  spustin fastApi `uvicorn main:app --reload`
---
- create dockerfile
- napsat do konzole - `docker pull python:3.11`
- buildne image se jmenenm wab v aktualnim adresari - `docker build -t wab .`
- spustime image - `docker run wab`
---
- `cd src`
- `uvicorn main:app`