import DataProcessor

class TextDataProcessor(DataProcessor):
    def process(self, data):
        # Placeholder for text data processing logic
        print(f"Processing text data: {data.content}")

class AudioDataProcessor(DataProcessor):
    def process(self, data):
        # Placeholder for audio data processing logic
        print(f"Processing audio data: {data.content}")

class VideoDataProcessor(DataProcessor):
    def process(self, data):
        # Placeholder for video data processing logic
        print(f"Processing video data: {data.content}")