# Test with adding additional context to a recognizer
# Entity pattern (regex) combined with text (zip, zipcode)
from typing import List
import pprint

from presidio_analyzer import AnalyzerEngine, PatternRecognizer, EntityRecognizer, Pattern, RecognizerResult
from presidio_analyzer.recognizer_registry import RecognizerRegistry
from presidio_analyzer.nlp_engine import NlpEngine, SpacyNlpEngine, NlpArtifacts
from presidio_analyzer.context_aware_enhancers import LemmaContextAwareEnhancer

# Define the regex pattern
regex = r"(\b\d{5}(?:\-\d{4})?\b)" # very weak regex pattern
zipcode_pattern = Pattern(name="zip code (weak)", regex=regex, score=0.01)

# Define the recognizer with the defined pattern
# Define the recognizer with the defined pattern and context words
zipcode_recognizer = PatternRecognizer(supported_entity="US_ZIP_CODE", 
                                       patterns = [zipcode_pattern],
                                       context= ["zip","zipcode"])

registry = RecognizerRegistry()
registry.add_recognizer(zipcode_recognizer)
analyzer = AnalyzerEngine(registry=registry)

# Test
results = analyzer.analyze(text="My zip code is 90210",language="en")
print("Result:")
print(results)