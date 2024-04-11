class DataProcessorCreator:
    def __init__(self, processor=None):
        self.processor = processor

    def setProcessor(self, processor):
        self.processor = processor

    def processData(self, data):
        if not self.processor:
            raise ValueError("No processor set for data processing")
        self.processor.process(data)