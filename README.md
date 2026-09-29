# AI Job Analyzer

A simple Python project built as part of the roadmap.sh "OpenAI API in Python" project.

## What it does

The program accepts a job description from the user and sends it to the OpenAI API for analysis.

The AI extracts:
- Job title
- Main responsibilities
- Required skills
- Required qualifications

## Tech stack

- Python
- OpenAI Python SDK
- OpenAI Responses API
- GPT-6 Luna

## Why Responses API

The original roadmap.sh project uses Chat Completions.

This project uses the newer OpenAI Responses API instead, while keeping the same learning goals:
- Send user input to an OpenAI model
- Use model instructions
- Control output length
- Experiment with temperature
- Read and display the model response

## Setup

Install dependencies:

```bash
pip install -r requirements.txt