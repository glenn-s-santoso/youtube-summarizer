# YouTube Summarizer

A command-line tool that generates concise summaries of YouTube videos using the Groq API.

## Features

- Extract transcripts from any YouTube video
- Generate summaries using Groq's LLaMA 3.3 70B model
- Save summaries as markdown files
- Simple command-line interface

## Setup

1. **Prerequisites**
   - Python 3.9 or higher
   - Poetry (dependency management)
   - Groq API key

2. **Installation**
   ```bash
   git clone https://github.com/yourusername/youtube-summarizer.git
   cd youtube-summarizer
   poetry install
   ```

3. **Environment Setup**
   ```bash
   cp .env.example .env
   # Edit .env and add your Groq API key
   ```
   Get your Groq API key from [console.groq.com](https://console.groq.com)

## Usage

Run the tool:

```bash
poetry run summarize
```

Or with Poetry shell:

```bash
poetry shell
summarize
```

When prompted, enter a YouTube video URL. The tool will:
- Extract the video transcript
- Generate a summary using Groq API
- Display the summary in the terminal
- Save the summary to a markdown file in the `output` directory

## How It Works

1. Extracts YouTube video ID from the URL
2. Fetches video transcript using YouTube Transcript API
3. Sends transcript to Groq API for summarization
4. Displays and saves the summary

## Dependencies

- youtube-transcript-api
- groq
- python-dotenv