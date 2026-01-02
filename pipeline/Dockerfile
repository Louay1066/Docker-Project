FROM  python:3.13.11-slim
WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"
COPY --from=ghcr.io/astral-sh/uv:latest  /uv /bin
COPY pyproject.toml .python-version uv.lock ./
COPY pipeline.py /app/pipeline.py
RUN uv sync --locked
ENTRYPOINT ["python", "pipeline.py"]
