black --target-version py36 --exclude venv/ .
isort -rc .
flake8 . --exclude=venv,./ordasafn/migrations,