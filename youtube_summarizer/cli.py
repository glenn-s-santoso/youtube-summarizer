import sys
from .summarizer import YouTubeSummarizer
from dotenv import load_dotenv
import os
import datetime
import pathlib

def main():
    # Load environment variables
    load_dotenv()
    
    # Get API key
    groq_api_key = os.getenv('GROQ_API_KEY')
    openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
    if not groq_api_key or not openrouter_api_key:
        print("Error: GROQ_API_KEY and OPENROUTER_API_KEY not found in environment variables")
        sys.exit(1)
    
    # Initialize summarizer
    summarizer = YouTubeSummarizer(openrouter_api_key)
    
    # Get YouTube URL from user
    url = input("Enter YouTube video URL: ")
    
    try:
        summary = summarizer.process_video(url)
        print("\nSummary:")
        print("-" * 50)
        print(summary)
        print("-" * 50)
        
        # Create output directory if it doesn't exist
        output_dir = pathlib.Path("output")
        output_dir.mkdir(exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = output_dir / f"summary_{timestamp}.md"
        
        # Write summary to markdown file
        with open(output_file, "w") as f:
            f.write(f"# YouTube Video Summary\n\n{summary}")
        
        print(f"Summary saved to {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
