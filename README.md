# AI Inference Monitoring Platform

## Overview:

This project is a backend-based AI inference monitoring and testing platform built with FastAPI. It simulates an AI inference service and focuses on observability, reliability testing, and regression validation of model outputs.

The system logs inference requests, tracks performance metrics such as latency and confidence scores, and provides automated API testing using both pytest and Robot Framework. A CI pipeline ensures tests run automatically on every code change.

## Key Objectives:

- Monitor AI inference behavior over time
- Track latency, confidence, and response consistency
- Provide structured logging for analysis and debugging
- Automate API and regression testing
- Validate system reliability through CI pipelines

## Tech Stack:
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- pytest
- Robot Framework
- GitHub Actions (CI)
