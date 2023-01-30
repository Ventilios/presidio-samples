from typing import List
import pprint

from presidio_analyzer import AnalyzerEngine, PatternRecognizer, EntityRecognizer, Pattern, RecognizerResult
from presidio_analyzer.recognizer_registry import RecognizerRegistry
from presidio_analyzer.nlp_engine import NlpEngine, SpacyNlpEngine, NlpArtifacts
from presidio_analyzer.context_aware_enhancers import LemmaContextAwareEnhancer
from presidio_analyzer.nlp_engine import NlpEngineProvider

#import spacy
#spacy.cli.download("nl_core_news_lg")

# Create configuration containing engine name and models
configuration = {
    "nlp_engine_name": "spacy",
    "models": [{"lang_code": "nl", "model_name": "nl_core_news_lg"},
               {"lang_code": "en", "model_name": "en_core_web_lg"}],
}

# Create NLP engine based on configuration
provider = NlpEngineProvider(nlp_configuration=configuration)
nlp_engine_with_dutch = provider.create_engine()

# Pass the created NLP engine and supported_languages to the AnalyzerEngine
analyzer = AnalyzerEngine(
    nlp_engine=nlp_engine_with_dutch, 
    supported_languages=["nl", "en"]
)

#
# Dutch line of text with some typical Dutch names
text_input = "Mijn naam is Remy en ik ben getrouwd met Geertje. Klaas en Karel zijn m'n beste vrienden."

#
# Analyze the Dutch text with the Dutch Analyzer
results_dutch = analyzer.analyze(text=text_input, language="nl")
print("Results from Dutch request:")
print(results_dutch)

print("Identified these -DUTCH- PII entities:")
for result in results_dutch:
    print(f"- {text_input[result.start:result.end]} as {result.entity_type}")

#
# Analyze the Dutch text with the English Analyzer
results_english = analyzer.analyze(text=text_input, language="en")
print("Results from English request:")
print(results_english)

print("Identified these -ENGLISH- PII entities:")
for result in results_english:
    print(f"- {text_input[result.start:result.end]} as {result.entity_type}")