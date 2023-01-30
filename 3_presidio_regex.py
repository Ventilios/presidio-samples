from typing import List
import pprint

from presidio_analyzer import AnalyzerEngine, PatternRecognizer, EntityRecognizer, Pattern, RecognizerResult
from presidio_analyzer.recognizer_registry import RecognizerRegistry
from presidio_analyzer.nlp_engine import NlpEngine, SpacyNlpEngine, NlpArtifacts
from presidio_analyzer.context_aware_enhancers import LemmaContextAwareEnhancer

# Define the regex pattern in a Presidio 'Pattern' object:
numbers_pattern = Pattern(name="numbers_pattern",regex="[0-9]{9}", score = 0.5)

# Define the recognizer with one or more patterns
number_recognizer = PatternRecognizer(supported_entity="NUMBER", patterns = [numbers_pattern])

text2 = "This will be registered with number 0214567873. The area code is 123456789."

numbers_result = number_recognizer.analyze(text=text2, entities=["NUMBER"])
print("Result:")
print(numbers_result)