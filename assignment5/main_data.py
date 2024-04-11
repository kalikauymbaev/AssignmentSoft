import Data
import DataProcessorCreator
from Processors import TextDataProcessor
from Processors import AudioDataProcessor
from Processors import VideoDataProcessor

def main():
    # Example data instances
    text_data = Data("text", "Example text data")
    audio_data = Data("audio", "/path/to/example/audio")
    video_data = Data("video", "/path/to/example/video")

    # Create the processor creator
    processor_creator = DataProcessorCreator()

    # Process text data
    processor_creator.setProcessor(TextDataProcessor())
    processor_creator.processData(text_data)

    # Process audio data
    processor_creator.setProcessor(AudioDataProcessor())
    processor_creator.processData(audio_data)

    # Process video data
    processor_creator.setProcessor(VideoDataProcessor())
    processor_creator.processData(video_data)

if __name__ == "__main__":
    main()