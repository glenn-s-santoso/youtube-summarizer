from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

class YouTubeSummarizer:
    def __init__(self, api_key):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )
    
    def get_video_id(self, url):
        """Extract video ID from YouTube URL."""
        parsed_url = urlparse(url)
        if parsed_url.hostname in ('youtu.be', 'www.youtu.be'):
            return parsed_url.path[1:]
        if parsed_url.hostname in ('youtube.com', 'www.youtube.com'):
            return parse_qs(parsed_url.query)['v'][0]
        raise ValueError("Not a valid YouTube URL")
    
    def get_transcript(self, video_id):
        """Get transcript of YouTube video."""
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            return ' '.join([entry['text'] for entry in transcript_list])
        except Exception as e:
            raise Exception(f"Failed to get transcript: {str(e)}")
    
    def summarize_text(self, text):
        """Generate summary using OpenRouter API with DeepSeek V3."""
        prompt = f"""Please provide a concise summary of the following video transcript. 
        Focus on the main points and key takeaways. Keep the summary clear and well-structured. We understand that sometimes there are too detailed transcripts that seem like unimportant. In that case, if it still provides some context and help the user better understand, please include it.
        
        Transcript:
        {text}
        """
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="deepseek/deepseek-chat:free",
                temperature=0.3,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            raise Exception(f"Failed to generate summary: {str(e)}")
    
    def process_video(self, url):
        """Process a YouTube video URL and return its summary."""
        video_id = self.get_video_id(url)
        transcript = self.get_transcript(video_id)
        return self.summarize_text(transcript)
