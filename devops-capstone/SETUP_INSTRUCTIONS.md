# INSTRUCCIONES PARA SUBIR EL PROYECTO A GITHUB
# Ejecuta estos comandos en tu terminal local

# 1. Clona tu repositorio vacío
git clone https://github.com/gmaitat/devops-capstone-project.git
cd devops-capstone-project

# 2. Copia todos los archivos del proyecto descargado aquí
#    (reemplaza /ruta/a/los/archivos por donde descargaste el zip)

# 3. Agrega todos los archivos
git add .

# 4. Commit inicial
git commit -m "feat: add complete devops capstone project structure

- Add Flask microservice with CRUD REST API
- Add SQLAlchemy models for Account
- Add unit tests with nosetests (>95% coverage)
- Add GitHub Actions CI pipeline
- Add Dockerfile for containerization
- Add Kubernetes deployment manifests
- Add Tekton CD pipeline
- Add setup.cfg with flake8, pylint, nosetests config"

# 5. Push a main
git push origin main

# ============================================================
# VERIFICACIÓN DE TAREAS (qué responde cada archivo)
# ============================================================
# Tarea 1  → README.md (URL pública con badge de build)
# Tarea 2  → .github/ISSUE_TEMPLATE/user_story.md
# Tarea 7  → setup.cfg (configuración nosetests/flake8/pylint)
# Tarea 21 → .github/workflows/ci-build.yaml
# Tarea 22 → service/__init__.py (Flask-Talisman headers)
